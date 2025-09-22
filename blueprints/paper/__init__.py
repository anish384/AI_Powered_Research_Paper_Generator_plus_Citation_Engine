from flask import Blueprint

paper_bp = Blueprint('paper', __name__)

from . import routes
