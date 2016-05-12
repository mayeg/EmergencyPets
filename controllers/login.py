# -*- coding: utf-8 -*-
import hashlib

from flask import session, render_template

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
            return render_template('plantillas/perfil.html', nombre=session['usuario']['email'])
        return render_template('home/index.html')

    @staticmethod
    def get_login_iniciar():
        if 'usuario' in session:
            return render_template('plantillas/perfil.html', nombre=session['usuario']['email'])
        return render_template('login/login.html')

    def login(self, email, contrasena):
        contrasena_c = hashlib.sha1(contrasena).hexdigest()
        usuario = Usuario(email=email, contrasena=contrasena_c)
        usuario_logueado = UsuarioDao().get_user_login(usuario)
        if usuario_logueado is not None:
            session['usuario'] = usuario_logueado.get_dict()

    def logout(self):
        del session['usuario']