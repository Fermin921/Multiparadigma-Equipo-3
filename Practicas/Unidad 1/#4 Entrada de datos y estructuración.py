# Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture
# las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato
# “{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre y una LISTA de
# todas las materias

CargaAcademica = {}
TotalCreditos = 0
Materias = []

print("Piense en sus materias favoritas de semestres pasados inferior a 8vo")
    
while True:
    try:
        Materia = input("Favor de ingresar el nombre de la materia: ")
        
        while True:
            Creditos = int(input("Agregar la cantidad de créditos con la que cuenta la materia: "))
            if Creditos<0:
                print("Debe ingresar números positivos.")
            else:
                break
                  
        CargaAcademica[Materia] = Creditos
        TotalCreditos += Creditos
        Materias.append(Materia)
        seguir = input("Si desea terminar de ingresar materias escriba \"exit\" sino da enter: ")
        if seguir.lower()=='exit':
            break
    except ValueError:
        print("Debes ingresar un número entero.")

print("RESUMEN DE MATERIAS")
for Materia, Creditos in CargaAcademica.items():
    print(f'"{Materia}" tiene "{Creditos}" créditos.')

print(f"Total de créditos del semestre: {TotalCreditos}")
print(f"Lista de todas las materias: {Materias}")
