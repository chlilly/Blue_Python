import boto3 
# Add items to table. 
dynamodb = boto3.client('dynamodb')
# Insert data within the Item variable. 
response = dynamodb.put_item(
    
Item_1={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Smoother'}
Item_2={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Summer Daze'}
Item_3={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Nature Calls'}
Item_4={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Chillville'}
Item_5={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Recline'}
Item_6={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Chillin'}
Item_7={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Afternoon Daze'}
Item_8={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Hazy Morning'}
Item_9={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'The Cool Out'}
Item_10={'Artist': 'S': 'The Cashmere Collective','SongTitle': 'S': 'Step Away'}

    
    ReturnConsumedCapacity='TOTAL',
    TableName='Grooves',
    
     ), 


