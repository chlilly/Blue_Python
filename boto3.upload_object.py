import boto3

s3 = boto3.client('s3')

filename = 'additemsWK14.py'
bucket_name="chilly-buckets"

with open(filename, 'rb') as data:
    s3.upload_fileobj(data, bucket_name, filename)
    print("Object Uploaded")