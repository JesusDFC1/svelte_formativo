from flask import Flask
from flask_cors import CORS
from producto import producto_blueprint
from clientes import cliente_blueprint
from tipo_usuario import tipo_admin_blueprint
from admin import admin_blueprint
from reporte import reporte_blueprint


app = Flask(__name__)
CORS(app)

##rutas para el login 
# @admin_blueprint.route("/login_admin", methods=['POST'])#iniciar admin
# @cliente_blueprint.route("/login_estandar", methods=['POST'])#iniciar usuario estandar

# #rutas tabla admin
# @admin_blueprint.route("/admin") #consulta general
# @admin_blueprint.route("/registro_Administrador/",methods=['POST'])#registrar admin
# @admin_blueprint.route("/consulta_individual_Administrador/<codigo>",methods=['GET'])#consulta individual
# @admin_blueprint.route("/eliminar_Administrador/<codigo>",methods=['DELETE'])#eliminar admin
# #rutas tabla cliente
# @cliente_blueprint.route("/clientes")#consulta general clientes
# @cliente_blueprint.route("/registro_cliente/", methods=['POST'])#registrar cliente
# @cliente_blueprint.route("/consulta_individual_clientes/<codigo>", methods=['GET'])#consultar un cliente individual
# @cliente_blueprint.route("/eliminar_clientes/<codigo>", methods=['DELETE'])#eliminar cliente

# #rutas tablas productos
# @producto_blueprint.route("/producto", methods=['GET'])#consulta general de los productos
# @producto_blueprint.route("/consulta_individual_producto/<codigo>", methods=['GET'])#consulta individual de los productos
# @producto_blueprint.route("/registro_producto", methods=['POST'])#registrar productos
# @producto_blueprint.route("/eliminar_producto/<codigo>", methods=['DELETE'])#eliminar productos
# @producto_blueprint.route("/actualizar_producto/<codigo>", methods=['PUT'])#actualizar productos

# #tabla reporte
# @reporte_blueprint.route("/reporte", methods=['GET'])#consulta general
# @reporte_blueprint.route("/consulta_individual_reporte/<codigo>", methods=['GET'])#consulta individual
# @reporte_blueprint.route("/registro_reporte", methods=['POST'])#registrar reportes 
# @reporte_blueprint.route("/eliminar_reporte/<codigo>", methods=['DELETE'])#eliminar reportes

#tabla para agregar img, a verdad aqui no se agrega productos


# tabla tipo de usuario
# @tipo_admin_blueprint.route("/tipo_usuario")#consulta general



app.register_blueprint(admin_blueprint)#/consulta_admin
app.register_blueprint(cliente_blueprint)#/consulta_clientes
app.register_blueprint(tipo_admin_blueprint)#/consulta_tipo_usuario
app.register_blueprint(producto_blueprint)
app.register_blueprint(reporte_blueprint)












if __name__ == '__main__':
    
    app.run(debug=True ,port=8080,use_reloader=False)
