import psycopg2
# from logger_base import log

conexion = psycopg2.connect(user="postgres",password="Jerry2001",host="127.0.0.1",port="5432",database="POSTGRES")

try:
    with conexion:
        with conexion.cursor() as cursos:
            sentencia = "INSERT INTO Personaje (idPersonaje,Nombre) VALUES (%s,%s)"
            valores = (
                ("1","Fermin"),
                ("2","Juan"),
                ("3","Gerardo")
            )
            cursos.executemany(sentencia,valores)
            registrosInsertados = cursos.rowcount
            # log.debug("Registros Insertados: {registrosInsertados}")
except Exception as e:
    # log.error(e) 
    pass
finally:
    conexion.close()