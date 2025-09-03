import boto3

def get_ssm_param(name):
    ssm = boto3.client('ssm')
    response = ssm.get_parameter(Name=name, WithDecryption=False)
    return response['Parameter']['Value']

AWS_REGION = "ap-south-1"
S3_BUCKET_NAME = get_ssm_param("/welldesk/s3/bucket_name")
