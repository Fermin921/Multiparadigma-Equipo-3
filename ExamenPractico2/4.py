def capturarCadenas():
    cadenas = []
    while True:
        cadena = input("Ingrese una cadena de texto (o escriba 'exit' para terminar de ingresar): ")
        if cadena.lower() == 'exit':
            break
        cadenas.append(cadena)

    return cadenas

def ordenarCadenas(cadenas):
    palabras = []
    numeros = []
    for cadena in cadenas:
        palabras.extend(cadena.split())
    
    for palabra in palabras:
        if palabra.isdigit():
            numeros.append(palabra)
            palabras.remove(palabra)
    
    palabras.sort()
    palabras.extend(numeros)
    return palabras

def imprimirPalabrasOrdenadas(palabras):
    for palabra in palabras:
        print(palabra, end=' ')

if __name__ == "__main__":
    print("Ingrese cadenas de texto (escriba 'exit' para terminar de ingresar).")
    cadenas = capturarCadenas()
    palabras_ordenadas = ordenarCadenas(cadenas)
    
    print("\nPalabras en orden alfabético con números al final:")
    imprimirPalabrasOrdenadas(palabras_ordenadas)
