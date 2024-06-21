
from flask import Flask
from flask_cors import CORS
from flask import Blueprint, jsonify,request
import pymysql
# app=Flask(__name__)
# CORS(app)
## Funcion para conectarnos a la base de datos de mysql
admin_blueprint = Blueprint('admin', __name__)
def conectar(vhost,vuser,vpass,vdb):
     conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset = 'utf8mb4')
     return conn 
#TABLA ADMINISTRADOR
@admin_blueprint.route("/admin")
def consulta_general():
     try:
         conn=conectar('localhost','root','','emprendimiento')
         cur = conn.cursor()
         cur.execute(""" SELECT * FROM Administrador """)
         #Extre todos los registros que se encuentran en el cursor cur
         datos=cur.fetchall()
         data=[]
         for row in datos:
             dato={'codigo_Administrador':row[0],'nombre':row[1],'apellidos':row[2],'telefono':row[3],'email':row[4]}
             data.append(dato)
         cur.close()
         conn.close()
         return jsonify({'Administrador':data,'mensaje':'Registros encontrados'})
     except Exception as ex:
         return jsonify({'mensaje':'Error'})


@admin_blueprint.route("/registro_Administrador/",methods=['POST'])
def registro_administrador():
    try:
        conn = conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        x = cur.execute(""" insert into Administrador (codigo_Administrador,nombres,apellidos,telefono,email) values
            ('{0}',{1},{2},{3},{4},')""".format(request.json['codigo_Administrador'],request.json['nombres'],request.json['apellidos'],request.json['telefono'],request.json['email'],))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
    
@admin_blueprint.route("/consulta_individual_Administrador/<codigo>",methods=['GET'])
def consulta_individual(codigo):
    try:
        conn=conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM Administrador where codigo_Administrador='{0}' """.format(codigo))
        datos=cur.fetchone()
        cur.close()
        conn.close()
        if datos!=None:
            dato={'codigo_Administrador':datos[0],'nombre':datos[1],'apellidos':datos[2],'telefono':datos[3],'email':datos[3]}
            return jsonify({'Administrador':dato,'mensaje':'Registro encontrado'})  
        else:
            return jsonify({'mensaje':'Registro no encontrado'})     
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
    
@admin_blueprint.route("/eliminar_Administrador/<codigo>",methods=['DELETE'])
def eliminar(codigo):
    
    
    try:
        conn=conectar('localhost','root','','emprendimiento')
        cur = conn.cursor()
        x=cur.execute(""" delete from Administrador where codigo_administrador={0}""".format(codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'eliminado'}) 
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})  
    
if __name__=='__main__':
      
    admin_blueprint.run(debug=True ,port=8080,use_reloader=False)  