import requests
import json
import mimetypes
import io

class GravityAIInferenceSDK:
    
    API_URL="https://on-demand.gravity-ai.com/"
    API_CREATE_JOB_URL = API_URL + 'api/v1/jobs'
    API_GET_JOB_RESULT_URL = API_URL + 'api/v1/jobs/result-link'
    outFilePath="out"

    def __init__(self, api_key):
        self.api_key = api_key
        self.request_headers = {
            'x-api-key': self.api_key
        }
    
    # Function to get latest jobs
    def get_latest_jobs(self):

        url = self.API_CREATE_JOB_URL + "/latest"
        r=requests.request("GET",url, headers=self.request_headers)
        
        if(r.status_code!=200):
            print('Error: '+ str(r.status_code))
            print("Error Message: "+ r.reason)
        else:
            d1=r.json()
            s1 = json.dumps(d1)
            d2 = json.loads(s1)
            print(json.dumps(d2, indent=4))
        
    # Post a new job with parameters
    def postJob(self, inputFilePath,name=None,version=None,mimetype=None):

        # set name, version, and mimetype
        if name!=None:
            jobname=name
        else:
            jobname=inputFilePath
        
        jobversion=version
    
        if mimetype!=None:
            jobmimetype=mimetype
        else:
            jobmimetype=mimetypes.guess_type(inputFilePath)[0]
        
        self.config = {
            "version": jobversion,
            "mimeType": jobmimetype,
            "jobName": jobname,
            "mapping": None,
            "outputMapping": None,
            "data": None,
            "groupId": None,
            "isGrouped":False,
            "versionId":None,
            "containerId":None
        }

        inputFile = open(inputFilePath, 'rb')
        files = {
            "file": inputFile
        }
        data = {
            'data': json.dumps(self.config)
        }

        r = requests.request("POST", self.API_CREATE_JOB_URL, headers=self.request_headers, data=data, files=files)

        if r.status_code!=200:
             print("Error: "+ str(r.status_code))
             print("Error Message: "+ r.reason)
             print("Also please check version number and mimetype. Keep these blank if you are not sure.")
        else:
            result = r.json()
            if result.get("isError", False):
                print("Error: " + result.get("errorMessage", ""))
                raise Exception("Error: " + result.get("errorMessage", ""))
            else:
                return result["data"]["id"]
               
    def downloadResultWithOutPath(self, jobId, outFilePath):
        url = self.API_GET_JOB_RESULT_URL + "/" + jobId
        r = requests.request("GET", url, headers=self.request_headers)
        if r.status_code!=200:
             print("Error Message:  "+ r.reason)
        else:
            link = r.json()
            if link.get("isError", False):
                print("Error: " + link.get("errorMessage", ""))
                raise Exception("Error: " + link.get("errorMessage", ""))
            else:
                result = requests.request("GET", link["data"])
                open(outFilePath, 'wb').write(result.content)
            
    # post job and get result file named outfile
    def getPostResult(self,inputFilePath,name=None,version=None,mimetype=None):
        jobid=self.postJob(inputFilePath,name,version,mimetype)
        print("Get your result in outfile!")
        self.downloadResultWithOutPath(jobid,"outfile")
    
    # returns job result directly
    def getJobResult(self,jobId):
        url = self.API_GET_JOB_RESULT_URL + "/" + jobId
        r = requests.request("GET", url, headers=self.request_headers)
        
        if r.status_code!=200:
             print("Error code: "+ str(r.status_code))
             print("Error Message "+ r.reason)
        else:
            link = r.json()
            if link.get("isError", False):
                print("Error: " + link.get("errorMessage", ""))
                raise Exception("Error: " + link.get("errorMessage", ""))
            else:
                result = requests.request("GET", link["data"])
                return result.content
            
    # Provide string data and post job
    def PostJobWithStringData(self,data):

        file1=io.StringIO(data)
        
        #set config
        self.config = {
            "version": None,
            "mimeType": "text/plain",
            "name": None,
            "mapping": None,
            "outputMapping": None,
            "data": None,
            "groupId": None,
            "isGrouped":False,
            "versionId":None,
            "containerId":None
        }
       
        files = {
            "file": file1
        }

        data = {
            'data': json.dumps(self.config)
        }

        r = requests.request("POST", self.API_CREATE_JOB_URL, headers=self.request_headers, data=data, files=files)

        if r.status_code!=200:
             print("Error: "+ str(r.status_code))
             print("Error Message: "+ r.reason)
        else:
            result = r.json()
            print(result)
            if result.get("isError", False):
                print("Error: " + result.get("errorMessage", ""))
                raise Exception("Error: " + result.get("errorMessage", ""))
            else:
                return result["data"]["id"]

    # Provide image data and post job
    def PostJobWithBinaryData(self,content,mimetype):
        
        print('in zip')
        file_like_object = io.BytesIO(content)
        print(file_like_object)
        
        with open('test.zip', 'wb') as f:
            f.write(file_like_object.getvalue())

        self.config = {
            "version": None,
            "mimeType": mimetype,
            "name": None,
            "mapping": None,
            "outputMapping": None,
            "data": None,
            "groupId": None,
            "isGrouped":False,
            "versionId":None,
            "containerId":None
        }
       
        files = {
            "file": file_like_object
        }

        data = {
            'data': json.dumps(self.config)
        }

        r = requests.request("POST", self.API_CREATE_JOB_URL, headers=self.request_headers, data=data, files=files)

        if r.status_code!=200:
             print("Error: "+ str(r.status_code))
             print("Error Message: "+ r.reason)
        else:
            result = r.json()
            print(result)
            if result.get("isError", False):
                print("Error: " + result.get("errorMessage", ""))
                raise Exception("Error: " + result.get("errorMessage", ""))
            else:
                return result["data"]["id"]
    
    # Provide image data and post job
    def PostJobWithImageData(self,content):

        buf = io.BytesIO()
        content.save(buf, format='PNG')
        data = buf.getvalue()
        
        self.config = {
            "version": None,
            "mimeType": "image/png",
            "name": None,
            "mapping": None,
            "outputMapping": None,
            "data": None,
            "groupId": None,
            "isGrouped":False,
            "versionId":None,
            "containerId":None
        }
        # Post a new job (file) to the API
        #inputFile = open(inputFilePath, 'rb')
        files = {
            "file": data
        }

        data = {
            'data': json.dumps(self.config)
        }

        r = requests.request("POST", self.API_CREATE_JOB_URL, headers=self.request_headers, data=data, files=files)

        if r.status_code!=200:
             print("Error: "+ str(r.status_code))
             print("Error Message: "+ r.reason)
        else:
            result = r.json()
            print(result)
            if result.get("isError", False):
                print("Error: " + result.get("errorMessage", ""))
                raise Exception("Error: " + result.get("errorMessage", ""))
            else:
                return result["data"]["id"]
    
            
    # Provide Json data and post job
    def PostJobWithJsonData(self,data):

        json_data=json.dumps(data)
        #set config
        self.config = {
            "version": None,
            "mimeType": "application/json",
            "name": None,
            "mapping": None,
            "outputMapping": None,
            "data": None,
            "groupId": None,
            "isGrouped":False,
            "versionId":None,
            "containerId":None
        }
        
        files = {
            "file": json_data
        }

        data = {
            'data': json.dumps(self.config)
        }

        r = requests.request("POST", self.API_CREATE_JOB_URL, headers=self.request_headers, data=data, files=files)

        if r.status_code!=200:
             print("Error: "+ str(r.status_code))
             print("Error Message: "+ r.reason)
        else:
            result = r.json()
            print(result)
            if result.get("isError", False):
                print("Error: " + result.get("errorMessage", ""))
                raise Exception("Error: " + result.get("errorMessage", ""))
            else:
                return result["data"]["id"]
    
            
    def changeJobName(self,API_KEY,jobId,jobName):
        request_headers = {
            'x-api-key': API_KEY,
            'Content-Type': "application/json"
        }

        url = self.API_CREATE_JOB_URL + "/" + jobId
        #set config
        self.config = {
            "name": jobName
        }

        r = requests.request("PUT", url, headers=request_headers, data=json.dumps(self.config))
        
        if(r.status_code!=200):
            print('Error: '+ str(r.status_code))
            print("Error Message: "+ r.reason)
        else:
            result = r.json()
            if(result["data"]!=None):
                if(result["data"].get("name")==jobName):
                    print(" Job name changed Suceessfully!") 
            else:
                print(" Unable to change job name!")   
    