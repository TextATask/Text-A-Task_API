import json
import os

from tasks import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

def all_incomplete(event, context):
  table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

  result = table.query(IndexName= "incompleteTasks",
                       ExpressionAttributeValues={},
                       KeyConditionExpression='attribute_exists(incomplete)'),

  response = {
    "statusCode": 200,
    "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
  }
  
  return response

