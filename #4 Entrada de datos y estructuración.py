# Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture
# las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato
# “{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre y una LISTA de
# todas las materias

CargaAcademica = {}
TotalCreditos = 0
Materias = []

print("Piense en sus materias favoritas de semestres pasados inferior a 8vo")
while True:
    Materia = input("Favor de ingresar el nombre de la materia: ")
    Creditos = int(
        input("Agregar la cantidad de creditos con la que cuenta la materia: ")
    )
    CargaAcademica[Materia] = Creditos
    TotalCreditos += Creditos
    Materias.append(Materia)
    Pregunta = int(
        input("¿Quiere seguir ingresando materias? (1 para Sí, 2 para No): ")
    )
    if Pregunta == 2:
        break

print("Resumen de materias")
for Materia, Creditos in CargaAcademica.items():
    print(f'"{Materia}" tiene "{Creditos}" creditos.')

print(f"Total de creditos del semestre: {TotalCreditos}")
