class Empleado(object):
    __dni = None
    __nombre = None
    __direccion = None
    __telefono = None
    
    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    
    def getDNI(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono