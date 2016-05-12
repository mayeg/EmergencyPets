from dto.usuario import Usuario


class Mascota:

    def __init__(self, id=0, dueno=0, nombre="", fecha_nacimiento="",
                 raza="", genero="", vacunas="", foto="", especie="",
                 peso_aprox=0):

        self.__id = id
        self.__dueno = Usuario(id=dueno)
        self.__nombre = nombre
        self.__fecha_nacimiento = fecha_nacimiento
        self.__raza = raza
        self.__genero = genero
        self.__vacunas = vacunas
        self.__foto = foto
        self.__especie = especie
        self.__peso_aprox = peso_aprox


    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDueno(self):
        return self.__dueno

    def setDueno(self, dueno):
        self.__dueno = dueno

    def getRaza(self):
        return self.__raza

    def setRaza(self, raza):
        self.__raza = raza

    def getVacunas(self):
        return self.__vacunas

    def setVacunas(self, vacunas):
        self.__vacunas = vacunas

    def getFoto(self):
        return self.__foto

    def setFoto(self, foto):
        self.__foto = foto

    def getEspecie(self):
        return self.__especie

    def setEspecie(self, especie):
        self.__especie = especie

    def getPeso_aprox(self):
        return self.__peso_aprox

    def setPeso_aprox(self, peso_aprox):
        self.__peso_aprox = peso_aprox

    def getFecha_nacimiento(self):
        return self.__fecha_nacimiento

    def setFecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero
