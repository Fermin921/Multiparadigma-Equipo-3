from Examen import Doctor
from Conexion import Conexion
from CursorPool import CursorDelPool
from logger_base import log

class DoctorDAO:
    _SELECCIONAR= 'SELECT * FROM public."Doctor" ORDER BY "Id"'
    _INSERTAR= 'INSERT INTO "Doctor" ("Id","Nombre", "NumeroDeTelefono") VALUES (%s,%s,%s)'
    _ACTUALIZAR= 'UPDATE "Doctor" set "Nombre" = %s, "NumeroDeTelefono" = %s where "Id" = %s'
    _BORRAR = 'DELETE FROM "Doctor" where "Id" = %s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            doctores = []
            for r in registros:
                doctores.append(Doctor(r[0], r[1], r[2]))
            return doctores

    @classmethod
    def seleccionar_por_id(cls, id):
        with CursorDelPool() as cursor:
            valores = (id,)
            cursor.execute(cls._SELECCIONAR_ID, valores)
            resultado = cursor.fetchall()  # Obtener el resultado de la consulta
            return resultado

    @classmethod
    def insertar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor._Id, doctor._Nombre, doctor._NumeroTel)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, doctor):
        with CursorDelPool() as cursor:
            valores = (doctor._Nombre, doctor._NumeroTel, doctor._Id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return doctor

    @classmethod
    def eliminar(cls, doctor):
        with CursorDelPool() as cursor:
            valores = doctor._Id
            cursor.execute(cls._BORRAR, valores)
            return cursor.rowcount
        
#SELECCIONAR
# if __name__ == "__main__":
#     doctor = DoctorDAO.seleccionar()
#     for a in doctor:
#         log.debug(a)

#INSERTAR
# if __name__ == "__main__":       
#     DoctorN = Doctor(Id="2",Nombre="Gerardo Cruz", NumeroDeTelefono=1045889)
#     doctores =DoctorDAO.insertar(DoctorN)
#     log.debug(f"ingresado correctamente, doctor insertado: {doctores}",DoctorN._Nombre, doctores)

#ACTUALIZAR
# if __name__ == "__main__":
#     doctorA = Doctor(Nombre='Josue Reyes', NumeroDeTelefono=4568752,Id=1 )
#     doctor_actualizado = DoctorDAO.actualizar(doctorA)
#     log.debug(f"{doctorA._Nombre} Actualizado Correctamente")

#ELIMINAR
if __name__ == "__main__":
    doctorB= Doctor(Id="2", Nombre='', NumeroDeTelefono='')
    doctorEliminado= DoctorDAO.eliminar(doctorB)
    log.debug(f"Doctor Eliminado")
