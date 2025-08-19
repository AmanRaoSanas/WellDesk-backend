import boto3
from config import AWS_REGION, S3_BUCKET_NAME

s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_file_to_s3(file_content, filename):
    try:
        s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=filename, Body=file_content)
        return True
    except Exception as e:
        print(f"Upload failed: {e}")
        return False
