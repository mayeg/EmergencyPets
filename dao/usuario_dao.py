# -*- coding: utf-8 -*-
from dto.usuario import Usuario

class UsuarioDao:
    def __init__(self):
        from integrador import mysql
        self.__conn = mysql.connect()
        self.__cur = self.__conn.cursor()

    def get_user_login(self, usuario):
        try:
            query = "SELECT * FROM usuario WHERE email=%s AND contrasena=%s"
            param = (usuario.getEmail(), usuario.getContrasena())
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return Usuario(id=data[0], email=data[5], contrasena=data[10])
        except Exception as e:
            print e.message, e.__class__
            return None

    def get_total_usuarios(self, pagina, codigo, nombres, cedula, apellidos):
        try:
            query = "SELes AND cedula LIKE %s AND apellidos LIKE %s"
            param = ("%" + codigo + "%", "%" + nombres + "%", "%" + cedula + "%"
                     , "%" + apellidos + "%")
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            print data[0]
            if data is None:
                return 0
            return data[0]
        except Exception as e:
            print e.message
            return 0

    def get_usuario_por_email(self, usuario):
        try:
            query = "SELECT * FROM usuario WHERE email = %s"
            param = (usuario.getEmail(),)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return Usuario(id=data[0], cedula=data[1], nombre=data[2],
                           apellido=data[3], genero=data[4], email=data[5],
                           barrio=data[6], direccion=data[7],
                           fecha_nacimiento=data[8], telefono=data[9],
                           contrasena=data[10])
        except Exception as e:
            print e.message
            return None

    def crear_usuario(self, usuario):
        print "llego al dao"
        try:
            query = "INSERT INTO usuario (cedula, nombre, apellido, " \
                    "genero, email, barrio, direccion, fecha_nacimiento," \
                    "telefono, contrasena) VALUES (%s, %s, %s, %s, %s" \
                    ", %s, %s, %s, %s, %s)"

            param = (usuario.getCedula(), usuario.getNombre(),
                     usuario.getApellido(), usuario.getGenero(),
                     usuario.getEmail(), usuario.getBarrio(),
                     usuario.getDireccion(), usuario.getFecha_nacimiento(),
                     usuario.getTelefono(), usuario.getContrasena())
            self.__cur.execute(query, param)
            self.__conn.commit()
            return True
        except Exception as e:
            print e.__class__
            print e.message
            return False

    def get_usuario_id(self, id):
        try:
            query = "SELECT * FROM usuario WHERE id = %s"
            param = (id,)
            self.__cur.execute(query, param)
            data = self.__cur.fetchone()
            if data is None:
                return None
            return Usuario(id=data[0], cedula=data[1], nombre=data[2],
                           apellido=data[3], genero=data[4], email=data[5],
                           barrio=data[6], direccion=data[7],
                           fecha_nacimiento=data[8], telefono=data[9],
                           contrasena=data[10])
        except Exception as e:
            print e.message
            return None
