import json
import logging
import os
import time

import boto3
dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event["body"])
    if 'body' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the task item.")
    
    timestamp = str(time.time())
    
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    item = {
        'id': os.environ['PHONE_NUMBER'],
        'text': data['body']['text'],
        'complete': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
        }
    
    table.put_item(Item=item)
    
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
        }
    
    return response