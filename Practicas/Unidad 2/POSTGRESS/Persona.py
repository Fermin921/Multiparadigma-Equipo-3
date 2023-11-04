from logger_base import log

class Personaje():
    def __init__(self, idPersonaje, Nombre, Poder)-> None:
        self._idPersonaje =idPersonaje
        self._Nombre = Nombre
        self._Poder = Poder
        
    def __str__(self) ->str:
        return f"idPersonaje: {self._idPersonaje}\nNombre: {self._Nombre}\nPoder: {self._Poder}"
    
class Artista():
    def __init__(self, IdArtista, NombreArtista, Genero)-> None:
        self._idArtista = IdArtista
        self._nombreartista= NombreArtista
        self._genero = Genero
        
    def __str__(self) ->str:
        return f"idArtista: {self._idArtista}\nNombre Artistico: {self._nombreartista}\nGenero: {self._genero}"
    
class Alumno():
    def __init__(self, IdAlumno, Nombre, ApellidoPaterno, ApellidoMaterno)->None:
        self._idAlumno = IdAlumno
        self._nombre= Nombre
        self._apellidopaterno = ApellidoPaterno
        self._apellidomaterno = ApellidoMaterno
        
    def __str__(self)->str:
        return f"idAlumno: {self._idAlumno}\nNombre: {self._nombre}\nApellido P: {self._apellidopaterno}\n:Apellido M: {self._apellidomaterno}"
    
    
    
    
    
    
    
# # Clase o bien formato de la tabla de la base de datos
# class Cliente:
#     def __init__(self, id=None, nombre=None) -> None:
#         self.id = id
#         self.nombre = nombre

#     def __str__(self) -> str:
#         return f"""
#         ID Cliente: {self.id}, Nombre: {self.nombre}
#         """

#     @property
#     def idCliente(self):
#         return self.id

#     @idCliente.setter
#     def idCliente(self, id):
#         self.id = id

#     @property
#     def Nombre(self):
#         return self.nombre

#     @Nombre.setter
#     def Nombre(self, nombre):
#         self.nombre = nombre


# if __name__ == "__main__":
#     persona1 = Cliente(1, "Juan")
#     log.debug(persona1)

