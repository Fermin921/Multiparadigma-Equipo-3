from flask import Blueprint, request,jsonify
from models import Comida
from app import db

appcomida = Blueprint('appcomida', __name__)

@appcomida.route('/indexComidaHTTP', methods=['GET'])
def obtenerComidasHTTP():
    comidas = Comida.query.all()
    comidas_json = [{"id": comida.id, "nombre_comida": comida.nombre_comida, "descripcion": comida.descripcion,
                    "tipo_comida": comida.tipo_comida, "horario_servicio": comida.horario_servicio} for comida in comidas]
    return jsonify(comidas_json)

@appcomida.route('/agregarComidaHTTP', methods=['POST'])
def agregarComidaHTTP():
    if request.headers.get('Content-Type') == 'application/json':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Datos no proporcionados"}), 400

        nombre_comida = data.get('nombre_comida', '')
        descripcion = data.get('descripcion', '')
        tipo_comida = data.get('tipo_comida', '')
        horario_servicio = data.get('horario_servicio', '')

        comida = Comida(
            nombre_comida=nombre_comida,
            descripcion=descripcion,
            tipo_comida=tipo_comida,
            horario_servicio=horario_servicio
        )
        db.session.add(comida)
        db.session.commit()

        return jsonify({"message": "Comida agregada exitosamente"}), 201
    else:
        return jsonify({"error": "Solicitud no válida"}), 400

@appcomida.route('/editarComidaHTTP/<int:id>', methods=['PUT'])
def editarComidaHTTP(id):
    comida = Comida.query.get(id)
    if not comida:
        return jsonify({"error": "Comida no encontrada"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos no proporcionados"}), 400

    if 'nombre_comida' in data:
        comida.nombre_comida = data['nombre_comida']
    if 'ingredientes' in data:
        comida.ingredientes = data['ingredientes']
    if 'restricciones_alimenticias' in data:
        comida.restricciones_alimenticias = data['restricciones_alimenticias']
    if 'fecha_introduccion' in data:
        comida.fecha_introduccion = data['fecha_introduccion']

    db.session.commit()
    return jsonify({"message": "Se editó la información de la comida"}), 200

@appcomida.route('/eliminarComidaHTTP/<int:id>', methods=['DELETE'])
def eliminarComidaHTTP(id):
    comida = Comida.query.get_or_404(id)
    db.session.delete(comida)
    db.session.commit()
    
    return jsonify({"message": "Comida eliminada exitosamente"})

@appcomida.route('/detalleComidaHTTP/<int:id>', methods=['GET'])
def detalleComidaHTTP(id):
    comida = Comida.query.get(id)
    if not comida:
        return jsonify({"error": "Comida no encontrada"}), 404
    respuesta = {
        "id": comida.id,
        "nombre_comida": comida.nombre_comida,
        "ingredientes": comida.ingredientes,
        "restricciones_alimenticias": comida.restricciones_alimenticias,
        "fecha_introduccion": comida.fecha_introduccion.strftime('%Y-%m-%d') if comida.fecha_introduccion else None
    }

    return jsonify(respuesta), 200
