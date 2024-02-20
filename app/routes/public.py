from flask import Blueprint, render_template

public_bp = Blueprint("public", __name__)


@public_bp.route("/")
def home():
    return render_template("home.html")

@public_bp.route("/news")
def news():
    return render_template("news.html")

@public_bp.route("/contact")
def contact():
    return render_template("contact.html")