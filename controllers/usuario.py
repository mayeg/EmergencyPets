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

    def get_home_user(self):
        id = session['usuario']['id']
        usuario = UsuarioDao().get_usuario_id(id)
        return render_template("usuarios/home.html",  usuario=usuario)


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

            mensaje = "BIENVENIDO A EMERGENCY PETS:\ Aqui podras registrar" \
                      "tu mascota y tener un control con las emergencias que" \
                      "presente."
            if EmailController().enviar_email(usuario.getEmail(), mensaje,
                "Registro Existoso - EmergencyPets"):
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
        return redirect(url_for("emergencia.get_mensaje"))

    def get_editar_usuario(self, id_usuario):
        usuario = Usuario(id=id_usuario)
        usuario_e = UsuarioDao().get_usuario_id(usuario.getId())
        usuario_edit = {
            'nombre': usuario_e.getNombre(),
            'apellido': usuario_e.getApellido(),
            'genero': usuario_e.getGenero(),
            'telefono': usuario_e.getTelefono(),
            'fecha_nacimiento': usuario_e.getFecha_nacimiento(),
            'barrio': usuario_e.getBarrio(),
            'direccion': usuario_e.getDireccion(),
            'cedula': usuario_e.getCedula(),
            'email': usuario_e.getEmail()
        }

        if usuario_e is None:
            flash("El usuario que intenta editar no existe.", "error")
        return render_template(
            "usuario/editar.html", usuario_edit=usuario_edit, id=id_usuario)


    def editar_usuario(self, nombre, apellido, cedula, email,id,genero,telefono,
                       fecha_nacimiento,barrio,direccion):

        usuario_e = Usuario(id=id, cedula=cedula, nombre=nombre, apellido=apellido,
                            genero=genero, email=email, barrio=barrio,
                            direccion=direccion, fecha_nacimiento=fecha_nacimiento,
                            telefono=telefono)

        if UsuarioDao().editar_usuario(usuario_e):
            flash("El usuario se edito correctamente.", "success")
        else:
            flash("Error al editar el usuario.", "error")
        return redirect(url_for("usuarios.get_home"))



