#AWS Automation clusing Boto3. 
#Create S3 Bucket using Python Boto3. 
from importlib.resources import is_resource
import boto3
aws_resoure = boto3.resource("s3")
bucket = is_resource.Bucket("getbuckets")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-1'
    },
)

print(response)