from Persona import Alumno
from Conexion2 import Conexion
from CursorPoll import CursorDelPool
from logger_base import log

class AlumnoDAO:
    _SELECCIONAR = 'SELECT * FROM "Alumno" ORDER BY "IdAlumno"'
    _SELECCIONAR_ID = 'SELECT "Alumno"."IdAlumno", "Alumno"."Nombre", "Alumno"."ApellidoPaterno", "Alumno"."ApellidoMaterno" FROM "Alumno" WHERE "Alumno"."IdAlumno" = %s'
    _INSERTAR = 'INSERT INTO "Alumno" ("IdAlumno","Nombre","ApellidoPaterno", "ApellidoMaterno") VALUES (%s,%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE "Alumno" set "Nombre" = %s, "ApellidoPaterno" = %s, "ApellidoMaterno" = %s where "IdAlumno" = %s'
    _BORRAR = 'DELETE FROM "Alumno" where "IdAlumno" = %s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            alumnos = []
            for r in registros:
                alumnos.append(Alumno(r[0], r[1], r[2], r[3]))
            return alumnos

    @classmethod
    def seleccionar_por_id(cls, idAlumno):
        with CursorDelPool() as cursor:
            valores = (idAlumno,)
            cursor.execute(cls._SELECCIONAR_ID, valores)
            resultado = cursor.fetchall()  # Obtener el resultado de la consulta
            return resultado

    @classmethod
    def insertar(cls,alumno):
        with CursorDelPool() as cursor:
            valores = (alumno._idAlumno, alumno._nombre, alumno._apellidopaterno, alumno._apellidomaterno)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls,alumno):
        with CursorDelPool() as cursor:
            valores = (alumno._nombre,alumno._apellidopaterno,alumno._apellidomaterno, alumno._idAlumno)
            cursor.execute(cls._ACTUALIZAR, valores)
            return alumno

    @classmethod
    def eliminar(cls, alumno):
        with CursorDelPool() as cursor:
            valores = alumno._idAlumno
            cursor.execute(cls._BORRAR, valores)
            return cursor.rowcount
#SELECCIONAR
# if __name__ == "__main__":
#     alumno2 = AlumnoDAO.seleccionar()
#     for p in alumno2:
#         log.debug(p)
        
#INSERTAR
# if __name__ == "__main__":       
#     alumnoN= Alumno(IdAlumno=4,Nombre='Luis',ApellidoPaterno='Castillo',ApellidoMaterno='Detal')
#     alumnos =AlumnoDAO.insertar(alumnoN)
#     log.debug(f"Ingresado correctamente, alumno insertado: {alumnos}")

#SELECCIONAR POR ID
# if __name__ == "__main__":
#     id = "2"
#     log.debug(f"{AlumnoDAO.seleccionar_por_id(id)}")

# #ACTUALIZAR 
# if __name__ == "__main__":
#     alumnoA = Alumno(Nombre='Gerardo Alberto', ApellidoPaterno='Cruz',ApellidoMaterno='Rojo', IdAlumno=1)
#     alumno_actualizado = AlumnoDAO.actualizar(alumnoA)
#     log.debug(f"Alumno Actualizado Correctamente")
    
#ELIMINAR
if __name__ == "__main__":
    alumnoB= Alumno(IdAlumno="3", Nombre='', ApellidoPaterno='', ApellidoMaterno='')
    alumnoEliminado= AlumnoDAO.eliminar(alumnoB)
    log.debug(f"Alumno Eliminado")