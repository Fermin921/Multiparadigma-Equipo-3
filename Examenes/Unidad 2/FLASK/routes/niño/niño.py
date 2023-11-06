from flask import Blueprint, request,jsonify
from models import Niño
from app import db

appniño = Blueprint('appniño', __name__)


@appniño.route('/indexNiñoHTTP', methods=['GET'])
def obtenerNiñosHTTP():
    niños = Niño.query.all()
    niños_json = [{"id": niño.id, "nombre": niño.nombre, "fecha_nacimiento": niño.fecha_nacimiento,
                   "genero": niño.genero, "tutor_principal": niño.tutor_principal} for niño in niños]
    return jsonify(niños_json)

@appniño.route('/agregarNiñoHTTP', methods=['POST'])
def agregarNiñoHTTP():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Datos no proporcionados"}), 400

        nombre = data.get('nombre', '')
        fecha_nacimiento = data.get('fecha_nacimiento', '')
        genero = data.get('genero', '')
        tutor_principal = data.get('tutor_principal', '')

        niño = Niño(
            nombre=nombre,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero,
            tutor_principal=tutor_principal
        )
        db.session.add(niño)
        db.session.commit()

        return jsonify({"message": "Niño agregado exitosamente"}), 201
    else:
        return jsonify({"error": "Solicitud no válida"}), 400

@appniño.route('/editarNiñoHTTP/<int:id>', methods=['PUT'])
def editarNiñoHTTP(id):
    niño = Niño.query.get(id)
    if not niño:
        return jsonify({"error": "Niño no encontrado"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos no proporcionados"}), 400

    if 'nombre' in data:
        niño.nombre = data['nombre']
    if 'fecha_nacimiento' in data:
        niño.fecha_nacimiento = data['fecha_nacimiento']
    if 'genero' in data:
        niño.genero = data['genero']
    if 'tutor_principal' in data:
        niño.tutor_principal = data['tutor_principal']

    db.session.commit()
    return jsonify({"message": "Se editó la información del niño"}), 200

@appniño.route('/eliminarNiñoHTTP/<int:id>', methods=['DELETE'])
def eliminarNiñoHTTP(id):
    niño = Niño.query.get_or_404(id)
    db.session.delete(niño)
    db.session.commit()
    
    return jsonify({"message": "Niño eliminado exitosamente"})

@appniño.route('/detalleNiñoHTTP/<int:id>', methods=['GET'])
def detalleNiñoHTTP(id):
    niño = Niño.query.get(id)
    if not niño:
        return jsonify({"error": "Niño no encontrado"}), 404
    respuesta = {
        "id": niño.id,
        "nombre": niño.nombre,
        "fecha_nacimiento": niño.fecha_nacimiento.strftime('%Y-%m-%d') if niño.fecha_nacimiento else None,
        "genero": niño.genero,
        "tutor_principal": niño.tutor_principal
    }

    return jsonify(respuesta), 200
