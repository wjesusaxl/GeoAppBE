
from django.core import serializers
from django.http import JsonResponse

from django.middleware.csrf import get_token

from django.apps import apps

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from django.conf import settings

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
            result = updateData(keyspace, entity, data, id)
        else:
            result = upsertData(keyspace, entity, data)

        return JsonResponse(result, safe=False)

    
    permission_classes = (IsAuthenticated, )
    def put(sel, request, *args, **kwargs):

        entity = kwargs.get('entity')
        data = json.loads(request.body)
        result = upsertData(entity, data, onlyUpdate=True)

        return JsonResponse(result, safe=False)


class Synchronization(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request, *args, **kwargs):

        conf = getConfigFile('enginedb/models')
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
                
                data = FilterDataset(rawData, fields)
                result[m] = upsertData(model["keyspace"], model["extModel"], data)
        
        return JsonResponse(result, safe=False)


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

def FilterDataset(data, fields):
    dataset = []                
    for r in data:
        o = {}
        row = r["fields"]
        for f in fields:
            o[fields[f]] = row[f]
        dataset.append(o)
    return dataset

def upsertData(keyspace, entity, data):
    conf = getConfigFile('api/url')
    geodb = conf['geodb']
    url = f"https://{geodb['dbID']}-{geodb['dbRegion']}.apps.astra.datastax.com/api/rest/v2/keyspaces/{keyspace}/{entity}"
    result = []

    for item in data:
        response = requests.post(url, json=item, headers={"x-cassandra-token": f"{geodb['dbApplicationToken']}"})
        status = response.status_code
        result.append( {
            "id": item["id"],
            "status": status,
            "response": json.loads(response.text)
        })

    return result

def updateData(keyspace, entity, data, id):
    conf = getConfigFile('api/url')
    geodb = conf['geodb']
    url = f"https://{geodb['dbID']}-{geodb['dbRegion']}.apps.astra.datastax.com/api/rest/v2/keyspaces/{keyspace}/{entity}/" + '/{id}'
    result = []

    for item in data:
        response = requests.put(url, json=item, headers={"x-cassandra-token": f"{geodb['dbApplicationToken']}"})
        status = response.status_code
        result.append( {
            "id": item["id"],
            "status": status,
            "response": json.loads(response.text)
        })

    return result
