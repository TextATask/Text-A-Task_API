import json
import os
import time
from urllib import response
from decimal import Decimal
from tasks import decimalencoder
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

def all_updated_today(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    current_time_float = time.time()
    current_time = Decimal(str(current_time_float))
    
    one_day_seconds = Decimal('1') * Decimal('24') * Decimal('60') * Decimal('60')
    one_day_ago = current_time - one_day_seconds
    
    result = table.scan(FilterExpression=Attr('updatedAt').between(one_day_ago, current_time))
    
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }
    
    return response