import boto3 
from boto3.dynamodb.conditions import Key, Attr
from msilib import Table
# Python and Boto3 to scan table. 

response = Table.scan(
    FilterExpression=Attr('SoungTitle').begins_with('C')
)
items = response['Items']
print(items)