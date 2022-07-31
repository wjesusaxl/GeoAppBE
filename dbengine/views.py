
from django.core import serializers
from django.db import connection
from django.http import JsonResponse

from django.middleware.csrf import get_token

from django.apps import apps

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from django.conf import settings

from dbengine.classes.task import Task

from .classes.metadata import Metadata
from .classes.database import Connection

import requests, os, json


class ServiceUnavailable(APIException):
    status_code = 500
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class NotFound(APIException):
    status_code = 404
    default_detail = 'Entity not found.'
    default_code = 'entity-not-found'

class Entity(APIView):
    connection = None
    def __init__(self):
        connection = Connection

    permission_classes = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        keyspace = kwargs.get('keyspace')
        entity = kwargs.get('entity')
        action = kwargs.get('action')

        conf = getConfigFile('api/url')
        geodb = conf['geodb']
        geodb['entity'] = entity

        url = f"https://{geodb['dbID']}-{geodb['dbRegion']}.apps.astra.datastax.com/api/rest/v2/keyspaces/{keyspace}/{geodb['entity']}/rows"

        response = requests.get(url, headers={"x-cassandra-token": f"{geodb['dbApplicationToken']}"})
        
        if not response.status_code == 200:            
            statusCode = response.status_code
            if statusCode == 400:
                raise NotFound
            if statusCode == 404:
                raise NotFound
            if statusCode == 500:
                raise ServiceUnavailable

        data = json.loads(response.text)
        
        return JsonResponse(data, safe=False)
    
    permission_classes = (IsAuthenticated, )
    def post(self, request, *args, **kwargs):
        
        keyspace = kwargs.ge('keyspace')
        entity = kwargs.get('entity')
        id = kwargs.get('id')
        action = request.POST.get("action")

        # conf = getConfigFile('api/url')
        # geodb = conf['geodb']
        # geodb['entity'] = entity

        # url = f"https://{geodb['dbID']}-{geodb['dbRegion']}.apps.astra.datastax.com/api/rest/v2/keyspaces/{geodb['dbKeyspace']}/{geodb['entity']}"

        data = json.loads(request.body)

        # result = []

        # for item in data:
        #     response = requests.post(url, json=item, headers={"x-cassandra-token": f"{geodb['dbApplicationToken']}"})
        #     status = response.status_code
        #     result.append( {
        #         "id": item["id"],
        #         "status": status,
        #         "response": json.loads(response.text)
        #     })
        if action == "only-update":
            result = self.connection.updateData(keyspace, entity, data, id)
        else:
            result = connection.upsertData(keyspace, entity, data)

        return JsonResponse(result, safe=False)

    
    permission_classes = (IsAuthenticated, )
    def put(self, request, *args, **kwargs):

        entity = kwargs.get('entity')
        data = json.loads(request.body)
        result = self.connection.upsertData(entity, data, onlyUpdate=True)

        return JsonResponse(result, safe=False)


class Synchronization(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request, *args, **kwargs):

        conf = getConfigFile('engine/models')
        models = json.loads(request.body)["models"]

        source = kwargs.get("from")
        if not models:
            raise ServiceUnavailable

        if source == "local":
            result = {}
            for m in models:
                model = conf["local"][m]
                appModel = apps.get_model(model["app"], m)
                fields = model["fields"]
                rawData = json.loads(serializers.serialize('json', appModel.objects.all()))
                
                data = connection.filterDataset(rawData, fields)
                result[m] = connection.upsertData(model["keyspace"], model["extModel"], data)
        
        return JsonResponse(result, safe=False)

class DataProvider(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        model = kwargs.get("model"),
        view = kwargs.get("view")

        conf = getConfigFile('api/url')
        geodb = conf['geodb']

        metadata = Metadata("dbengine/metadata", geodb["dbApplicationToken"])
        conf = metadata.getContent(model, view, dict(request.GET.items()))
        return JsonResponse(conf, safe=False)

class TaskAPI(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, *args, **kwargs):
        object = kwargs.get("object")
        action = kwargs.get("action")
        objectName = kwargs.get("objectName")

        task = Task()        
        body = task.process(objectType=object, action=action, objectName=objectName)
        # if (action + '-' + object) == 'drop-datatype':
        #     result = conn.dropDataType(body['keyspace'])

        

        return JsonResponse(body, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def getCSRFToken(request):
    data = {
        "csrf": get_token(request)
    } 
    return JsonResponse(data)

def getConfigFile(entry):    
    with open(os.path.join(settings.BASE_DIR, f"static/conf/{entry}.json")) as conf:
        conf = json.load(conf)
    
    return conf

