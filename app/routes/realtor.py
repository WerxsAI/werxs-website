from flask import Blueprint, render_template

realtor_bp = Blueprint("realtor", __name__)


@realtor_bp.route("/realtor")
def realtor():
    return render_template("coming_soon.html")