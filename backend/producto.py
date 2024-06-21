from flask import Flask
from flask_cors import CORS
from flask import Blueprint, jsonify,request
import pymysql

producto_blueprint = Blueprint('producto', __name__)

def conectar(vhost, vuser, vpass, vdb):
    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset='utf8mb4')
    return conn

@producto_blueprint.route("/producto", methods=['GET'])
def consulta_general():
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        cur.execute("""select * from producto""")
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {'id_productos': row[0], 'codigo_productos': row[1], 'nombre_producto': row[2], 'precio': float(row[3]), 'descripcion':(row[4]),}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify({'productos': data, 'mensaje': 'Registros encontrados'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@producto_blueprint.route("/consulta_individual_producto/<codigo>", methods=['GET'])
def consulta_individual_producto(codigo):
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        cur.execute("""select * from producto WHERE id_productos='{0}'""".format(codigo))
        datos = cur.fetchone()
        cur.close()
        conn.close()
        if datos != None:
            dato = {'id_productos': datos[0], 'codigo_productos': datos[1], 'nombre_producto': datos[2], 'precio': float(datos[3]), 'descripcion': datos[4],}
            return jsonify({'Producto': dato, 'mensaje': 'Registro encontrado'})
        else:
            return jsonify({'mensaje': 'Registro no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@producto_blueprint.route("/registro_producto", methods=['POST'])
def registro_producto():
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        cur.execute("""insert intro producto (codigo_productos, nombre_producto, precio, descripcion,imagen) VALUES
                    ('{0}', '{1}', {2}, '{3}','{4}',)""".format(request.json['codigo_productos'], request.json['nombre_producto'],request.json['precio'], request.json['descripcion'],))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@producto_blueprint.route("/eliminar_producto/<codigo>", methods=['DELETE'])
def eliminar_producto(codigo):
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        cur.execute("""DELETE FROM producto WHERE id_productos='{0}'""".format(codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro eliminado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@producto_blueprint.route("/actualizar_producto/<codigo>", methods=['PUT'])
def actualizar_producto(codigo):
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        cur.execute("""
            UPDATE producto
            SET codigo_productos='{0}', nombre_producto='{1}', precio={2}, descripcion='{3}',id_productos='{4}',imagen='{5}'""".format(request.json['codigo_productos'], request.json['nombre_producto'], request.json['precio'], request.json['descripcion'],codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro actualizado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})
    
if __name__ == '__main__':
   producto_blueprint.run(debug=True)