from flask import Blueprint, request,jsonify
from models import Tutor
from app import db

apptutor = Blueprint('apptutor', __name__)

@apptutor.route('/indexTutorHTTP', methods=['GET'])
def obtenerTutoresHTTP():
    tutores = Tutor.query.all()
    tutores_json = [{"id": tutor.id, "nombre": tutor.nombre, "apellido": tutor.apellido,
                    "direccion": tutor.direccion, "numero_telefono": tutor.numero_telefono} for tutor in tutores]
    return jsonify(tutores_json)

@apptutor.route('/agregarTutorHTTP', methods=['POST'])
def agregarTutorHTTP():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Datos no proporcionados"}), 400

        nombre = data.get('nombre', '')
        apellido = data.get('apellido', '')
        direccion = data.get('direccion', '')
        numero_telefono = data.get('numero_telefono', '')

        tutor = Tutor(
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            numero_telefono=numero_telefono
        )
        db.session.add(tutor)
        db.session.commit()

        return jsonify({"message": "Tutor agregado exitosamente"}), 201
    else:
        return jsonify({"error": "Solicitud no válida"}), 400

@apptutor.route('/editarTutorHTTP/<int:id>', methods=['PUT'])
def editarTutorHTTP(id):
    tutor = Tutor.query.get(id)
    if not tutor:
        return jsonify({"error": "Tutor no encontrado"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos no proporcionados"}), 400

    if 'nombre' in data:
        tutor.nombre = data['nombre']
    if 'apellido' in data:
        tutor.apellido = data['apellido']
    if 'direccion' in data:
        tutor.direccion = data['direccion']
    if 'numero_telefono' in data:
        tutor.numero_telefono = data['numero_telefono']

    db.session.commit()
    return jsonify({"message": "Se editó la información del tutor"}), 200

@apptutor.route('/eliminarTutorHTTP/<int:id>', methods=['DELETE'])
def eliminarTutorHTTP(id):
    tutor = Tutor.query.get_or_404(id)
    db.session.delete(tutor)
    db.session.commit()
    
    return jsonify({"message": "Tutor eliminado exitosamente"})

@apptutor.route('/detalleTutorHTTP/<int:id>', methods=['GET'])
def detalleTutorHTTP(id):
    tutor = Tutor.query.get(id)
    if not tutor:
        return jsonify({"error": "Tutor no encontrado"}), 404
    respuesta = {
        "id": tutor.id,
        "nombre": tutor.nombre,
        "apellido": tutor.apellido,
        "direccion": tutor.direccion,
        "numero_telefono": tutor.numero_telefono
    }

    return jsonify(respuesta), 200
