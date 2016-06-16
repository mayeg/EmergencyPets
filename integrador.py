# -*- coding: utf-8 -*-
import os
from flask import Flask
from flaskext.mysql import MySQL
from routes.emergencia_routes import emergencia
from routes.login_routes import login_r
from routes.usuario_routes import usuario
from routes.mascota_routes import mascota

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'views')
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'uploads')
app = Flask(__name__, template_folder=tmpl_dir)
app.secret_key = 'proyecto_ufps'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mysql = MySQL()

# import routes
app.register_blueprint(login_r)
app.register_blueprint(usuario, url_prefix="/usuarios")
app.register_blueprint(mascota, url_prefix="/mascotas")
app.register_blueprint(emergencia, url_prefix="/emergencia")

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'ufps_34'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ufps_pp'
app.config['MYSQL_DATABASE_DB'] = 'ufps_34'
app.config['MYSQL_DATABASE_HOST'] = 'sandbox2.ufps.edu.co'
mysql.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
