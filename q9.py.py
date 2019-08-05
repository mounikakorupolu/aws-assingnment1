import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Creating the DynamoDB table.

table = dynamodb.create_table(    #table is the response for the create_table
    TableName='Games',            #tablename must be unique in a region..i have used table name as Hello.
    KeySchema=[
        {
            'AttributeName': 'gname',     #hash attribute (a partition key)
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'gid',       #range attribute (a sort key)
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'gname',
            'AttributeType': 'S'          # S refers string type
        },
        {
            'AttributeName': 'gid',
            'AttributeType': 'N'          # N refers number type
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='Games')       # Wait until the table exists.
.
print(table.item_count)          # Printing the no. of items in the table

                                 #if result=0 then it meant creation of table is success and there is no content

print('Table has been created, continuing to insert data.')


table.put_item(
   Item={
           'gname': 'chess',
         'gid': 1,
        'publisher': 'Mounika',
        'rating': '10',
        'release_date': '04-08-2019',
        'genres': ['concentration' , 'focus']

    }                                                            #items are loaded into table 'Games'
)


table.put_item(
   Item={
           'gname': 'bussinessgame',
           'gid': 2,
        'publisher': 'Manasa',
        'rating': '10',
        'release_date': '03-08-2019',
        'genres': ['enjoy' , 'fun']

    }                                                           #items are loaded into table 'Games'
)
                                                          #items are loaded into table 'Games'
)




