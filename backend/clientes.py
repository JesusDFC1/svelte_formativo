from flask import Flask, Blueprint, jsonify, request
from flask_cors import CORS
import pymysql
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

cliente_blueprint = Blueprint('clientes', __name__)

def conectar(vhost, vuser, vpass, vdb):
    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset='utf8mb4')
    return conn

@cliente_blueprint.route("/clientes")
def consulta_general():
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM clientes """)
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {'idcliente': row[0], 'nombres': row[1], 'apellidos': row[2], 'telefono': row[3], 'correo': row[4], 'clave': row[5]}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify({'clientes': data, 'mensaje': 'Registros encontrados'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@cliente_blueprint.route("/registro_cliente/", methods=['POST'])
def registro_cliente():
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        clave = request.json['clave']
        clave_hash = bcrypt.generate_password_hash(clave).decode('utf-8')
        # Usa parámetros para evitar inyección SQL y errores de índice
        sql = """
            INSERT INTO clientes (idclientes,nombres, apellidos, telefono, correo, clave) 
            VALUES (%s, %s, %s, %s, %s,%s)
        """
        valores = (request.json['idclientes'],request.json['nombres'], request.json['apellidos'], request.json['telefono'], request.json['correo'], clave_hash)
        cur.execute(sql, valores)
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

@cliente_blueprint.route("/consulta_individual_clientes/<codigo>", methods=['GET'])
def consulta_individual(codigo):
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM clientes WHERE idcliente = %s """, (codigo,))
        datos = cur.fetchone()
        cur.close()
        conn.close()
        if datos:
            dato = {'idcliente': datos[0], 'nombres': datos[1], 'apellidos': datos[2], 'telefono': datos[3], 'correo': datos[4], 'clave': datos[5]}
            return jsonify({'cliente': dato, 'mensaje': 'Registro encontrado'})
        else:
            return jsonify({'mensaje': 'Registro no encontrado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

@cliente_blueprint.route("/eliminar_clientes/<codigo>", methods=['DELETE'])
def eliminar(codigo):
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        cur.execute(""" DELETE FROM clientes WHERE idcliente = %s """, (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

@cliente_blueprint.route("/login", methods=['POST'])
def login():
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        correo = request.json['correo']
        clave = request.json['clave']
        cur.execute(""" SELECT * FROM clientes WHERE correo = %s """, (correo,))
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

app.register_blueprint(cliente_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
