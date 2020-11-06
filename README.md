# bdcat-fhir-azure-prototype

This repository contains helper scripts, configuration files, and sample content used evaluate the Azure API for FHIR.


## Documentation
Please see the following Google Docs for more detailed information:  
*   [Azure API for FHIR Report](https://docs.google.com/document/d/1NXHNEx8wLVJHJWPWmVXmZYhvADreVQp9yb4jGK4droM/edit?usp=sharing)
*   [FHIR on Azure - Cookbook](https://docs.google.com/document/d/1cw-BMdDtnzsMylZvANx5aXqlVDX1MV4lIfqeXmy-DIs/edit?usp=sharing)

## Helper Scripts
* [fhir_list_all_resources.py](fhir_list_all_resources.py): Lists the resources in a FHIR Server
* [fhir_post_bundle.py](fhir_post_bundle.py): Posts a bundle JSON file to a FHIR Server 
* [fhir_post_from_directory.py](fhir_post_from_directory.py): Posts JSON files to a FHIR Server that are located in the specified directory
* [fhir_transform_bundle.py](fhir_transform_bundle.py): Given a JSON FHIR bundle file with POST requests, this script transforms the POST requests into PUT requests, and handles setting the references. This was written to be used the the output of synthea-generated FHIR files, so that the ids could be retained.

## Helper Configuration Files
*   [anonymizer-configuration.json](anonymizer-configuration.json): a configuration file used by [FHIR Tools for Anonymization](https://github.com/microsoft/FHIR-Tools-for-Anonymization) to redact or alter fields in FHIR JSON files

## Sample Content

*   [bam_document_reference.json](bam_document_reference.json): an example of a DocumentReference to a BAM file, taken from https://github.com/ncpi-fhir/ncpi-model-forge/issues/23

### Synthea FHIR patients
*   [sample_covid_fhir_juvenile_patients](sample_covid_fhir_juvenile_patients/): synthetic juvenile (age 0-18) COVID patients created using [synthea](https://github.com/synthetichealth/synthea), in FHIR JSON format. The files were transformed before intake using the script [fhir_transform_bundle.py](fhir_transform_bundle.py).
*   [sample_covid_fhir_juvenile_patients_anonymized](sample_covid_fhir_juvenile_patients_anonymized/): the same patients as above, but run through the [FHIR Tools for Anonymization](https://github.com/microsoft/FHIR-Tools-for-Anonymization) using the configuration file [anonymizer-configuration.json](anonymizer-configuration.json)

### Synthea CCDA patients
* [sample_ccda_juvenile_patients/original_ccda](sample_ccda_juvenile_patients/original_ccda): synthetic juvenile (age 0-18) COVID patients created using [synthea](https://github.com/synthetichealth/synthea), in CCDA JSON format
* [sample_ccda_juvenile_patients/converted_to_fhir_json/](sample_ccda_juvenile_patients/converted_to_fhir_json/): FHIR JSON files, created using [FHIR Converter](https://github.com/microsoft/FHIR-Converter) on the original_ccda files
* [sample_ccda_juvenile_patients/anonymized_fhir_json/](sample_ccda_juvenile_patients/anonymized_fhir_json/): the same patients as above, but run through the [FHIR Tools for Anonymization](https://github.com/microsoft/FHIR-Tools-for-Anonymization) using the configuration file [anonymizer-configuration.json](anonymizer-configuration.json)

### simhospital HL7V2 patients
* [sample_hl7v2/original_hl7v2](sample_hl7v2/original_hl7v2): synthetic patients generated using [simhospital](https://github.com/google/simhospital/), in HL7 V2 format
* [sample_hl7v2/converted_fhir_json/](sample_hl7v2/converted_fhir_json/): FHIR JSON files, created using [FHIR Converter](https://github.com/microsoft/FHIR-Converter) on the original_ccda files. The files were modified after conversion to turn the Bundle "transaction" to a "batch" and changing the "POST" requests to "PUT".
* [sample_hl7v2/anonymized_fhir_json/](sample_hl7v2/anonymized_fhir_json/): the same patients as above, but run through the [FHIR Tools for Anonymization](https://github.com/microsoft/FHIR-Tools-for-Anonymization) using the configuration file [anonymizer-configuration.json](anonymizer-configuration.json)

### PFB Proof of Concept
The following files were used to show a proof of concept of a script interacting with a FHIR Server and outputting patients in PFB format. The .avro files were created using the [pypfb](https://github.com/uc-cdis/pypfb) following the [instructions](https://github.com/uc-cdis/pypfb#example-of-minimal-pfb).
* [fhir_pfb_export.py](pfb/fhir_pfb_export.py): Sends a query to a FHIR Server and returns a PFB file of the matching patients
* [minimal_file.json](pfb/minimal_file.json): The Schema in JSON format
* [minimal_schema.avro](pfb/minimal_schema.avro): The minimal PFB with Schema
* [minimal_data.avro](pfb/minimal_data.avro): The minimal PFB with Schema and Data




