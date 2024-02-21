import json
import time
import logging
import os

from tasks import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def complete(event, context):
    data = json.loads(event['body'])
    if 'id' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the task item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeValues={
          ':incomplete': None,
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET incomplete = :incomplete, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response