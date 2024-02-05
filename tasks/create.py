import json
import logging
import os
import time
import uuid
import random
import boto3

dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event["body"])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the task item.")
    
    timestamp = str(time.time())
    
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    new_id = str(random.randint(1, 899999) + 100000)
    
    item = {
        'id': new_id,
        'text': data['text'],
        'incomplete': timestamp,
        'updatedAt': timestamp,
        'createdAt': timestamp
        }
    
    table.put_item(Item=item)
    
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
        }
    
    return response