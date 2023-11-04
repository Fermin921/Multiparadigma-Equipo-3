import psycopg2

# Codigo para realizar altas a la base de datos
conexion = psycopg2.connect(
    user="postgres",
    password="Jerry2001",
    host="127.0.0.1",
    port="5432",
    database="POSTGRES1",
)
from logger_base import log

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = "INSERT INTO Personaje(nombre) VALUES (%s)"
    valores = ("Juan",)
    cursor.execute(sentencia, valores)
    conexion.commit()
    log.debug(f"{valores} insertado correctamente")
except Exception as e:
    conexion.rollback()
    log.error(e)
