from flask.blueprints import Blueprint
from flask import request, session

from controllers.usuario import UsuarioController

usuario = Blueprint("usuarios", __name__)


@usuario.route("/registro", methods=["GET", "POST"])
def registro_usuario():
    if request.method == "GET":
        return UsuarioController().get_registro()
    print "se fue por post"
    cedula = request.form.get('cedula', None)
    nombre = request.form.get('nombre', None)
    apellido = request.form.get('apellido', None)
    genero = request.form.get('genero', None)
    email = request.form.get('email', None)
    barrio = request.form.get('barrio', None)
    direccion = request.form.get('direccion', None)
    fecha_nacimiento = request.form.get('fecha_nacimiento', None)
    telefono = request.form.get('telefono', None)
    contrasena = request.form.get('contrasena', None)
    return UsuarioController().crear_usuario(cedula, nombre, apellido, genero,
                                             email, barrio, direccion,
                                             fecha_nacimiento, telefono,
                                             contrasena)
@usuario.route("/registro1", methods=["GET", "POST"])
def registro_usuario1():
    if request.method == "GET":
        return UsuarioController().get_registro1()
    print "se fue por post"
    cedula = request.form.get('cedula', None)
    nombre = request.form.get('nombre', None)
    apellido = request.form.get('apellido', None)
    genero = request.form.get('genero', None)
    email = request.form.get('email', None)
    barrio = request.form.get('barrio', None)
    direccion = request.form.get('direccion', None)
    fecha_nacimiento = request.form.get('fecha_nacimiento', None)
    telefono = request.form.get('telefono', None)
    contrasena = request.form.get('contrasena', None)
    return UsuarioController().crear_usuario(cedula, nombre, apellido, genero,
                                             email, barrio, direccion,
                                             fecha_nacimiento, telefono,
                                             contrasena)

@usuario.route("/registro2", methods=["GET", "POST"])
def registro_usuario2():
    if request.method == "GET":
        return UsuarioController().get_registro2()
    print "se fue por post"
    cedula = request.form.get('cedula', None)
    nombre = request.form.get('nombre', None)
    apellido = request.form.get('apellido', None)
    genero = request.form.get('genero', None)
    email = request.form.get('email', None)
    barrio = request.form.get('barrio', None)
    direccion = request.form.get('direccion', None)
    fecha_nacimiento = request.form.get('fecha_nacimiento', None)
    telefono = request.form.get('telefono', None)
    contrasena = request.form.get('contrasena', None)
    return UsuarioController().crear_usuario(cedula, nombre, apellido, genero,
                                             email, barrio, direccion,
                                             fecha_nacimiento, telefono,
                                             contrasena)

@usuario.route("/perfil", methods=["GET"])
def perfil_usuario():
    id = session['usuario']['id']
    return UsuarioController().get_perfil(id)