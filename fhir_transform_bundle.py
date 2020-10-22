# Given a .json fhir bundle file with POST requests, this script transforms
# the POST requests into PUT requests, and handles setting the references. 
# This was written to be used the the output of synthea-generated FHIR files.

import sys
import json
    
json_file_path = sys.argv[1]
ids = {}

with open(json_file_path) as json_file:
    json_data = json.load(json_file)

for entry in json_data['entry']:
	id = entry['resource']['id']
	entry['request']['method'] = "PUT"
	entry['request']['url'] = entry['request']['url'] + '/' + id
	ids[entry['fullUrl']] = entry['request']['url']

	if ('patient' in entry['resource']):
		reference = entry['resource']['patient']['reference']
		if (reference in ids):
			entry['resource']['patient']['reference'] = ids[reference]

	if ('encounter' in entry['resource']):
		reference = entry['resource']['encounter']['reference']
		if (reference in ids):
			entry['resource']['encounter']['reference'] = ids[reference]

	if ('subject' in entry['resource']):
		reference = entry['resource']['subject']['reference']
		if (reference in ids):
			entry['resource']['subject']['reference'] = ids[reference]

	if ('serviceProvider' in entry['resource']):
		reference = entry['resource']['serviceProvider']['reference']
		if (reference in ids):
			entry['resource']['serviceProvider']['reference'] = ids[reference]

	if ('provider' in entry['resource']):
		reference = entry['resource']['provider']['reference']
		if (reference in ids):
			entry['resource']['provider']['reference'] = ids[reference]

	if ('claim' in entry['resource']):
		reference = entry['resource']['claim']['reference']
		if (reference in ids):
			entry['resource']['claim']['reference'] = ids[reference]

	if ('managingOrganization' in entry['resource']):
		for managingOrganization in entry['resource']['managingOrganization']:
			reference = managingOrganization['reference']
			if (reference in ids):
				managingOrganization['reference'] = ids[reference]

	if ('careTeam' in entry['resource']):
		for careTeam in entry['resource']['careTeam']:
			if ('provider' in careTeam):
				reference = careTeam['provider']['reference']
				if (reference in ids):
					careTeam['provider']['reference'] = ids[reference]
			if ('reference' in careTeam):
				reference = careTeam['reference']
				if (reference in ids):
					careTeam['reference'] = ids[reference]

	if ('addresses' in entry['resource']):
		for address in entry['resource']['addresses']:
			if ('reference' in address):
				reference = address['reference']
				if (reference in ids):
					address['reference'] = ids[reference]

	if ('participant' in entry['resource']):
		for participant in entry['resource']['participant']:
			if ('individual' in participant):
				reference = participant['individual']['reference']
				if (reference in ids):
					participant['individual']['reference'] = ids[reference]
			if ('member' in participant):
				reference = participant['member']['reference']
				if (reference in ids):
					participant['member']['reference'] = ids[reference]
					
	if ('contained' in entry['resource']):
		for contained in entry['resource']['contained']:
			if ('subject' in contained):
				reference = contained['subject']['reference']
				if (reference in ids):
					contained['subject']['reference'] = ids[reference]
			if ('requester' in contained):
				reference = contained['requester']['reference']
				if (reference in ids):
					contained['requester']['reference'] = ids[reference]
			if ('performer' in contained):
				for performer in contained['performer']:
					reference = performer['reference']
					if (reference in ids):
						performer['reference'] = ids[reference]
			if ('beneficiary' in contained):
				reference = contained['beneficiary']['reference']
				if (reference in ids):
					contained['beneficiary']['reference'] = ids[reference]
		
	if ('supportingInfo' in entry['resource']):
		for supportingInfo in entry['resource']['supportingInfo']:
			if ('valueReference' in supportingInfo):
				reference = supportingInfo['valueReference']['reference']
				if (reference in ids):
					supportingInfo['valueReference']['reference'] = ids[reference]

	if ('item' in entry['resource']):
		for item in entry['resource']['item']:
			if ('encounter' in item):
				for encounter in item['encounter']:
					reference = encounter['reference']
					if (reference in ids):
						encounter['reference'] = ids[reference]

	if ('reasonReference' in entry['resource']):
		for reasonReference in entry['resource']['reasonReference']:
			reference = reasonReference['reference']
			if (reference in ids):
				reasonReference['reference'] = ids[reference]

	if ('result' in entry['resource']):
		for result in entry['resource']['result']:
			reference = result['reference']
			if (reference in ids):
				result['reference'] = ids[reference]


	if ('diagnosis' in entry['resource']):
		for diagnosis in entry['resource']['diagnosis']:
			reference = diagnosis['diagnosisReference']['reference']
			if (reference in ids):
				diagnosis['diagnosisReference']['reference'] = ids[reference]

	if ('procedure' in entry['resource']):
		for procedure in entry['resource']['procedure']:
			reference = procedure['procedureReference']['reference']
			if (reference in ids):
				procedure['procedureReference']['reference'] = ids[reference]


print(json.dumps(json_data, indent = 4))