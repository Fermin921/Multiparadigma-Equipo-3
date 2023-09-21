def escribir_cadenas():
    cadenas=[]
    while True:
        cadena = input("Escribe un texto (si deseas terminar escribe exit): ")
        if cadena.lower()=='exit':
            break
        cadenas.append(cadena)
    return cadenas

def extraerPalabrasyNums(cadenas):
    palabras=[]
    numeros=[]
    for cadena in cadenas:
        palabras.extend([palabra for palabra in cadena.split() if not palabra.isdigit()])
        numeros.extend([palabra for palabra in cadena.split() if palabra.isdigit()])

    palabras.sort(key=str.lower) 
    ordenado=' '.join(palabras+numeros)
    return ordenado

cadenas=escribir_cadenas()
 
if len(cadenas)>0:# se verifica si no esta vacio
    resultado=extraerPalabrasyNums(cadenas)
    print("Palabras en orden alfabetico y numeros al final: ")
    print(resultado)
else:
    print("dejaste vacio el campo")