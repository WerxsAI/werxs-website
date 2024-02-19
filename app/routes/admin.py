from flask import Blueprint, render_template
from app.util.auth_util import login_required

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin")
@login_required
def home():
    return render_template("admin.html")
