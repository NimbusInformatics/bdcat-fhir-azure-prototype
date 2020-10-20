These are synthetic juvenile (age 0-18) COVID patients. This is the anonymized version fo the files in the [sample_covid_fhir_juvenile_patients](../sample_covid_fhir_juvenile_patients/) directory. They were created using 
[FHIR Tools for Anonymization] (https://github.com/microsoft/FHIR-Tools-for-Anonymization) using the configuration file [anonymizer-configuration.json](../anonymizer-configuration.json).


They were POSTed to an Azure FHIR Server using the command: 

`curl -X POST https://<FHIR-SERVER>.azurehealthcareapis.com \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $token" \
  -d @<FHIR_BUNDLE>.json`

