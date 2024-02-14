from flask import Blueprint, render_template

realtor_hp = Blueprint("realtor", __name__)


@realtor_hp.route("/realtor")
def realtor():
    return render_template("coming_soon.html")