# DAO = DATA ACCESS OUT
from Persona import Personaje
from Conexion2 import *
from CursorPoll import *
from logger_base import *

class PersonajeDAO:
    _SELECCIONAR = 'SELECT * FROM public."Personaje" ORDER BY "idPersonaje"'
    _SELECCIONAR_ID = 'SELECT "Personaje"."idPersonaje", "Personaje"."Nombre", "Personaje"."Poder" FROM "Personaje" WHERE "Personaje"."idPersonaje" = %s'
    _INSERTAR = 'INSERT INTO "Personaje" ("idPersonaje", "Nombre", "Poder") VALUES (%s,%s, %s)'
    _ACTUALIZAR = 'UPDATE "Personaje" SET "Nombre" = %s, "Poder" = %s WHERE "idPersonaje" = %s'
    _BORRAR = 'DELETE FROM "Personaje" where "idPersonaje" = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personajes = []
            for r in registros:
                personajes.append(Personaje(r[0], r[1], r[2]))
            return personajes

    @classmethod
    def seleccionar_por_id(cls, idPersonaje):
        with CursorDelPool() as cursor:
            valores = (idPersonaje,)
            cursor.execute(cls._SELECCIONAR_ID, valores)
            resultado = cursor.fetchall()  # Obtener el resultado de la consulta
            return resultado
        
    @classmethod
    def insertar(cls, personaje):
        with CursorDelPool() as cursor:
            valores = (personaje._idPersonaje, personaje._Nombre, personaje._Poder)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, personaje):
        with CursorDelPool() as cursor:
            valores = (personaje._Nombre, personaje._Poder, personaje._idPersonaje)
            cursor.execute(cls._ACTUALIZAR, valores)
            return personaje

    @classmethod
    def eliminar(cls, personaje):
        with CursorDelPool() as cursor:
            valores = personaje._idPersonaje
            cursor.execute(cls._BORRAR, valores)
            return cursor.rowcount

    # end def

#SELECCIONAR
# if __name__ == "__main__":
#      personaje2 = PersonajeDAO.seleccionar()
#      for p in personaje2:
#         log.debug(p)

#INSERTAR
# if __name__ == "__main__":       
#     personaje1= Personaje(idPersonaje=4,Nombre='Mario', Poder=85)
#     personajes =PersonajeDAO.insertar(personaje1)
#     log.debug(f"{personaje1._Nombre} ingresado correctamente, personajes insertados: {personajes}")

#SELECCIONAR POR ID
# if __name__ == "__main__":
#     id = "3"
#     log.debug(f"{PersonajeDAO.seleccionar_por_id(id)}")

#ACTUALIZAR
# if __name__ == "__main__":
#     personajeA = Personaje(Nombre='Luigi', Poder=99, idPersonaje=4)
#     personaje_actualizado = PersonajeDAO.actualizar(personajeA)
#     log.debug(f"{personajeA._Nombre} Actualizado Correctamente")

#ELIMINAR
if __name__ == "__main__":
    personajeB= Personaje(idPersonaje="4", Nombre='', Poder='')
    personajeEliminado= PersonajeDAO.eliminar(personajeB)
    log.debug(f"{personajeB._Nombre} Eliminado Correctamente")