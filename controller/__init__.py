
from flask import *

def create_api():
    api = Blueprint('api', __name__)
    return api
api=create_api()

from . import cafes,favor,member,message,photo,rating,users




