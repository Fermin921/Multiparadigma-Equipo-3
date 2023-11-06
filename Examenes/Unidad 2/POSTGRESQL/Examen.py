#Id, Raza, FechaDeIngreso, FechaDeSalida
from logger_base import log

class Animal():
    def __init__(self, Id, Raza, FechaDeIngreso, FechaDeSalida)-> None:
        self._Id=Id
        self._Raza= Raza
        self._FechaDeIngreso= FechaDeIngreso
        self._FechaDeSalida = FechaDeSalida
    def __str__(self)-> str:
        return f"IdAnimal: {self._Id}\nRaza: {self._Raza}\nFecha de Ingreso: {self._FechaDeIngreso}\nFecha de Salida: {self._FechaDeSalida}"
    
class Doctor():
    def __init__(self, Id, Nombre, NumeroDeTelefono)-> None:
        self._Id= Id
        self._Nombre= Nombre
        self._NumeroTel= NumeroDeTelefono
    def __str__(self)-> str:
        return f"IdDoctor: {self._Id}\nNombre: {self._Nombre}\nNumero de Telefono: {self._NumeroTel}"
    
class Consulta():
    def __init__(self, Id, IdDoctor, Servicio, Costo)->None:
        self._Id= Id
        self._IdDoctor = IdDoctor
        self._Servicio = Servicio
        self._Costo= Costo
    def __str__(self)-> str:
        return f"IdConsulta: {self._Id}\nIdDoctor: {self._IdDoctor}\nServicio: {self._Servicio}\nCosto: {self._Costo}"
    

