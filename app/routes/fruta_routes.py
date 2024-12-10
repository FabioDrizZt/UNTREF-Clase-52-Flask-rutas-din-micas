from flask import Blueprint
from app.controllers.frutas_controller import *

frutas_bp = Blueprint("frutas", __name__)

frutas_bp.route("/frutas", methods=["GET"])(get_all_frutas_controller)
frutas_bp.route("/frutas/<id>", methods=["GET"])(get_all_frutas_by_id_controller)
frutas_bp.route("/frutas/nombre/<name>", methods=["GET"])(get_all_frutas_by_name_controller)
frutas_bp.route("/frutas/precio/<importe>", methods=["GET"])(get_all_frutas_by_price_controller)