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
        response = table.query(
            TableName="Text-A-Task-API-dev1",
            IndexName="id",
            KeyConditionExpression=event['pathParameters']['id'])
            
    except ClientError as err:
        logger.error(
            "Task %s not found in table %s. Error: Code %s, Message: %s",
            event['pathParameters']['id'],
            table.name,
            err.response["Error"]["Code"],
            err.response["Error"]["Message"])
    
    response = {
        "statusCode": 200,
        "body": json.dumps(response['Item'],
                           cls=decimalencoder.DecimalEncoder)
        }
    
    return response