
from flask import Flask, Blueprint, jsonify, request
from flask_cors import CORS
import pymysql
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
## Funcion para conectarnos a la base de datos de mysql
admin_blueprint = Blueprint('admin', __name__)

def conectar(vhost,vuser,vpass,vdb):
     conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset = 'utf8mb4')
     return conn
@admin_blueprint.route("/admin")
def consulta_general():
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()

   
        cur.execute("""
            SELECT a.codigo_Administrador, a.nombre, a.apellidos, a.telefono, 
                   a.email, a.clave, t.Usuario
            FROM Administrador a
            INNER JOIN Tipo_Usuario t ON a.Tipo_Usuario_idTipo_Usuario = t.idTipo_Usuario;
        """)

        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'codigo_Administrador': row[0],
                'nombre': row[1],
                'apellidos': row[2],
                'telefono': row[3],
                'email': row[4],
                'clave': row[5],
                'usuario': row[6]  
            }
            data.append(dato)

        cur.close()
        conn.close()
        return jsonify({'Administrador': data, 'mensaje': 'Registros encontrados'})

    except Exception as ex:
        print(f"Error: {ex}")
        return jsonify({'mensaje': 'Error: ' + str(ex)}), 500



@admin_blueprint.route("/registro_Administrador/",methods=['POST'])
def registro_administrador():
    try:
        conn = conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        clave = request.json['clave']
        clave_hash = bcrypt.generate_password_hash(clave).decode('utf-8')
        sql = """ insert into Administrador (codigo_Administrador,nombre,apellidos,telefono,email, clave)
        VALUES (%s, %s, %s, %s, %s,%s) """
        valores = (request.json['codigo_Administrador'],request.json['nombre'],request.json['apellidos'],request.json['telefono'],request.json['email'], clave_hash)
        cur.execute(sql, valores)
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
@admin_blueprint.route("/consulta_individual_Administrador/<codigo>", methods=['GET'])
def consulta_individual(codigo):
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        
        # Ejecutar la consulta con INNER JOIN
        cur.execute("""
            SELECT a.codigo_Administrador, a.nombre, a.apellidos, a.telefono, 
                   a.email, a.clave, t.Usuario
            FROM Administrador a
            INNER JOIN Tipo_Usuario t ON a.Tipo_Usuario_idTipo_Usuario = t.idTipo_Usuario
            WHERE a.codigo_Administrador = %s;
        """, (codigo,))
        
        datos = cur.fetchone()
        cur.close()
        conn.close()

        if datos is not None:
            dato = {
                'codigo_Administrador': datos[0],
                'nombre': datos[1],
                'apellidos': datos[2],
                'telefono': datos[3],
                'email': datos[4],
                'clave': datos[5],
                'usuario': datos[6]  # Campo 'Usuario' de la tabla 'Tipo_Usuario'
            }
            return jsonify({'Administrador': dato, 'mensaje': 'Registro encontrado'})  
        else:
            return jsonify({'mensaje': 'Registro no encontrado'})     
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})


@admin_blueprint.route("/eliminar_Administrador/<codigo>",methods=['DELETE'])
def eliminar(codigo):
    
    
    try:
        conn=conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        x=cur.execute(""" delete from Administrador where codigo_administrador=%s""", (codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'eliminado'}) 
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})  
    
    

    
##rutas para el login 
@admin_blueprint.route("/login_admin", methods=['POST'])
def login():
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        correo = request.json['correo']
        clave = request.json['clave']
        cur.execute(""" SELECT * FROM Administrador WHERE correo = %s """, (correo))
        datos = cur.fetchone()
        cur.close()
        conn.close()
        if datos and bcrypt.check_password_hash(datos[5], clave):
            return jsonify({'mensaje': 'Login successful'})
        else:
            return jsonify({'mensaje': 'Invalid credentials'}), 401
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
app.register_blueprint(admin_blueprint, url_prefix='/api')  

if __name__=='__main__':
    app.run(debug=True)