from flask import Flask, request, redirect, flash
import boto3
from werkzeug.utils import secure_filename
from flask import current_app as app

# Configure your S3 bucket details
S3_BUCKET = "your_bucket_name"
S3_KEY = "your_aws_access_key_id"
S3_SECRET = "your_aws_secret_access_key"
S3_LOCATION = f"http://{S3_BUCKET}.s3.amazonaws.com/"

s3 = boto3.client("s3", aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)


def upload_file_to_s3(file, bucket_name, acl="public-read"):
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={"ACL": acl, "ContentType": file.content_type},
        )

    except Exception as e:
        # In case the upload fails
        print("Something Happened: ", e)
        return e

    return f"{S3_LOCATION}{file.filename}"


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("No file part")
        return redirect(request.url)

    file = request.files["file"]

    if file.filename == "":
        flash("No selected file")
        return redirect(request.url)

    if file:
        output = upload_file_to_s3(file, S3_BUCKET)
        return str(output)


if __name__ == "__main__":
    app.run(debug=True)
