import requests
import sys
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
fhir_server = sys.argv[1]
token = sys.argv[2]

headers = {"Authorization": "Bearer " + token}

def get_response_json_object(url):
	r = requests.get(url, headers=headers, verify=False)
	return r.json()

resource_types=[]
uris = []
json_obj = get_response_json_object(fhir_server + "/metadata")
for resource in json_obj['rest'][0]['resource']:
#	print(resource['type'])
	resource_types.append(resource['type'])
# print(json.dumps(json_obj, indent = 4, sort_keys=True))

for resource_type in resource_types:
#	print(resource_type)
	json_obj = get_response_json_object(fhir_server + "/" + resource_type + "?_count=25")
	print(json_obj)
	if ('entry' in json_obj):
		for entry in json_obj['entry']:
			uris.append(entry['fullUrl'])
	#	print(json.dumps(json_obj, indent = 4, sort_keys=True))

for uri in uris:
	print(uri)
#	r = requests.delete(uri, headers=headers, verify=False)
#	print(r)