# -*- coding: utf-8 -*-
from dto.mascota import Mascota


class MascotaDao:
    def __init__(self):
        from integrador import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def crear_mascota(self, mascota):
            try:
                query = "INSERT INTO mascota (nombre, dueno, fecha_nacimiento,"\
                        "raza, genero, vacunas, foto, especie, peso_aprox) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

                param = (mascota.getNombre(), mascota.getDueno().getId(),
                         str(mascota.getFecha_nacimiento()), mascota.getRaza(),
                         mascota.getGenero(), mascota.getVacunas(),
                         mascota.getFoto(), mascota.getEspecie(),
                         mascota.getPeso_aprox())

                print param

                self.__cur.execute(query, param)
                self.__conn.commit()
                return True
            except Exception as e:
                print e.__class__
                print e.message
                return False