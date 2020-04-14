from flask import Blueprint

training = Blueprint('training', __name__ , template_folder='templates')

from app.training import routes
