from claseEmpleado import Empleado

class EmpleadoExterno(Empleado):
    __tarea = None
    __fechaInicio = None
    __fechaFinalizacion = None
    __montoViatico = None
    __costoObra = None
    __montoSeguroDeVida = None

    def __init__(self, dni, nombre, direccion, telefono, tarea, fechaInicio, fechaFinalizacion, montoViatico, costoObra, montoSeguroDeVida):
        Empleado.__init__(self, dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fechaInicio = fechaInicio
        self.__fechaFinalizacion = fechaFinalizacion
        self.__montoViatico = montoViatico
        self.__costoObra = costoObra
        self.__montoSeguroDeVida = montoSeguroDeVida

    def getSueldo(self):
        return self.__costoObra - self.__montoViatico - self.__montoSeguroDeVida

    def getTarea(self):
        return self.__tarea
    
    def getFechaFinalizacion(self):
        return self.__fechaFinalizacion
    
    def getTipo(self):
        return "Externo"

    def getFechaFinalizacion(self):
        return self.__fechaFinalizacion
    
    def setViatico(self, nuevoViatico):
        self.__montoViatico = nuevoViatico