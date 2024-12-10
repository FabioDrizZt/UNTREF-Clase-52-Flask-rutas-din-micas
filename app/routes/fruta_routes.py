from flask import Blueprint
from app.controllers.frutas_controller import get_all_frutas_controller

frutas_bp = Blueprint("frutas", __name__)

frutas_bp.route("/frutas")(get_all_frutas_controller)