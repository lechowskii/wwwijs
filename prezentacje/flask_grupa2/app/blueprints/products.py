
from flask import Blueprint, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from ..database import db_session

bp = Blueprint("products",__name__,template_folder="/templates",url_prefix="/products")

@bp.get("/")
def get_products():
    return render_template("products.html")

@bp.route("/add", methods=('GET','POST'))
def add_product():
    return redirect(url_for(get_products()))

@bp.route("/delete/<int:id>")
def delete_product():
    return redirect(url_for(get_products()))
