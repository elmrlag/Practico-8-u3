from claseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    __fechaInicio = None
    __fechaFinalizacion = None
    __cantHorasTrabajadas = None
    __valorPorHora = None
    
    def __init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFinalizacion, cantHorasTrabajadas):
        Empleado.__init__(self, dni, nombre, direccion, telefono)
        self.__fechaInicio = fechaInicio
        self.__fechaFinalizacion = fechaFinalizacion
        self.__cantHorasTrabajadas = cantHorasTrabajadas
        self.__valorPorHora = 150 # Es el mismo para todos los empleados contratados
    
    def getSueldo(self):
        return self.__cantHorasTrabajadas * self.__valorPorHora

    def getTipo(self):
        return "Contratado"
    
    def setHoras(self, horas):
        self.__cantHorasTrabajadas += horas
    
    def setValorHoras(self, nuevoValor):
        self.__valorPorHora = nuevoValor