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


    def get_editar_mascota(self, id_usuario):
        usuario = Usuario(id=id_usuario)
        usuario_e = UsuarioDao().get_usuario_id(usuario.getId())
        mascota_e = MascotaDao().get_mascota_dueno(usuario)
        print mascota_e, "controller"
        mascota_edit = {
            'nombre': mascota_e.getNombre(),
            'foto': mascota_e.getFoto(),
            'raza': mascota_e.getRaza(),
            'vacunas': mascota_e.getVacunas(),
            'genero': mascota_e.getGenero(),
            'fecha_nacimiento': mascota_e.getFecha_nacimiento(),
            'especie': mascota_e.getEspecie(),
            'peso_aprox': mascota_e.getPeso_aprox()
        }

        if mascota_e is None:
            flash("La mascota  que intenta editar no existe.", "error")
        return render_template(
            "usuarios/editar_mascota.html", mascota_edit=mascota_edit,
            id=id_usuario, usuario=usuario_e)

    def editar_mascota(self, id_usuario, nombre, dueno, fecha_nacimiento, raza,
                       genero,  vacunas, file, especie, peso_aprox ):
        from integrador import UPLOAD_FOLDER
        filename = str(datetime.now().microsecond) + secure_filename(
            file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        mascota = Mascota(id=id_usuario, nombre=nombre, dueno=dueno,
                          fecha_nacimiento=fecha_nacimiento, raza=raza,
                          genero=genero, vacunas=vacunas, foto=filename,
                          especie=especie, peso_aprox=peso_aprox)

        if MascotaDao().editar_mascota(mascota):
            flash("El usuario se edito correctamente.", "success")
        else:
            flash("Error al editar el usuario.", "error")
        return redirect(url_for("login.get_home"))
