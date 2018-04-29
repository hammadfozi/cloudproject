from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import boto3
import decimal

# Create your views here.


def index(request):
    dynamo_increase()
    return HttpResponse("<h1>This is the custom app homepage</h1>")


def dynamo_increase():
    DYNAMO_ENDPOINT = getattr(settings, "DYNAMO_ENDPOINT", None)
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url=DYNAMO_ENDPOINT)
    view_table = dynamodb.Table('dummz')
    response = view_table.update_item(
    Key={
    'id': 1
    },
    UpdateExpression="set hits = hits + :val",
    ExpressionAttributeValues={
    ':val': 1 #decimal.Decimal(1)
    },
    ReturnValues="UPDATED_NEW"
    )

