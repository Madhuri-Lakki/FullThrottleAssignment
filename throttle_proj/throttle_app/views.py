from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view, renderer_classes, parser_classes
from throttle_app.models import User
from throttle_app.models import ActivityPeriod
from throttle_app.Database import Database
from throttle_app.InsertData import InsertThrottleData
from rest_framework.parsers import JSONParser
import json
from throttle_app import models
import mysql.connector
# Create your views here.


@api_view(['POST'])
@parser_classes([JSONParser])
def Throttledataposts(request):

    input = request.data

    info = input['members']

    for case in info:

        print(case['activity_periods'])

        ob1 = InsertThrottleData(case)
        res1 = ob1.insertuserdata()
        ##totaldata = ob1.insertactivitydata()

    return HttpResponse(res1)

