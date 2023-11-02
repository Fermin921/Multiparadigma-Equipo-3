#Clase Usuario
class Usuario:
    def __init__(self, usuario, contraseña, rol, nombre, curp, ciudad):
        self.usuario = usuario
        self.contraseña = contraseña
        self.rol = rol
        self.nombre = nombre
        self.curp = curp
        self.ciudad = ciudad
        
    def __str__(self):
        return f"Usuario: {self.usuario}, Contraseña: {self.contraseña}, Rol: {self.rol}, Nombre: {self.nombre}, CURP: {self.curp}, Ciudad: {self.ciudad}"
    
    
# se almacenan los usuarios en una lista
usuariosRegistrados=[]

def registrarUsuario():
    usuario=input("Usuario: ")
    contraseña = input("Contraseña: ")
    rol = "Cliente"
    nombre = input("Nombre: ")
    curp = input("CURP: ")
    ciudad = input("Ciudad: ")
    
    for usuario_existente in usuariosRegistrados:
        if usuario_existente.curp==curp:
            print("El usuario ya existe")
            return
        
    usuarioNuevo=Usuario(usuario, contraseña, rol, nombre, curp, ciudad)
    usuariosRegistrados.append(usuarioNuevo)
    print("Usuario registrado exitosamente")
    
# Usuario Administrador declarado
usuarioAdministrador=Usuario("Barrabasito","admin","Administrador","Juan","JHRSNA20020NA2","Nuevo Laredo")
usuariosRegistrados.append(usuarioAdministrador)

def iniciarSesion():
    usuario=input("Usuario: ")
    contraseña=input("Contrasena: ")
    
    for usuarioExistente in usuariosRegistrados:
        if usuarioExistente.usuario==usuario and usuarioExistente.contraseña==contraseña:
            print("Has iniciado sesión.")
            print("Información de inicio de sesión: ")
            if usuarioExistente.rol=="Administrador":
                for usuarioRegistrado in usuariosRegistrados:
                    print(usuarioRegistrado)
            else:
                print(usuarioExistente)
            return
        
    print("Error al iniciar Sesión datos Incorrectos.")
    
def main():
    while True:
        print("\nMenú: \n1. Registro\n2. Inicio de Sesión\n3. Salida\n")
        
        opcion= input("Seleciona una opción: ")
        
        if opcion=="1":
            registrarUsuario()
        elif opcion=="2":
            iniciarSesion()
        elif opcion=="3":
            print("Saliste")
            break
        else:
            print("Introduce una opción válida del Menú.")
            
if __name__ == "__main__":
    main()

