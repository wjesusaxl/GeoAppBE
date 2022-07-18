import os, json, requests
from django.conf import settings

class DBObject:
    dmlApi = securityConf = {}    
    keyspace = ""
    def __init__(self, keyspace):
        self.dmlApi = self.__getConfigFile("api/dml")["v2"]
        self.securityConf = self.__getConfigFile("api/database")
        self.keyspace = keyspace

    def __getConfigFile(self, entry):    
        with open(os.path.join(settings.BASE_DIR, f"static/conf/{entry}.json")) as conf:
            conf = json.load(conf)
        
        return conf

    def callDmlApi(self, objectType, action, body = None, params={}):        
        basePath = self.dmlApi["apiBasePath"]        
        objectConf = self.dmlApi[objectType][action]        

        apiMethod = objectConf["method"]
        apiUrl = basePath + objectConf["url"]

        params['keyspace'] = self.keyspace
        params["astraClusterId"] = self.securityConf["astraClusterId"]
        params["astraRegion"] = self.securityConf["astraRegion"]

        if apiMethod == "DELETE":
            data = self.delete(apiUrl.format(**params))

        if apiMethod == "POST":
            data = self.post(apiUrl.format(**params), body)

        return data

    def delete(self, url):
        data = { }        
        response = requests.delete(
            url=url,
            headers={
                "x-cassandra-token": self.securityConf["dbApplicationToken"]
            }
        )
        statusCode = response.status_code
        data["ok"] = response.ok
        if statusCode == 204:
            data = {
                "ok": True,
            }
        else:
            data["code"] = statusCode
            data["reason"] = response.reason
            data["msg"] = json.loads(response.text)

        return data
    
    def post(self, url, body):
        data = { }                
        response = requests.post(
            url=url,
            headers={
                "x-cassandra-token": self.securityConf["dbApplicationToken"]
            },
            json=body
        )
        statusCode = response.status_code
        data["ok"] = response.ok
        data["status"] = statusCode
        if not statusCode == 201:            
            data["code"] = statusCode
            data["reason"] = response.reason
            data["msg"] = response.text

        return data

