from operator import itemgetter
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.table('online_users')
item = {'gamertag','system'}


Item_1 = {'gamertag': 'Oldheadcity', 'system': 'Xbox', }
Item_2 = {'gamertag': 'Bigdub703', 'system': 'Xbox'}
Item_3 = {'gamertag': 'AsapBully', 'system': 'Xbox'}
Item_4 = {'gamertag': 'Babyboy23', 'system': 'Xbox'}
Item_5 = {'gamertag': 'WizKid007', 'system': 'pC'}
Item_6 = {'gamertag': 'Gatekeeper', 'system': 'PS5'}
Item_7 = {'gamertag': 'NightKing0256', 'system': 'PS5'}
Item_8 = {'gamertag': 'Hook55', 'system': 'PS5'}
Item_9 = {'gamertag': 'WolfOG', 'system': 'PC'}
Item_10 = {'gamertag': 'Champthagoat', 'system': 'PC'}

add_items = [Item_1, Item_2, Item_3, Item_4,
             Item_5, Item_6, Item_7, Item_8, Item_9, Item_10]

with table.batch_writer() as batch:
    for i in range(10):
        batch.put_item(
            Item={
                'gamertag': item['gamertag'],
                'system': item['system'],

            }
        )


items_to_delete = [Item_2, Item_10]

with table.batch_writer() as batch:
    for item in items_to_delete:
        response = batch.put_item(Item={
            "gamertag": item["gamertag"],
            "system": item["system"]}
        )
print("Table has been updated")
