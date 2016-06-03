# -*- coding: utf-8 -*-
import hashlib

from flask.helpers import flash
from dao.mascota_dao import MascotaDao
from flask import render_template, redirect, url_for, session

from dao.usuario_dao import UsuarioDao
from dto.mascota import Mascota
from dto.usuario import Usuario


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
                      vacunas, foto, especie, peso_aprox):

        mascota = Mascota(nombre=nombre, dueno=dueno,
                          fecha_nacimiento=fecha_nacimiento, raza=raza,
                          genero=genero, vacunas=vacunas, foto=foto,
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
        render_template("usuarios/listar_mascotas.html", usuario=usuario,
                        mascotas=mascotas)