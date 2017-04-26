from flask import Flask, render_template, request, redirect,jsonify, url_for, flash, Blueprint
from pkg import app
from markupsafe import escape

index_b = Blueprint('index_b', __name__)


@index_b.route('/')
def index():
    return render_template("front_end/index.html")
