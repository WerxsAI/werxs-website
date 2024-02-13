from flask import Blueprint, render_template

admin_hp = Blueprint("admin", __name__)


@admin_hp.route("/")
def home():
    return render_template("admin_hp.html")
