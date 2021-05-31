from claseEmpleado import Empleado

class EmpleadoDePlanta(Empleado):
    __sueldoBasico = None
    __antiguedad = None

    def __init__(self, dni, nombre, direccion, telefono, sueldoBasico, antiguedad):
        Empleado.__init__(self, dni, nombre, direccion, telefono)
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad

    def getSueldo(self):
        return self.__sueldoBasico + self.__sueldoBasico / 100 * self.__antiguedad

    def getTipo(self):
        return "De planta"
    
    def setNuevoBasico(self, nuevoBasico):
        self.__sueldoBasico = nuevoBasico