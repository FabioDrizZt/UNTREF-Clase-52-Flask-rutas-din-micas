from flask import jsonify
from app.models.fruta_model import get_all_frutas

def get_all_frutas_controller():
  try:
    frutas = get_all_frutas()
    if not frutas:
      jsonify({'message': 'No se encontraron las frutas' }), 500
    return jsonify(frutas), 200
  except TypeError as err:
    print('Error al obtener las frutas: ', err)
    return []