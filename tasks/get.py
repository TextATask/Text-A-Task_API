import os
import json
import logging
from tasks import decimalencoder
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
dynamodb = boto3.resource('dynamodb')

def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    try: 
        result = table.get_item(
            Key={
                'id': event['pathParameters']['id']
            }
        )
    except ClientError as err:
        logger.error(
            "Task % not found in table %. Error: Code %, Message %",
            event['pathParameters']['id'],
            table.name,
            err.response["Error"]["Code"],
            err.response["Error"]["Message"])
    
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
        }
    
    return response