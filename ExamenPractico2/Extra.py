def ContarPalabras(palabra, nomarchivo):
    with open(nomarchivo, "r") as x:
        texto = x.read()
        palabras = texto.split()
        contador = 0
        posiciones = []
        for i in range(len(palabras)):
            y = palabras[i]
            if y.lower() == palabra.lower():
                contador += 1
                posiciones.append(i)
        return contador, posiciones


resultado = ()
Palabra2 = input("Favor de ingresar la palabra que desea buscar: ")
resultado = ContarPalabras(Palabra2, "ExamenPractico2/Palabras.txt")
contador, posiciones = resultado
print(f"La palabra se repite {contador} veces.")
print(f"Las posiciones son: {posiciones}")
