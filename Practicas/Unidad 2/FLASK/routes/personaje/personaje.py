from flask import Blueprint, request, redirect, render_template, url_for,jsonify
from models import Personaje
from forms import PersonajeForm
from app import db

apppersonaje = Blueprint('apppersonaje', __name__, template_folder="templates/personaje")

@apppersonaje.route('/indexPersonaje')
def inicio():
    personajes = Personaje.query.all()
    return render_template('personaje/indexPersonaje.html', personajes=personajes)

@apppersonaje.route('/agregarPersonaje', methods=["GET", "POST"])
def agregarPersonaje():
    personaje = Personaje()
    personajeForm = PersonajeForm(obj=personaje)
    if request.method == "POST":
        if personajeForm.validate_on_submit():
            personajeForm.populate_obj(personaje)
            db.session.add(personaje)
            db.session.commit()
            return redirect(url_for('apppersonaje.inicio'))
    return render_template('personaje/agregarPersonaje.html', forma=personajeForm)

@apppersonaje.route("/editarPersonaje/<int:id>", methods=["GET", "POST"])
def editarPersonaje(id):
    personaje = Personaje.query.get_or_404(id)
    personajeForm = PersonajeForm(obj=personaje)
    if request.method == "POST":
        if personajeForm.validate_on_submit():
            personajeForm.populate_obj(personaje)
            db.session.commit()
            return redirect(url_for('apppersonaje.inicio'))
    return render_template('personaje/editarPersonaje.html', forma=personajeForm)

@apppersonaje.route('/eliminarPersonaje/<int:id>')
def eliminarPersonaje(id):
    personaje = Personaje.query.get_or_404(id)
    db.session.delete(personaje)
    db.session.commit()
    return redirect(url_for('apppersonaje.inicio'))

@apppersonaje.route('/detallePersonaje/<int:id>')
def detallePersonaje(id):
    personaje = Personaje.query.get_or_404(id)
    return render_template('personaje/detallePersonaje.html', personaje=personaje)

#Peticiones HTTP desde JSON
@apppersonaje.route('/indexPersonajeHTTP', methods=['GET'])
def obtenerPersonajesHTTP():
    personajes = Personaje.query.all()
    personajes_json = [{"id": personaje.id, "nombre": personaje.nombre, "descripcion": personaje.descripcion,
                       "franquicia": personaje.franquicia, "habilidades": personaje.habilidades,
                       "fecha_creacion": personaje.fecha_creacion} for personaje in personajes]
    return jsonify(personajes_json)

@apppersonaje.route('/agregarPersonajeHTTP', methods=['POST'])
def agregarPersonajeHTTP():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Datos no proporcionados"}), 400

        nombre = data.get('nombre', '')
        descripcion = data.get('descripcion', '')
        franquicia = data.get('franquicia', '')
        habilidades = data.get('habilidades', '')
        fecha_creacion = data.get('fecha_creacion', '')

        personaje = Personaje(
            nombre=nombre,
            descripcion=descripcion,
            franquicia=franquicia,
            habilidades=habilidades,
            fecha_creacion=fecha_creacion
        )
        db.session.add(personaje)
        db.session.commit()

        return jsonify({"message": "Personaje agregado exitosamente"}), 201
    else:
        return jsonify({"error": "Solicitud no válida"}), 400
    
    
@apppersonaje.route('/editarPersonajeHTTP/<int:id>', methods=['PUT'])
def editarPersonajeHTTP(id):
    personaje = Personaje.query.get(id)
    if not personaje:
        return jsonify({"error": "Personaje no encontrado"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos no proporcionados"}), 400

    if 'nombre' in data:
        personaje.nombre = data['nombre']
    if 'descripcion' in data:
        personaje.descripcion = data['descripcion']
    if 'franquicia' in data:
        personaje.franquicia = data['franquicia']
    if 'habilidades' in data:
        personaje.habilidades = data['habilidades']
    if 'fecha_creacion' in data:
        personaje.fecha_creacion = data['fecha_creacion']
    
    db.session.commit()
    return jsonify({"message": "Se editó la información del personaje"}), 200

@apppersonaje.route('/eliminarPersonajeHTTP/<int:id>', methods=['DELETE'])
def eliminarPersonajeHTTP(id):
    personaje = Personaje.query.get_or_404(id)
    db.session.delete(personaje)
    db.session.commit()
    
    return jsonify({"message": "Personaje eliminado exitosamente"})
