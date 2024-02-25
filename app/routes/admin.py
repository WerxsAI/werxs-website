from flask import Blueprint, render_template, url_for, redirect, flash, request
from app.util.auth_util import login_required

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin/home")
@login_required
def home():
    return render_template("admin.html")


@admin_bp.route("/admin/create_blog", methods=["GET", "POST"])
def create_blog():
    
    # import db and form and model
    from app.forms.blogPostForm import BlogPostForm
    from app.util.db_util import getDB
    from app.models.BlogModel import BlogModel
    # Debugging: Confirm the function is hit
    print("Create blog route hit")
    form = BlogPostForm()
    if form.validate_on_submit():
        # Debugging: Check form validation success
        print("Form validated")
        db = getDB()
        blog_model = BlogModel(db)
        blog_id = blog_model.create_blog_post(
            title=form.title.data,
            author=form.author.data,
            content=form.content.data,
            category_name=form.category_name.data,
            image_url=form.image_url.data,
        )
        flash("Blog post created successfully!", "success")
        return redirect(url_for("admin.home"))
    else:
        # If this is printed, there's a validation error or the form hasn't been submitted
        print("Form not validated or not submitted")
    return render_template(
        "admin/create_blog.html", title="Create Blog Post", form=form
    )
