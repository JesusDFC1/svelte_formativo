from flask import Flask
from flask_cors import CORS
from flask import Blueprint, jsonify,request
import pymysql


reporte_blueprint = Blueprint('reporte', __name__)

def conectar(vhost, vuser, vpass, vdb):
    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset='utf8mb4')
    return conn

@reporte_blueprint.route("/reporte", methods=['GET'])
def consulta_general_reporte():
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Reporte""")
        datos = cur.fetchall()
        data = []
        for row in datos:
            dato = {
                'id_Reporte': row[0],
                'descripcion': row[1],
                'fecha_reporte': row[2].strftime('%Y-%m-%d'),
                'clientes_idclientes': row[3],
                'Administrador_codigo_Administrador': row[4]
            }
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify({'Reportes': data, 'mensaje': 'Registros encontrados'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@reporte_blueprint.route("/consulta_individual_reporte/<codigo>", methods=['GET'])
def consulta_individual_reporte(codigo):
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Reporte WHERE id_Reporte='{0}'""".format(codigo))
        datos = cur.fetchone()
        cur.close()
        conn.close()
        if datos != None:
            dato = {
                'id_Reporte': datos[0],
                'descripcion': datos[1],
                'fecha_reporte': datos[2].strftime('%Y-%m-%d'),
                'clientes_idclientes': datos[3],
                'Administrador_codigo_Administrador': datos[4]
            }
            return jsonify({'Reporte': dato, 'mensaje': 'Registro encontrado'})
        else:
            return jsonify({'mensaje': 'Registro no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@reporte_blueprint.route("/registro_reporte", methods=['POST'])
def registro_reporte():
    try:
        conn = conectar('localhost', 'root', '', 'emprendimiento')
        cur = conn.cursor()
        cur.execute("""INSERT INTO Reporte (descripcion, fecha_reporte, clientes_idclientes, Administrador_codigo_Administrador) VALUES
                    ('{0}', '{1}', {2}, {3})""".format(request.json['descripcion'], request.json['fecha_reporte'], request.json['clientes_idclientes'], request.json['Administrador_codigo_Administrador']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@reporte_blueprint.route("/eliminar_reporte/<codigo>", methods=['DELETE'])
def eliminar_reporte(codigo):
  try:
    conn = conectar('localhost', 'root', '', 'emprendimiento')
    cur = conn.cursor()
    cur.execute("""DELETE FROM Reporte WHERE id_Reporte='{0}'""".format(codigo))
    conn.commit()

    # Check if rows were affected (i.e., report deleted)
    row_count = cur.rowcount
    cur.close()
    conn.close()

    if row_count > 0:
      return jsonify({'mensaje': 'Registro eliminado exitosamente'})
    else:
      return jsonify({'mensaje': 'Registro no encontrado'})

  except Exception as ex:
    return jsonify({'mensaje': 'Error'})
if __name__ == '__main__':
   reporte_blueprint.run(debug=True)