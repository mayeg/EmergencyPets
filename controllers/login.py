# -*- coding: utf-8 -*-
import hashlib

from flask import session, render_template
from flask.helpers import flash

from controllers.emails import EmailController
from dao.usuario_dao import UsuarioDao
from dto.usuario import Usuario

from dao.mascota_dao import  Mascota
from dto.mascota import  Mascota

class Login:

    def __init__(self):
        pass

    @staticmethod
    def get_home_usuario():
        if 'usuario' in session:
            return render_template('plantillas/perfil.html', nombre=session['usuario']['nombre'])
        return render_template('home/index.html')

    @staticmethod
    def get_login_iniciar():
        if 'usuario' in session:
            return render_template('plantillas/perfil.html', nombre=session['usuario']['nombre'])
        return render_template('login/login.html')

    def login(self, email, contrasena):
        contrasena_c = hashlib.sha1(contrasena).hexdigest()
        usuario = Usuario(email=email, contrasena=contrasena_c)
        usuario_logueado = UsuarioDao().get_user_login(usuario)
        if usuario_logueado is not None:
            session['usuario'] = usuario_logueado.get_dict()

    def get_cambiar_contrasena(self, token):
        usuario = UsuarioDao().get_usuario_por_token(
            Usuario(token_password=token))
        if usuario is None:
            flash(u"El token no es valido para el cambio de contraseña.",
                  'error')
            return False
        return render_template('login/cambiar_contraseña.html', token=token)

    def cambiar_contrasena_olvidada(self, contrasena_1, contrasena_2, token):
        if contrasena_2 != contrasena_1:
            flash(u"Las contraseñas no coinciden.", "Error")
            return
        usuario = UsuarioDao().get_usuario_por_token(
            Usuario(token_password=token))
        if usuario is None:
            flash(u"El token no es valido para el cambio de contraseña.",
                  'error')
            return
        usuario.setTokenPassword(None)
        usuario.setContrasena(hashlib.sha1(contrasena_1).hexdigest())
        if UsuarioDao().cambiar_recordar_contrasena(usuario):
            flash(u"Contraseña actualizada correctamente.", 'success')
        else:
            flash(u"Error al cambiar la contraseña, intente nuevamente.",
                  "error")

    def get_recordar_contrasena(self):
        return render_template("login/olvide_contraseña.html")

    def recordar_contrasena(self, email):
        usuario_c = UsuarioDao().get_usuario_por_email(Usuario(email=email))
        type_flash = "error"
        if usuario_c is None:
            msg = "El usuario no existe en el sistema."
        else:
            token = hashlib.sha1(
                str(usuario_c.getId()) + usuario_c.getCedula()).hexdigest()
            usuario_c.setTokenPassword(token)
            mensaje = "Para realizar el cambio de contraseña en el sistema " \
                      "haga <a href='https://emergencypets.herokuapp.com//cambiar_contrasena/"+ \
                      usuario_c.getTokenPassword() + "'>clic aquí.</a>"
            if EmailController().enviar_email(
                    usuario_c.getEmail(), mensaje,
                    "Cambio de Contraseña - EmergencyPets"):
                if not UsuarioDao().editar_usuario(usuario_c):
                    msg = u"Error al realizar el cambio de la contraseña."
                else:
                    msg = u"Se ha un email con las intrucciones para " \
                          u"restablecer su contraseñas."
                    type_flash = "success"
            else:
                msg = u"Error al enviar el email de cambio de contraseña."
        flash(msg, type_flash)

    def logout(self):
        del session['usuario']