These are synthetic juvenile (age 0-18) COVID patients, created using [synthea](https://github.com/synthetichealth/synthea), using the command

`java -jar synthea-with-dependencies.jar -c synthea.conf -m covid19 -a 0-18 -p 10`

The files were modified in the following way:

The Bundles were changed to be of type "batch", as the Azure API for FHIR only accepts batch Bundles.

A transform script, [fhir_transform_bundle.py](../fhir_transform_bundle.py),  was run on them to change the POST requests to PUT requests.

`curl -X POST https://<FHIR-SERVER>.azurehealthcareapis.com \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $token" \
  -d @<FHIR_BUNDLE>.json`


