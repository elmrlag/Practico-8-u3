#Clases
from claseEmpleadoDePlanta import EmpleadoDePlanta
from claseEmpleadoExterno import EmpleadoExterno
from claseEmpleadoContratado import EmpleadoContratado
from claseEmpleado import Empleado
# Interfaces
from zope.interface import implementer
from interfazGerente import IGerente
from interfazTesorero import ITesorero
# Otras
from datetime import datetime
import numpy as np
import csv

@implementer(IGerente)
@implementer(ITesorero)

class Arreglo:
    __dimension = 0
    __actual = 0
    __empleados = None

    def __init__(self, dimension):
        self.__dimension = dimension
        self.__actual = 0
        self.__empleados = np.empty(dimension, dtype=Empleado)

        # Cargamos los empleados
        archivoContratados=open("contratados.csv")
        archivoExternos = open("externos.csv")
        archivoPlanta = open("planta.csv")
        # Creamos una lista de archivos
        listaArchivos= {archivoContratados, archivoExternos, archivoPlanta}
        # Iteramos los archivos
        for archivo in listaArchivos:
            reader = csv.reader(archivo, delimiter=",")
            # Iteramos las filas
            for fila in reader:
                unEmpleado = None
                dni = fila[0]
                nombre = fila[1]
                direccion = fila[2]
                telefono = fila[3]
                # Si el archivo es el de empleados contratados...
                if(archivo.name == "contratados.csv"):
                    fechaInicio = fila[4]
                    fechaFinalizacion = fila[5]
                    cantHorasTrabajadas = int(fila[6])
                    unEmpleado = EmpleadoContratado(dni, nombre, direccion, telefono, fechaInicio, fechaFinalizacion, cantHorasTrabajadas)
                # Si el archivo es el de empleados de planta...
                elif (archivo.name == "planta.csv"):
                    sueldoBasico = float(fila[4])
                    antiguedad = int(fila[5])
                    unEmpleado = EmpleadoDePlanta(dni, nombre, direccion, telefono, sueldoBasico, antiguedad)
                # Si el archivo es el de empleados externos...
                elif (archivo.name == "externos.csv"):
                    tarea = str(fila[4]).strip()
                    fechaInicio = fila[5]
                    fechaFinalizacion = fila[6]
                    montoViatico = float(fila[7])
                    costoObra = float(fila[8])
                    segDeVida = float(fila[9])
                    unEmpleado = EmpleadoExterno(dni, nombre, direccion, telefono, tarea, fechaInicio, fechaFinalizacion, montoViatico, costoObra, segDeVida)
                # Agregamos el empleado al arreglo
                self.__empleados[self.__actual] = unEmpleado
                self.__actual += 1
            # Cerramos el archivo
            archivo.close()

    def setHorasTrabajadas(self, dni, horas):
        i = 0
        band = False
        while band == False and i < len(self.__empleados):
            if int(self.__empleados[i].getDNI()) == dni:
                try:
                    self.__empleados[i].setHoras(horas)
                    print("Las horas han sido modificadas con exito!")
                except:
                    print("Este empleado no pertenece a la categoria de 'Empleado contratados'.")
                finally:
                    pass
                band = True
            else:
                i += 1
        if band == False : print(f"El numero de DNI '{dni}' no se encuentra registrado.")
    
    def montoPorTarea(self, tarea):
        acum = 0
        for empleado in self.__empleados:
            fecha = str(datetime.now()).split(" ")
            if empleado.getTipo() == "Externo" and fecha[0] < str(empleado.getFechaFinalizacion()).strip() and empleado.getTarea() == tarea:
                acum += empleado.getSueldo()
        return acum

    def listar(self):
        print("------------------------------------------------------------")
        for empleado in self.__empleados:
            if empleado.getSueldo() > 25000:
                print(f"NOMBRE: {empleado.getNombre()}, DIRECCION: {empleado.getDireccion()}, DNI: {empleado.getDNI()}")
                print("------------------------------------------------------------")

    def mostrar(self):
        print("------------------------------------------------------------")
        for empleado in self.__empleados:
            print(f"NOMBRE: {empleado.getNombre()}, TELEFONO: {empleado.getTelefono()}, SUELDO: {empleado.getSueldo()}")
            print("------------------------------------------------------------")
    
    def gastosSueldoPorEmpleado(self, dni):
        i = 0
        band = False
        while band == False and i < len(self.__empleados):
            if int(self.__empleados[i].getDNI()) == dni:
                print(f"A este empleado le corresponde el sueldo: {self.__empleados[i].getSueldo()}")
                band = True
            else:
                i += 1
        if band == False : print(f"El numero de DNI '{dni}' no se encuentra registrado.")

    def modificarBasicoEPlanta(self, dni, nuevoBasico):
        i = 0
        band = False
        while band == False and i < len(self.__empleados):
            if int(self.__empleados[i].getDNI()) == dni:
                if self.__empleados[i].getTipo() == 'De planta':
                    self.__empleados[i].setNuevoBasico = int(input("Ingrese el nuevo sueldo basico: "))
                else:
                    print("Este no es un empleado de planta.")
                band = True
            else:
                i += 1
        if band == False : print(f"El numero de DNI '{dni}' no se encuentra registrado.")

    def modificarViaticoEExterno(self, dni, nuevoViatico):
        i = 0
        band = False
        while band == False and i < len(self.__empleados):
            if int(self.__empleados[i].getDNI()) == dni:
                if self.__empleados[i].getTipo() == 'Externo':
                    self.__empleados[i].setNuevoViatico = int(input("Ingrese el nuevo monto viatico: "))
                else:
                    print("Este no es un empleado externo.")
                band = True
            else:
                i += 1
        if band == False : print(f"El numero de DNI '{dni}' no se encuentra registrado.")

    def modificarValorEPorHora(self, dni, nuevoValorHora):
        i = 0
        band = False
        while band == False and i < len(self.__empleados):
            if int(self.__empleados[i].getDNI()) == dni:
                if self.__empleados[i].getTipo() == 'Contratado':
                    self.__empleados[i].setValorHoras = int(input("Ingrese el nuevo valor por hora: "))
                else:
                    print("Este no es un empleado contratado.")
                band = True
            else:
                i += 1
        if band == False : print(f"El numero de DNI '{dni}' no se encuentra registrado.")

    def actualizarArchivos(self):
        print("Despues lo hago")