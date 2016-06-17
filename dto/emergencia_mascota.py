from dto.emergencia import Emergencia
from dto.mascota import Mascota
from dto.usuario import Usuario


class Emergencia_Mascota:

    def __init__(self, id=0, id_usuario=0, id_emergencia=0, fecha=""):

        self.__id = id
        self.__id_usuario = Usuario(id=id_usuario)
        self.__id_emergencia = Emergencia(id=id_emergencia)
        self.__fecha = fecha

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getId_usuario(self):
        return self.__id_usuario

    def setId_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def getId_emergencia(self):
        return self.__id_emergencia

    def setId_emergencia(self, id_emergencia):
        self.__id_emergencia = id_emergencia

    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha):
        self.__fecha = fecha
