from app import db

class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    franquicia = db.Column(db.String(50))
    habilidades = db.Column(db.String(200))
    fecha_creacion = db.Column(db.Date)
    imagen = db.Column(db.String(200))  # Ruta de la imagen del personaje

    def __str__(self):
        return f"Personaje(id={self.id}, nombre='{self.nombre}', descripción='{self.descripcion}', franquicia='{self.franquicia}', habilidades='{self.habilidades}', fecha_creación='{self.fecha_creacion}')"

class Juego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_lanzamiento = db.Column(db.Date)
    genero = db.Column(db.String(50))
    copias_vendidas = db.Column(db.Integer)
    imagen = db.Column(db.String(200))  # Ruta de la imagen del juego

    def __str__(self):
        return f"Juego(id={self.id}, nombre='{self.nombre}', fecha_lanzamiento={self.fecha_lanzamiento}, género='{self.genero}', copias_vendidas={self.copias_vendidas})"

class Consola(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_lanzamiento = db.Column(db.Date)
    generacion = db.Column(db.String(50))
    consolas_vendidas = db.Column(db.Integer)
    imagen = db.Column(db.String(200))  # Ruta de la imagen de la consola

    def __str__(self):
        return f"Consola(id={self.id}, nombre='{self.nombre}', fecha_lanzamiento='{self.fecha_lanzamiento}', generación='{self.generacion}', consolas_vendidas={self.consolas_vendidas})"


    
    
# @appersona.route("/agregarJson",method=["POST"])
# def agregarJson():
#     json = request.get_json()
#     persona = Persona()
#     persona.email = json["email"]
#     persona.nombre = json["nombre"]
#     persona.apellido = json["apellido"]
#     db.session.add(persona)
#     db.session.commit()
#     return jsonify({"status":200,"mensaje":"persona agregada"})

# @appersona.route("/editarJson",method=["POST"])
# def editarJson():
#     json = request.get_json()
#     persona = Persona.query.get_or_404(json["id"])
#     persona.email = json["email"]
#     persona.nombre = json["nombre"]
#     persona.apellido = json["apellido"]
    
#     db.session.commit()
#     return jsonify({"status":200,"mensaje":"persona actualizada"})
    