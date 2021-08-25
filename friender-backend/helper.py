import os
import boto3
import botocore

aws_access_key = os.environ.get('S3_ACCESS_KEY')
aws_secret_key = os.environ.get('S3_SECRET_KEY')

bucket_name='friender-rithm-r-s'

s3 =boto3.client(
  "s3",
  aws_access_key,
  aws_secret_key
)

def upload_file(file, profile):
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
              "ACL":"public-read",
              "ContentType": file.content_type
            }
        )
    except Exception as e:
        print("Something Happened: ", e)