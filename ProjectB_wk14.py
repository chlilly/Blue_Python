import boto3

# boto3 AWS service
dynamodb = boto3.resource('dynamodb'),
region_name = ('us-east-1'),



table = dynamodb.create_table('online_users',
    AttributeDefinitions = [
        {
            'AttributeName': 'gamertag',
            'AttributeType': 'S'
        },
        {    
            'AttributeName': 'system',
            'AttributeType': 'S'
        },
    ],    
    TableName='online_users',
    KeySchema=[
            {
                'AttributeName': 'gamertag',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'system',
                'KeyType': 'RANGE'  # Sort key
            }
        ],

        
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)


print("Table status:", table.table_status)
