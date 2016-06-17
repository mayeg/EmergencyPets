from flask.blueprints import Blueprint
from flask import request, session
from flask.helpers import flash
from werkzeug.utils import redirect

from controllers.mascota import MascotaController

mascota = Blueprint("mascotas", __name__)


@mascota.route("/registro", methods=["GET", "POST"])
def registro_mascota():
    if request.method == "GET":
        id = session['usuario']['id']
        return MascotaController().get_registro(id)
    nombre = request.form.get('nombre', None)
    dueno = session['usuario']['id']
    fecha_nacimiento = request.form.get('fecha_nacimiento', None)
    raza = request.form.get('raza', None)
    genero = request.form.get('genero', None)
    vacunas = request.form.get('vacunas', None)
    file = request.files['foto']
    if file.filename == '':
        flash('No selecciono el archivo', 'Error')
        return redirect(request.url)
    especie = request.form.get('especie', None)
    peso_aprox = request.form.get('peso_aprox', None)
    return MascotaController().crear_mascota(nombre, dueno, fecha_nacimiento,
                                             raza, genero, vacunas, file,
                                             especie, peso_aprox)


@mascota.route("/listar", methods=["GET"])
def listar_mascotas():
    return MascotaController().mascotas_usuario()



@mascota.route("/ver/<id>", methods=["GET"])
def ver_mascotas(id):
    id_usuario = session['usuario']['id']
    return MascotaController().get_ver_mascota(id,id_usuario)


@mascota.route("/editar", methods=["GET", "POST"])
def editar_mascota():
    id_usuario = session['usuario']['id']
    if request.method == "GET":
        return MascotaController().get_editar_mascota(id_usuario)

    nombre = request.form.get('nombre', None)
    dueno = session['usuario']['id']
    fecha_nacimiento = request.form.get('fecha_nacimiento', None)
    raza = request.form.get('raza', None)
    genero = request.form.get('genero', None)
    vacunas = request.form.get('vacunas', None)
    file = request.files['foto']
    if file.filename == '':
        flash('No selecciono el archivo', 'Error')
        return redirect(request.url)
    especie = request.form.get('especie', None)
    peso_aprox = request.form.get('peso_aprox', None)

    return MascotaController().editar_mascota(id_usuario, nombre, dueno,
                                              fecha_nacimiento, raza, genero,
                                              vacunas, file, especie, peso_aprox)