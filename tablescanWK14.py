import boto3 
table = "Grooves.query"
response = table.query(
    KeyConditionExpression=Key("SongTitle").eq("Summer Daze")
)
items = response['Items']
print(items)