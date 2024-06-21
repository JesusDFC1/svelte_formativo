
from flask import Flask
from flask_cors import CORS
from flask import Blueprint,jsonify,request
import pymysql
# app=Flask(__name__)
# CORS(app)
## Funcion para conectarnos a la base de datos de mysql
tipo_admin_blueprint = Blueprint('tipo_usuario',__name__)
def conectar(vhost,vuser,vpass,vdb):
     conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset = 'utf8mb4')
     return conn
 #Tabla tipo_Usuario
@tipo_admin_blueprint.route("/tipo_usuario")
def consulta_general():
     try:
         conn=conectar('localhost','root','','emprendimiento')
         cur = conn.cursor()
         cur.execute(""" SELECT * FROM Tipo_Usuario """)
         #Extre todos los registros que se encuentran en el cursor cur
         datos=cur.fetchall()
         data=[]
         for row in datos:
             dato={'idTipo_Usuario':row[0],'nombre':row[1]}
             data.append(dato)
         cur.close()
         conn.close()
         return jsonify({'Tipo_Usuario':data,'mensaje':'Registros encontrados'})
     except Exception as ex:
         return jsonify({'mensaje':'Error'})

@tipo_admin_blueprint.route("/consulta_usuario/<codigo>",methods=['GET'])
def consulta_usuario(codigo):
     try:
         conn=conectar('localhost','root','','emprendimiento')
         cur = conn.cursor()
         cur.execute(""" SELECT * FROM Tipo_usuario where nombre='{0}' """.format(codigo))
         datos=cur.fetchone()
         cur.close()
         conn.close()
         if datos!=None:
             dato={'idTipo_usuario':datos[0],'nombre':datos[1],}
         else:
             return jsonify({'mensaje':'Registro no encontrado'})
     except Exception as ex:
         print(ex)
         return jsonify({'mensaje':'Error'})

@tipo_admin_blueprint.route("/registro_tipo_usuario/",methods=['POST'])
def registro_tipo_usuario():
    try:
        conn = conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        x = cur.execute(""" insert into Tipo_Usuario  ( idTipo_Usuario,nombre) values   
           ('{0}',{1})""".format(request.json['idTipo_Usuario'],request.json['nombre']))
        conn.commit() 
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro agregado'}) 
    except Exception as ex:
         print(ex)
         return jsonify({'mensaje':'Error'})
        
@tipo_admin_blueprint.route("/eliminar_Tipo_Usuario/<codigo>",methods=['DELETE'])
def eliminar(codigo):
    try:
        conn=conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        x=cur.execute(""" delete from Tipo_Usuario where id_baul={0}""".format(codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'eliminado'}) 
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})        
        
        
        
    

if __name__=='__main__':
    tipo_admin_blueprint.run(debug=True)