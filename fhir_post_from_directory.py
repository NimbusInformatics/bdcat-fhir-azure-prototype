# Given a FHIR server, an auth token, and directory, this script finds the 
# the .json files in the directory, and posts them to the FHIR server

import requests
import sys
import json
import urllib3
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
fhir_server_uri = sys.argv[1]
token = sys.argv[2]
directory_path = sys.argv[3]

headers = {'Authorization' : "Bearer " + token, 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

# List all files in directory using pathlib
basepath = Path(directory_path)
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
	if (item.name.endswith('.json')):
		print(directory_path + '/'  + item.name)
		with open(directory_path + '/'  + item.name) as json_file:
			json_data = json.load(json_file)
			r = requests.post(fhir_server_uri, data=json.dumps(json_data), headers=headers, verify=False)
			print(r.json())



