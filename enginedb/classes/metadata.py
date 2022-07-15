import os, json, requests
from django.conf import settings

class ConfigurationException(Exception):
    status = 500
    message = "error"

class Metadata:
    modelViewConf = {}
    securityToken = ""
    def __init__(self, confEntry, securityToken):
        self.modelViewConf = self.GetConfigFile(confEntry)
        self.securityToken = securityToken

    def getContent(self, model, view, filters={}):
        data = {}
        content = []

        # Getting Main and Secondary model data
        entities = self.modelViewConf["entities"]
        columns = self.modelViewConf["columns"]

        mainEntity = [e for e in entities if entities[e]['reference'] == 'main'][0]
        
        for e in entities:
            data['main' if entities[e]['reference'] == 'main' else e] = self.GetDatabaseData(url=entities[e]["apiUrl"].format(**filters))

        # Adding joining functionality
        # for r in data['main']:
        #     row = {}
        content = data
            
                
            
        return content

    def GetValueFromModel(model, id):
        value = ""
        return value
    

    def GetConfigFile(self, entry):    
        with open(os.path.join(settings.BASE_DIR, f"static/conf/{entry}.json")) as conf:
            conf = json.load(conf)
        
        return conf

    def GetDatabaseData(self, url, filters = None):
        headers = {
            'Content-Type': 'application/json',
            'x-cassandra-token': self.securityToken
        }
        data = {}
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




