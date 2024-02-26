from flask import Flask, request, jsonify, flash, redirect, Blueprint, render_template
import boto3
from werkzeug.utils import secure_filename
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

# Configure your S3 bucket details
S3_BUCKET = env.get("S3_BUCKET")
S3_KEY = env.get("S3_KEY")
S3_SECRET = env.get("S3_SECRET")
s3 = boto3.client("s3", aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)

ALLOWED_EXTENSIONS = {"csv", "json"}

data_upload_bp = Blueprint("data_upload", __name__)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@data_upload_bp.route("/generate_presigned_url", methods=["POST"])
def generate_presigned_url():
    filename = request.json.get("filename")
    filetype = request.json.get("filetype")
    if not filename or not filetype:
        return jsonify({"error": "Missing filename or filetype"}), 400

    if allowed_file(filename):
        presigned_url = s3.generate_presigned_url(
            "put_object",
            Params={"Bucket": S3_BUCKET, "Key": filename, "ContentType": filetype},
            ExpiresIn=3600,  # URL expires in 1 hour
        )
        return jsonify({"url": presigned_url, "filename": filename})
    else:
        return jsonify({"error": "File type not allowed"}), 400


@data_upload_bp.route("/data_upload", methods=["GET", "POST"])
def data_upload():
    if request.method == "GET":
        # Render the data upload form when the user navigates to the page
        return render_template("data_upload.html")
    else:  # POST
        # Extract form data or handle file upload
        llm_model = request.form.get("llmModel")
        s3_file_key = request.form.get("s3FileKey")
        s3_file_url = request.form.get("s3FileUrl")

        if not llm_model or not s3_file_key or not s3_file_url:
            flash("Missing data")
            return redirect(request.url)

        # Process the data, e.g., save to database and provide feedback
        flash("File successfully uploaded with LLM Model: " + llm_model)
        return redirect("/")
