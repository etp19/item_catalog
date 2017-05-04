from flask import render_template, Blueprint

index_b = Blueprint('index_b', __name__)


@index_b.route('/')
def index():
    return render_template("front_end/index.html")
