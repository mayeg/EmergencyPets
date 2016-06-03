from flask.blueprints import Blueprint
from flask import request, redirect, url_for
from flask.globals import session

from controllers.usuario import  UsuarioController
from dao.usuario_dao import UsuarioDao

emergencia = Blueprint("emergencia", __name__)

@emergencia.route("/", methods=["GET"])
def get_home():
    return UsuarioController().get_emergencias()

@emergencia.route("/atragantamiento", methods=["GET"])
def get_atragantamiento():
    return UsuarioController().get_emergencia_atraganta()


@emergencia.route("/traumatismo", methods=["GET"])
def get_traumatismo():
    return UsuarioController().get_emergencia_traumatismo()

@emergencia.route("/mensaje", methods=["GET","POST"])
def get_mensaje():
    if request.method == "GET":
        return UsuarioController().get_mensaje_privado()
    mensaje = request.form.get('cedula', None)
    id = session['usuario']['id']
    return UsuarioController().enviarMensajeDoc(mensaje,id)
