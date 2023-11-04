from Persona import Artista
from Conexion2 import Conexion
from CursorPoll import CursorDelPool
from logger_base import log

class ArtistaDAO:
    _SELECCIONAR = 'SELECT * FROM public."Artista" ORDER BY "IdArtista"'
    _SELECCIONAR_ID = 'SELECT "Artista"."IdArtista", "Artista"."NombreArtista", "Artista"."Genero" FROM "Artista" WHERE "Artista"."IdArtista" = %s'
    _INSERTAR = 'INSERT INTO "Artista" ("IdArtista","NombreArtista", "Genero") VALUES (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE "Artista" set "NombreArtista" = %s, "Genero" = %s where "IdArtista" = %s'
    _BORRAR = 'DELETE FROM "Artista" where "IdArtista" = %s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            artistas = []
            for r in registros:
                artistas.append(Artista(r[0], r[1], r[2]))
            return artistas

    @classmethod
    def seleccionar_por_id(cls, idArtista):
        with CursorDelPool() as cursor:
            valores = (idArtista,)
            cursor.execute(cls._SELECCIONAR_ID, valores)
            resultado = cursor.fetchall()  # Obtener el resultado de la consulta
            return resultado

    @classmethod
    def insertar(cls,artista):
        with CursorDelPool() as cursor:
            valores = (artista._idArtista, artista._nombreartista, artista._genero)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, artista):
        with CursorDelPool() as cursor:
            valores = (artista._nombreartista, artista._genero, artista._idArtista)
            cursor.execute(cls._ACTUALIZAR, valores)
            return artista

    @classmethod
    def eliminar(cls, artista):
        with CursorDelPool() as cursor:
            valores = artista._idArtista
            cursor.execute(cls._BORRAR, valores)
            return cursor.rowcount


        

#SELECCIONAR
# if __name__ == "__main__":
#     artista2 = ArtistaDAO.seleccionar()
#     for a in artista2:
#         log.debug(a)

#SELECCIONAR POR ID
# if __name__ == "__main__":
#     id = "2"
#     log.debug(f"{ArtistaDAO.seleccionar_por_id(id)}")

#INSERTAR
# if __name__ == "__main__":       
#     artista1= Artista(IdArtista=5,NombreArtista='Luis Miguel', Genero='Pop Latino')
#     artistas =ArtistaDAO.insertar(artista1)
#     log.debug(f"{artista1._nombreartista} ingresado correctamente, artista insertado: {artistas}")

#ACTUALIZAR
# if __name__ == "__main__":
#     artistaA = Artista(NombreArtista='50 cent', Genero='Rap y Hip Hop', IdArtista=2)
#     artista_actualizado = ArtistaDAO.actualizar(artistaA)
#     log.debug(f"{artistaA._nombreartista} Actualizado Correctamente")
    
#ELIMINAR
if __name__ == "__main__":
    artistaB= Artista(IdArtista="4", NombreArtista='', Genero='')
    artistaEliminado= ArtistaDAO.eliminar(artistaB)
    log.debug(f"Artista Eliminado")