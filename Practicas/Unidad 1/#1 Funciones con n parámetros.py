# Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el
# producto total y su suma total

def CalcularProductoTotal(*args):
    TotalProduc = 1
    TotalSuma = 0
    for n in args:
        TotalProduc *= n
        TotalSuma += n
    return TotalSuma, TotalProduc

Parametros = []

#Validar entrada
while True:
    try:
        num = float(input("Ingresa un valor de tipo numérico: "))
        Parametros.append(num)
        seguir = input("Si desea terminar de ingresar escriba \"exit\" sino da enter: ")
        if seguir.lower()=='exit':
            break
    except ValueError:
        print("Debes ingresar un valor de tipo numérico.")

if len(Parametros) <= 1:
    print("No se realizaron las operaciones ya que no se ingreso más de 1 número")
else:
    TotalSuma, TotalProducto = CalcularProductoTotal(*Parametros)
    print(f"El total del producto es: {TotalProducto}")
    print(f"La suma total es: {TotalSuma}")
