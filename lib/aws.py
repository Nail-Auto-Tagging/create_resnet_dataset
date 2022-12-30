import boto3
from lib.settings import (
    aws_access_key_id,
    aws_secret_access_key,
    aws_bucket_name,
    aws_region,
    aws_cloudfront_host,
)

s3_client = boto3.client(
    service_name="s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region,
)

meta = {
    "png": {"ContentType": "binary/octet-stream", "ACL": "public-read"},
    "jpeg": {"ContentType": "image/jpeg", "ACL": "public-read"},
    "jpg": {"ContentType": "image/jpeg", "ACL": "public-read"},
}


def upload_image_to_s3(local_path, s3_path):
    s3_client.upload_file(
        local_path,
        aws_bucket_name,
        s3_path,
        ExtraArgs=meta["jpg"],
    )
    return f"{aws_cloudfront_host}/{s3_path}"
