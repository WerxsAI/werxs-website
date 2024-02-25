# app/forms.py or app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class BlogPostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    content = TextAreaField(
        "Content", validators=[DataRequired()]
    )  # This will be enhanced with TinyMCE in the template
    category_name = StringField("Category Name", validators=[DataRequired()])
    image_url = StringField("Image URL")
    submit = SubmitField("Post")
