import os
import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)
dynamodb = boto3.resource('dynamodb')

def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    try: 
        response = table.delete_item(
            Key={
                'id': event['pathParameters']['id']
            }
        )
            
    except ClientError as err:
        logger.error(
            "Task %s not found in table %s. Error: Code %s, Message: %s",
            event['pathParameters']['id'],
            table.name,
            err.response["Error"]["Code"],
            err.response["Error"]["Message"])
    
    response = {
        "statusCode": 200
        }
    
    return response