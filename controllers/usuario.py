# -*- coding: utf-8 -*-
import hashlib

from flask.helpers import flash

from controllers.emails import EmailController
from dao.mascota_dao import MascotaDao
from dao.usuario_dao import UsuarioDao
from flask import render_template, redirect, url_for, session
from dto.usuario import Usuario


class UsuarioController:
    def __init__(self):
        pass

    def get_registro(self):
        usuario = {
            'nombre': "", 'apellido': "", 'cedula': "", 'genero': "",
            'email': "", 'barrio': "", 'direccion': "", 'fecha_nacimiento': "",
            'telefono': ""}

        return render_template("usuarios/registro.html", usuario=usuario)

    def get_registro1(self):

        return render_template("usuarios/registro1.html")

    def get_registro2(self):

        return render_template("usuarios/registro2.html")

    def crear_usuario(self, cedula, nombre, apellido, genero, email, barrio,
                      direccion, fecha_nacimiento, telefono, contrasena):
        contrasena_c = hashlib.sha1(contrasena).hexdigest()
        usuario = Usuario(cedula=cedula, nombre=nombre, apellido=apellido,
                          genero=genero, email=email, barrio=barrio,
                          direccion=direccion,
                          fecha_nacimiento=fecha_nacimiento,
                          telefono=telefono, contrasena=contrasena_c)

        if UsuarioDao().get_usuario_por_email(usuario) is not None:
            flash("Ya existe un usuario con el email {}.".format(
                usuario.getEmail()), "error")

            return render_template("usuarios/registro.html")

        if UsuarioDao().crear_usuario(usuario):
            flash("El usuario se creo correctamente.", "success")
            return render_template("login/login.html")
        else:
            flash("Error al registrar el usuario.", "error")
        return redirect(url_for("login.get_home"))

    def get_emergencias(self):
        return render_template("plantillas/emergencia.html")

    def get_emergencia_atraganta(self):
        return render_template("emergencias/atragantamiento.html")

    def get_emergencia_traumatismo(self):
        return render_template("emergencias/traumatismo.html")

    def get_perfil(self, id):
        usuario = UsuarioDao().get_usuario_id(id)
        return render_template("usuarios/perfilU.html", usuario=usuario)

    def get_mensaje_privado(self):
        return render_template("emergencias/mensaje.html")

    def enviarMensajeDoc(self, mensaje, id):
        usuario = UsuarioDao().get_usuario_id(id)
        para = 'veterinariacucuta@gmail.com'
        if EmailController().enviar_email(
                para, mensaje+" correo del usuario: "+usuario.getEmail(),
                "Solicitud Consulta - EmergencyPets"):
                msg = u" Se envio correctamente el correo."
                type_flash = "success"
        else:
            msg = u"Error al enviar el correo."
        flash(msg, type_flash)
        return self.get_mensaje_privado()




