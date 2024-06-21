from flask import Flask
from flask_cors import CORS
from producto import producto_blueprint
from clientes import cliente_blueprint
from tipo_usuario import tipo_admin_blueprint
from admin import admin_blueprint
from reporte import reporte_blueprint


app = Flask(__name__)
CORS(app)

app.register_blueprint(admin_blueprint)#/consulta_admin
app.register_blueprint(cliente_blueprint)#/consulta_clientes
app.register_blueprint(tipo_admin_blueprint)#/consulta_tipo_usuario
app.register_blueprint(producto_blueprint)
app.register_blueprint(reporte_blueprint)












if __name__ == '__main__':
    
    app.run(debug=True ,port=8080,use_reloader=False)