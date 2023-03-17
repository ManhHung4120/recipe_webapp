import base64
import os
import boto3, botocore
from models import Image
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.utils import secure_filename
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

def upload_file_to_s3(file, acl="public-read"):
    filename = secure_filename(file.filename)
    try:
        s3.upload_fileobj(
            file,
            os.getenv("AWS_BUCKET_NAME"),
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e

    # after upload file to s3 bucket, return filename of the uploaded file
    return file.filename
def get_image_from_s3(filename):
    try:
        image_object = s3.get_object(Bucket= os.getenv("AWS_BUCKET_NAME"), Key=filename)
        image_content = image_object['Body'].read()

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
            return ""

    return image_content

def getImageFromImageId(image_id):
    if image_id == "default":
        return "", ""
    try:
        image_obj = Image.query.filter_by(image_id=image_id).first()
    except SQLAlchemyError as e:
        error = f"Failed to query user: {e.__class__.__name__}"
        return "", error
    if image_obj:
        image_name = image_obj.image
        image = get_image_from_s3(image_name)
        image_encode = base64.b64encode(image.read())
        return image_encode, ""
    return "",""


    