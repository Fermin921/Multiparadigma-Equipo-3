
#Obtener entradas
def obtenerNumero3Digitos():
    while True:
        try:
            numero = int(input("Ingresa un numero de 3 digitos: "))
            if 100 <= numero <= 999:
                return numero
            else:
                print("Ingresa un numero de 3 digitos valido.")
        except ValueError:
            print("Ingresa un número valido.")

# Revertir entradas
def RevertirNumero (numero):
    #A texto
    numeroStr = str(numero)
    # slicing
    numeroAlrevesC = numeroStr[::-1]
    #A entero
    numeroAlrevesE = int(numeroAlrevesC)
    return numeroAlrevesE

numero1 = RevertirNumero(obtenerNumero3Digitos())
numero2 = RevertirNumero(obtenerNumero3Digitos())

if numero1 > numero2:
    print("Numero mayor: ",numero1)
else:
    print("Numero mayor: ",numero2)