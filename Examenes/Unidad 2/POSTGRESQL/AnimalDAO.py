from Examen import Animal
from Conexion import Conexion
from CursorPool import CursorDelPool
from logger_base import log

class AnimalDAO:
    _SELECCIONAR= 'SELECT * FROM public."Animal" ORDER BY "Id"'
    _INSERTAR= 'INSERT INTO "Animal" ("Id","Raza", "FechaDeIngreso", "FechaDeSalida") VALUES (%s,%s,%s,%s)'
    _ACTUALIZAR= 'UPDATE "Animal" set "Raza" = %s, "FechaDeIngreso" = %s, "FechaDeSalida" = %s where "Id" = %s'
    _BORRAR = 'DELETE FROM "Animal" where "Id" = %s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            animales = []
            for r in registros:
                animales.append(Animal(r[0], r[1], r[2], r[3]))
            return animales

    @classmethod
    def seleccionar_por_id(cls, id):
        with CursorDelPool() as cursor:
            valores = (id,)
            cursor.execute(cls._SELECCIONAR_ID, valores)
            resultado = cursor.fetchall()  # Obtener el resultado de la consulta
            return resultado

    @classmethod
    def insertar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal._Id, animal._Raza, animal._FechaDeIngreso, animal._FechaDeSalida)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, animal):
        with CursorDelPool() as cursor:
            valores = (animal._Raza, animal._FechaDeIngreso, animal._FechaDeSalida, animal._Id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return animal

    @classmethod
    def eliminar(cls, animal):
        with CursorDelPool() as cursor:
            valores = animal._Id
            cursor.execute(cls._BORRAR, valores)
            return cursor.rowcount
        
#SELECCIONAR
# if __name__ == "__main__":
#     animal = AnimalDAO.seleccionar()
#     for a in animal:
#         log.debug(a)

#INSERTAR
# if __name__ == "__main__":       
#     animalN = Animal(Id="2",Raza='Perro', FechaDeIngreso='2023-11-01', FechaDeSalida='2023-11-06')
#     animales =AnimalDAO.insertar(animalN)
#     log.debug(f"ingresado correctamente, artista insertado: {animales}",animalN._Raza, animales)

#ACTUALIZAR
# if __name__ == "__main__":
#     animal1 = Animal(Raza='Gato', FechaDeIngreso='2023-10-31', FechaDeSalida='2023-11-03', Id=1)
#     animal_actualizado = AnimalDAO.actualizar(animal1)
#     log.debug(f"{animal1._Raza} Actualizado Correctamente")

#ELIMINAR
if __name__ == "__main__":
    animalB= Animal(Id="2", Raza='', FechaDeIngreso='',FechaDeSalida='')
    animalEliminado= AnimalDAO.eliminar(animalB)
    log.debug(f"Animal Eliminado")
