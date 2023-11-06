from Examen import Consulta
from Conexion import Conexion
from CursorPool import CursorDelPool
from logger_base import log

class ConsultaDAO:
    _SELECCIONAR= 'SELECT * FROM public."Consulta" ORDER BY "Id"'
    _INSERTAR= 'INSERT INTO "Consulta" ("Id","IdDoctor", "Servicio", "Costo") VALUES (%s,%s,%s,%s)'
    _ACTUALIZAR= 'UPDATE "Consulta" set "IdDoctor" = %s, "Servicio" = %s, "Costo"=%s where "Id" = %s'
    _BORRAR = 'DELETE FROM "Consulta" where "Id" = %s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            consultas = []
            for r in registros:
                consultas.append(Consulta(r[0], r[1], r[2], r[3]))
            return consultas

    @classmethod
    def seleccionar_por_id(cls, id):
        with CursorDelPool() as cursor:
            valores = (id,)
            cursor.execute(cls._SELECCIONAR_ID, valores)
            resultado = cursor.fetchall()  # Obtener el resultado de la consulta
            return resultado

    @classmethod
    def insertar(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta._Id, consulta._IdDoctor, consulta._Servicio, consulta._Costo)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, consulta):
        with CursorDelPool() as cursor:
            valores = (consulta._IdDoctor, consulta._Servicio, consulta._Costo, consulta._Id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return consulta

    @classmethod
    def eliminar(cls, consulta):
        with CursorDelPool() as cursor:
            valores = consulta._Id
            cursor.execute(cls._BORRAR, valores)
            return cursor.rowcount
        
        
#SELECCIONAR
# if __name__ == "__main__":
#     consulta = ConsultaDAO.seleccionar()
#     for a in consulta:
#         log.debug(a)

#INSERTAR
# if __name__ == "__main__":       
#     consultaN = Consulta(Id="1",IdDoctor="1", Servicio='Chequeo', Costo= 200 )
#     consultas =ConsultaDAO.insertar(consultaN)
#     log.debug(f"ingresado correctamente, consulta insertada: {consultas}",consultaN._Servicio, consultas)

#ACTUALIZAR
# if __name__ == "__main__":
#     consultaA = Consulta(IdDoctor=1, Servicio='Inyeccion', Costo=400, Id=1)
#     consulta_actualizada = ConsultaDAO.actualizar(consultaA)
#     log.debug(f"{consultaA._Servicio} Actualizado Correctamente")

#ELIMINAR
if __name__ == "__main__":
    consultaB= Consulta(Id="1", IdDoctor="", Servicio='',Costo='')
    consultaEliminado= ConsultaDAO.eliminar(consultaB)
    log.debug(f"Consulta Eliminada")