from app import db

class Niño(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    genero = db.Column(db.String(20))
    tutor_principal = db.Column(db.String(100))

    def __str__(self):
        return f"Niño(id={self.id}, nombre='{self.nombre}', fecha de nacimiento='{self.fecha_nacimiento}', género='{self.genero}', tutor principal='{self.tutor_principal}')"

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200))
    numero_telefono = db.Column(db.String(20))

    def __str__(self):
        return f"Tutor(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', dirección='{self.direccion}', número de teléfono='{self.numero_telefono}')"

class PersonalGuarderia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    puesto = db.Column(db.String(50))
    fecha_contratacion = db.Column(db.Date)

    def __str__(self):
        return f"PersonalGuarderia(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', puesto='{self.puesto}', fecha de contratación='{self.fecha_contratacion}')"

class Aula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_aula = db.Column(db.String(100), nullable=False)
    capacidad_maxima = db.Column(db.Integer)
    edades_admitidas = db.Column(db.String(50))
    maestro_a_cargo = db.Column(db.String(100))

    def __str__(self):
        return f"Aula(id={self.id}, nombre de aula='{self.nombre_aula}', capacidad máxima='{self.capacidad_maxima}', edades admitidas='{self.edades_admitidas}', maestro a cargo='{self.maestro_a_cargo}')"

class Comida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_comida = db.Column(db.String(100), nullable=False)
    ingredientes = db.Column(db.String(200))
    restricciones_alimenticias = db.Column(db.String(100))
    fecha_introduccion = db.Column(db.Date)

    def __str__(self):
        return f"Comida(id={self.id}, nombre de comida='{self.nombre_comida}', ingredientes='{self.ingredientes}', restricciones alimenticias='{self.restricciones_alimenticias}', fecha de introducción='{self.fecha_introduccion}')"
