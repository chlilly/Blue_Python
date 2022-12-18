import boto3 

dynamodb = boto3.client('dynamodb')
# Insert data within the Item_3 variable. 
response = dynamodb.put_item(
    
    Item_1={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Smoother'}
	Item_2={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Summer Daze'}
	Item_3={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Chillin'}
	Item_6={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Afternoon Daze'}
	Item_7={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Hazy Morning'}
	Item_8={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'The Cool Out'}
	Item_9={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Step Away'}
	Item_10={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Bliss'}
    
    ReturnConsumedCapacity='TOTAL',
    TableName='Grooves',
    
    ), 


