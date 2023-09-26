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
Contador = 1
while Contador == 1:
    num = int(input("Favor de ingresar un valor: "))
    if num <= 0:
        print("Favor de ingresar un numero valido")
    Parametros.append(num)
    Contador = int(input("¿Quiere seguir agregando numeros? 1.Si 2.No "))

if len(Parametros) <= 1:
    print("No se realizaron las operaciones ya que no se ingreso mas de 1 numero")
else:
    TotalSuma, TotalProducto = CalcularProductoTotal(*Parametros)
    print(f"El total del producto es {TotalProducto}")
    print(f"El total del producto es {TotalSuma}")
