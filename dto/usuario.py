# -*- coding: utf-8 -*-

class Usuario:

    def __init__(self, id=0,  cedula="", nombre="", apellido="", genero="",
                 email="", barrio="", direccion="", fecha_nacimiento="",
                 telefono="", contrasena="", token_password=""):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__genero = genero
        self.__email = email
        self.__barrio = barrio
        self.__direccion = direccion
        self.__fecha_nacimiento = fecha_nacimiento
        self.__telefono = telefono
        self.__contrasena = contrasena
        self.__token_password = token_password

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getCedula(self):
        return self.__cedula

    def setCedula(self, cedula):
        self.__cedula = cedula

    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getBarrio(self):
        return self.__barrio

    def setBarrio(self, barrio):
        self.__barrio = barrio

    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def getFecha_nacimiento(self):
        return self.__fecha_nacimiento

    def setFecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def getTelefono(self):
        return self.__telefono

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def getContrasena(self):
        return self.__contrasena

    def setContrasena(self, contrasena):
        self.__contrasena = contrasena

    def getTokenPassword(self):
        return self.__token_password

    def setTokenPassword(self, token):
        self.__token_password = token

    def __unicode__(self):
        return "email: {}, contrasena:{}".format(
            self.__email, self.__contrasena)

    def get_dict(self):
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'email': self.__email
        }