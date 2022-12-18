import boto3 
# Python and Boto3 to scan table. 
table = "Grooves.query"
response = table.query(
    KeyConditionExpression=Key("SongTitle").eq("Summer Daze")
)
items = response['Items']
print(items)