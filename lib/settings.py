import os
from dotenv import load_dotenv


load_dotenv()

aws_region = os.getenv("AWS_REGION")
aws_bucket_name = os.getenv("AWS_BUCKET_NANE")
aws_cloudfront_host = os.getenv("AWS_CLOUDFRONT_HOST")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

mongo_uri = "mongodb+srv://NailedItReadWrite:nailedit0916@nailedit.cpmjygq.mongodb.net/nailedit"
mongo_dbname = "nailedit"
