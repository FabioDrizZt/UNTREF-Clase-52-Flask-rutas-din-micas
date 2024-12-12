from flask import jsonify, request
# from app.models.fruta_mongo import *

from app.models.fruta_mysql import *
# from app.models.fruta_file import *


def get_all_frutas_controller():
    try:
        frutas = get_all_frutas()
        if not frutas:
            jsonify({"message": "No se encontraron las frutas"}), 500
        return jsonify(frutas), 200
    except TypeError as err:
        print("Error al obtener las frutas: ", err)
        return []


def get_all_frutas_by_id_controller(id):
    try:
        fruta = get_all_frutas_by_id(int(id))
        if not fruta:
            jsonify({"message": "No se encontró la fruta"}), 500
        return jsonify(fruta), 200
    except TypeError as err:
        print("Error al obtener la fruta: ", err)
        return []


def get_all_frutas_by_name_controller(name):
    try:
        fruta = get_all_frutas_by_name(name)
        if not fruta:
            jsonify({"message": "No se encontró la fruta"}), 500
        return jsonify(fruta), 200
    except TypeError as err:
        print("Error al obtener la fruta: ", err)
        return []


def get_all_frutas_by_price_controller(importe):
    try:
        fruta = get_all_frutas_by_price(int(importe))
        if not fruta:
            jsonify({"message": "No se encontró la fruta"}), 500
        return jsonify(fruta), 200
    except TypeError as err:
        print("Error al obtener la fruta: ", err)
        return []

def create_fruta_controller():
    try:
        data = request.get_json()
        fruta = create_fruta(data)
        return jsonify(fruta), 201
    except Exception as e:
        print('Error al crear la fruta:', e)
        return jsonify({'message': 'Error al crear la fruta'}), 500


def update_fruta_controller(id):
    try:
        data = request.get_json()
        fruta = update_fruta(id, data)
        if not fruta:
            return jsonify({"message": "No se encontró la fruta"}), 404
        return jsonify(fruta), 200
    except Exception as e:
        print("Error al actualizar la fruta:", e)
        return jsonify({"message": "Error al actualizar la fruta"}), 500


def delete_fruta_controller(id):
    try:
        fruta = delete_fruta(id)
        if not fruta:
            return jsonify({"message": "No se encontró la fruta"}), 404
        return jsonify({"message": "Fruta eliminada"}), 200
    except Exception as e:
        print("Error al eliminar la fruta:", e)
        return jsonify({"message": "Error al eliminar la fruta"}), 500
