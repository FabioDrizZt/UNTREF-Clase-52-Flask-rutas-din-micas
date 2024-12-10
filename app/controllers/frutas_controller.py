from flask import jsonify
from app.models.fruta_model import *
# from app.models.fruta_file import *

def get_all_frutas_controller():
  try:
    frutas = get_all_frutas()
    if not frutas:
      jsonify({'message': 'No se encontraron las frutas' }), 500
    return jsonify(frutas), 200
  except TypeError as err:
    print('Error al obtener las frutas: ', err)
    return []
  
def get_all_frutas_by_id_controller(id):
  try:
    fruta = get_all_frutas_by_id(int(id))
    if not fruta:
      jsonify({'message': 'No se encontró la fruta' }), 500
    return jsonify(fruta), 200
  except TypeError as err:
    print('Error al obtener la fruta: ', err)
    return []
  
def get_all_frutas_by_name_controller(name):
  try:
    fruta = get_all_frutas_by_name(name)
    if not fruta:
      jsonify({'message': 'No se encontró la fruta' }), 500
    return jsonify(fruta), 200
  except TypeError as err:
    print('Error al obtener la fruta: ', err)
    return []
  
def get_all_frutas_by_price_controller(importe):
  try:
    fruta = get_all_frutas_by_price(int(importe))
    if not fruta:
      jsonify({'message': 'No se encontró la fruta' }), 500
    return jsonify(fruta), 200
  except TypeError as err:
    print('Error al obtener la fruta: ', err)
    return []