from flask import Blueprint

api = Blueprint('main', __name__)

from . import applications, classrooms
