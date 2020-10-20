These are synthetic juvenile (age 0-17) COVID patients, created using [synthea](https://github.com/synthetichealth/synthea), using the command

`java -jar synthea-with-dependencies.jar -c synthea.conf -m covid19 -a 0-18 -p 10`

The only modification to these files is that the Bundles were changed to be of type "batch", as the Azure API for FHIR only accepts batch Bundles.
They were POSTed to an Azure FHIR Server using the command: 

`curl -X POST https://<FHIR-SERVER>.azurehealthcareapis.com \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $token" \
  -d @<FHIR_BUNDLE>.json`


