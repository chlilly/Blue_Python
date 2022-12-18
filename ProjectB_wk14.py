import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(

     KeySchema=[
            {"AttributeName": "Album", "KeyType": "HASH"},
            {"AttributeName": "SongTitle", "KeyType": "RANGE"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "Album", "AttributeType": "S"},
            {"AttributeName": "SongTitle", "AttributeType": "S"},
        ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10,
    },
    TableName='Grooves'

),

print(table)
