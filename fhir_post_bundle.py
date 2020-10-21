import requests
import sys
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
fhir_server_uri = sys.argv[1]
token = sys.argv[2]
json_file_path = sys.argv[3]

headers = {'Authorization' : "Bearer " + token, 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

with open(json_file_path) as json_file:
    json_data = json.load(json_file)


r = requests.post(fhir_server_uri, data=json.dumps(json_data), headers=headers, verify=False)
print(r.json())
