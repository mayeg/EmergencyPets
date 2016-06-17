# -*- coding: utf-8 -*-
import hashlib
import os
from flask.helpers import flash
from dao.mascota_dao import MascotaDao
from flask import render_template, redirect, url_for, session
from datetime import datetime
from dao.usuario_dao import UsuarioDao
from dto.mascota import Mascota
from dto.usuario import Usuario
from werkzeug.utils import secure_filename

class MascotaController:
    def __init__(self):
        pass

    def get_registro(self, id):

        mascota = {'nombre': "", 'fecha_nacimiento': "", 'raza': "",
                   'genero': "", 'vacunas': "", 'foto': "", 'especie': "",
                   'peso_aprox': 0}

        usuario = UsuarioDao().get_usuario_id(id)
        print usuario

        return render_template("usuarios/registromascota.html", user=usuario,
                               mascota=mascota)

    def crear_mascota(self, nombre, dueno, fecha_nacimiento, raza, genero,
                      vacunas, file, especie, peso_aprox):
        from integrador import UPLOAD_FOLDER
        filename = str(datetime.now().microsecond) + secure_filename(
            file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        mascota = Mascota(nombre=nombre, dueno=dueno,
                          fecha_nacimiento=fecha_nacimiento, raza=raza,
                          genero=genero, vacunas=vacunas, foto=filename,
                          especie=especie, peso_aprox=peso_aprox)

        if MascotaDao().crear_mascota(mascota):
            flash("La mascota se creo correctamente.", "success")
        else:
            flash("Error al registrar el mascota.", "error")
        return redirect(url_for("login.get_home"))


    def mascotas_usuario(self):
        ide = session['usuario']['id']
        nombre = session['usuario']['nombre']
        usuario = Usuario(id=ide, nombre=nombre)
        mascotas = MascotaDao().listar_mascotas(usuario)
        return render_template("usuarios/listar_mascotas.html", usuario=usuario,
                        mascotas=mascotas)
