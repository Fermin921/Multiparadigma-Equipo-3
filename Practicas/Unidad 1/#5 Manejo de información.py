# Escribir una función que reciba n parámetros de llave valor e imprima la información en formato
# “{valor}”: “{llave}”

def funcion(**kwargs):
   for key, parametro in kwargs.items():
        print(f'"{parametro}": "{key}"')
    
funcion(llave1="Juan",llave2=523,llave3='b',llave4=2.53)