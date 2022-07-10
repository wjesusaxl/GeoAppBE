import os, json, requests
from django.conf import settings

class ConfigurationException(Exception):
    status = 500
    message = "error"

class Metadata:
    modelViewConf = {}
    def __init__(self, confEntry, securityToken):
        self.modelViewConf = self.getConfigFile(confEntry)
        self.securityToken = securityToken

    def getContent(self, model, view):

        models2 = self.getSecondaryModels()
        data = {
            "models2": models2
        }

        return data

    def getSecondaryModels(self):
        data = {}
        entities = self.modelViewConf["entities"]
        secondaryEntities = [e for e in entities if entities[e]["reference"] == "secondary"]
        try:

            if not secondaryEntities:
                raise ConfigurationException()

            for e in secondaryEntities:
                entity = entities[e]
                data[e] = self.GetDatabaseData(url=entity["apiUrl"])

        except ConfigurationException as ex:
            data = {
                "message": ex
            }

        return data

    def getConfigFile(self, entry):    
        with open(os.path.join(settings.BASE_DIR, f"static/conf/{entry}.json")) as conf:
            conf = json.load(conf)
        
        return conf

    def GetDatabaseData(self, url, filters = None):
        headers = {
            'Content-Type': 'application/json',
            'x-cassandra-token': self.securityToken
        }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            data = data["data"]


        return data


# def test_view (request):
#    try:
#        # Some code .... 
#        status = 200
#        msg = 'Everything is ok.'
#        if my_business_logic_is_violated():
#            raise MyPreconditionException()
#    except MyPreconditionException as e:
#        # Here we're handling client side errors, and hence we return
#        # status codes in the 4XX range
#        status = 428
#        msg = 'Precondition not met.'
#    except MyServerException as e:
#        # Here, we assume that exceptions raised are because of server
#        # errors and hence we return status codes in the 5XX range
#        status = 500
#        msg = 'Server error, yo.'
#    finally:
#        # Here we return the response to the client, regardless of whether
#        # it was created in the try or the except block
#        return JsonResponse({'message': msg}, status=status)