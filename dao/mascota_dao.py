# -*- coding: utf-8 -*-
from dto.mascota import Mascota
from dto.usuario import Usuario


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
                self.__cur.execute(query, param)
                self.__conn.commit()
                return True
            except Exception as e:
                print e.__class__
                print e.message
                return False

    def listar_mascotas(self, usuario):
        try:
            query = "SELECT * FROM mascota WHERE dueno=%s"
            param = (int(usuario.getId()),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchall()
            resultado = list()
            if data is None:
                return []
            for mascota in data:
                masco = Mascota(id=mascota[0], dueno=mascota[1], nombre=mascota[2],
                                fecha_nacimiento=mascota[3], raza=mascota[4],
                                genero=mascota[5], especie=mascota[8],
                                peso_aprox=mascota[9])
                resultado.append(masco)
            return resultado

        except Exception as e:
            print e.message, e.__class__
            return []

    def get_mascota_dueno(self, usuario):
        try:
            query = "SELECT * FROM mascota  WHERE dueno =%s"
            param = (int(usuario.getId()),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            print data, "dao"
            if data is None:
                return None
            mascota = Mascota(dueno=data[1], nombre=data[2],
                              fecha_nacimiento=data[3], raza=data[4],
                              genero=data[5], vacunas=data[6], foto=data[7],
                              especie=data[8], peso_aprox=data[9])
            return mascota
        except Exception as e:
            print e.__class__
            print e.message
            return None

    def get_mascota(self, mascota):
        try:
            query = "SELECT * FROM mascota  WHERE id =%s"
            param = (mascota.getId(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            mascota = Mascota(dueno=data[1], nombre=data[2],
                              fecha_nacimiento=data[3], raza=data[4],
                              genero=data[5], vacunas=data[6], foto=data[7],
                              especie=data[8], peso_aprox=data[9])
            return mascota
        except Exception as e:
            print e.__class__
            print e.message
            return None


    def editar_mascota(self, mascota):
        try:
            query = "UPDATE mascota SET nombre=%S, dueno=%s, fecha_nacimiento=%s," \
                    "raza=%s, genero=%s, vacunas=%s, foto=%s, especie=%s, " \
                    "peso_aprox=%s " \
                    " WHERE id=%s "

            param = (mascota.getNombre(), mascota.getDueno().getId(),
                     str(mascota.getFecha_nacimiento()), mascota.getRaza(),
                     mascota.getGenero(), mascota.getVacunas(),
                     mascota.getFoto(), mascota.getEspecie(),
                     mascota.getPeso_aprox(), mascota.getId())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False
