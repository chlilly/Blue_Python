import boto3

dynamodb = boto3.resource(
    'dynamodb', 
    region_name='us-east-1',
    aws_access_key_id='',
    aws_secret_access_key='')

table = dynamodb.create_table(
    TableName='online_users',
    KeySchema=[
        {
            'AttributeName': 'gamertag',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'system',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'gamertag',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'system',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)



print("Table status:", table.table_status)
