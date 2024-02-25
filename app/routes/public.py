from flask import Blueprint, render_template

public_bp = Blueprint("public", __name__)


@public_bp.route("/")
def home():
    return render_template("home.html")

@public_bp.route("/blog")
def blog():
    return render_template("blog.html")

@public_bp.route("/blog_detail")
def blog_detail():
    return render_template("blog_detail.html")

@public_bp.route("/contact")
def contact():
    return render_template("contact.html")