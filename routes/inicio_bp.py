from flask import Blueprint

from controllers.InicioController import index, home, frmlogin, logout, login

inicio_bp = Blueprint('inicio_bp', __name__, template_folder='templates/')
inicio_bp.route('/', methods=['GET'])(index)
# TODO
inicio_bp.route('/home', methods=['GET'])(home)
inicio_bp.route('/login', methods=['POST'])(login)
inicio_bp.route('/logout', methods=['GET'])(logout)
inicio_bp.route('/frmlogin', methods=['GET'])(frmlogin)
