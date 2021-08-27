import os
import boto3
from dotenv import load_dotenv

load_dotenv()
aws_access_key = os.environ.get('S3_ACCESS_KEY')
aws_secret_key = os.environ.get('S3_SECRET_KEY')

bucket_name='friender-rithm-r-s'

s3 = boto3.client(
  "s3",
  region_name="us-west-1",
  aws_access_key_id=aws_access_key,
  aws_secret_access_key=aws_secret_key
)


def upload_file(file, object_name=None):

    if object_name is None:
        object_name = os.path.basename(file)

    try:
        s3.put_object(file, bucket_name ,object_name, ExtraArgs={ "ContentType": "image/jpeg"})

    except Exception as e:
        print("Something Happened: ", e)


file = "/Users/simonzhang/Desktop/Rithm/week-10/Friender/friender-backend/rick-and-morty.jpg"
upload_file(file)