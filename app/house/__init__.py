from flask import Blueprint

main = Blueprint('house',__name__)

from . import views,errors
