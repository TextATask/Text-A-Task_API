import json
import time
import logging
import os
from decimal import Decimal
from tasks import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def complete(event, context):

    current_time_float = time.time()
    timestamp = Decimal(str(current_time_float))

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeValues={
          ':updatedAt': timestamp,
        },
        
        UpdateExpression='SET updatedAt = :updatedAt REMOVE incomplete',
        ReturnValues='ALL_NEW',
    )

    
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response