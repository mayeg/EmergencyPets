from flask.blueprints import Blueprint
from flask import request, session

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
    foto = request.form.get('foto', None)
    especie = request.form.get('especie', None)
    peso_aprox = request.form.get('peso_aprox', None)
    return MascotaController().crear_mascota(nombre, dueno, fecha_nacimiento,
                                             raza, genero, vacunas, foto,
                                             especie, peso_aprox)


@mascota.route("/listar", methods=["GET"])
def listar_mascotas():
    return MascotaController().mascotas_usuario()


