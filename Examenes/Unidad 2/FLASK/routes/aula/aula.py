from flask import Blueprint, request,jsonify
from models import Aula
from app import db

appaula = Blueprint('appaula', __name__)

@appaula.route('/indexAulaHTTP', methods=['GET'])
def obtenerAulasHTTP():
    aulas = Aula.query.all()
    aulas_json = [{"id": aula.id, "nombre_aula": aula.nombre_aula, "capacidad_maxima": aula.capacidad_maxima,
                  "edades_admitidas": aula.edades_admitidas, "maestro_a_cargo": aula.maestro_a_cargo} for aula in aulas]
    return jsonify(aulas_json)

@appaula.route('/agregarAulaHTTP', methods=['POST'])
def agregarAulaHTTP():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Datos no proporcionados"}), 400

        nombre_aula = data.get('nombre_aula', '')
        capacidad_maxima = data.get('capacidad_maxima', 0)
        edades_admitidas = data.get('edades_admitidas', '')
        maestro_a_cargo = data.get('maestro_a_cargo', '')

        aula = Aula(
            nombre_aula=nombre_aula,
            capacidad_maxima=capacidad_maxima,
            edades_admitidas=edades_admitidas,
            maestro_a_cargo=maestro_a_cargo
        )
        db.session.add(aula)
        db.session.commit()

        return jsonify({"message": "Aula agregada exitosamente"}), 201
    else:
        return jsonify({"error": "Solicitud no válida"}), 400

@appaula.route('/editarAulaHTTP/<int:id>', methods=['PUT'])
def editarAulaHTTP(id):
    aula = Aula.query.get(id)
    if not aula:
        return jsonify({"error": "Aula no encontrada"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos no proporcionados"}), 400

    if 'nombre_aula' in data:
        aula.nombre_aula = data['nombre_aula']
    if 'capacidad_maxima' in data:
        aula.capacidad_maxima = data['capacidad_maxima']
    if 'edades_admitidas' in data:
        aula.edades_admitidas = data['edades_admitidas']
    if 'maestro_a_cargo' in data:
        aula.maestro_a_cargo = data['maestro_a_cargo']

    db.session.commit()
    return jsonify({"message": "Se editó la información del aula"}), 200

@appaula.route('/eliminarAulaHTTP/<int:id>', methods=['DELETE'])
def eliminarAulaHTTP(id):
    aula = Aula.query.get_or_404(id)
    db.session.delete(aula)
    db.session.commit()
    
    return jsonify({"message": "Aula eliminada exitosamente"})

@appaula.route('/detalleAulaHTTP/<int:id>', methods=['GET'])
def detalleAulaHTTP(id):
    aula = Aula.query.get(id)
    if not aula:
        return jsonify({"error": "Aula no encontrada"}), 404
    respuesta = {
        "id": aula.id,
        "nombre_aula": aula.nombre_aula,
        "capacidad_maxima": aula.capacidad_maxima,
        "edades_admitidas": aula.edades_admitidas,
        "maestro_a_cargo": aula.maestro_a_cargo
    }

    return jsonify(respuesta), 200
