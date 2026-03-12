# Extract, Transform and Load Process to upload Quality Outcomes Framework (QOF) data into Snowflake

This git repository uploads all downloaded QOF data files and uploads them to Snowflake. The data contains information on QOF indicators and the number of personalised care adjustments (pre 2019 called exclusions). Data is released yearly.

Raw data files can be found here: https://digital.nhs.uk/data-and-information/publications/statistical/quality-and-outcomes-framework-achievement-prevalence-and-exceptions-data 

Before running the code, save the raw CSVs named ACHIEVEMENT_XXXX.csv and ACHIEVEMENT_LONDON_XXXX.csv, depending on the fiscal year, in the data folder of this repo. Years 19/20 - 21/22 contain national data and are labelled as the first instance and the following years as the second. Then, ensure you have a relevant .env file set up and run the main.py file. 

## Changelog

### [1.0.0] - 2026-03-04
#### Added
- Initial version of the QOF repo 


## Licence
This repository is dual licensed under the [Open Government v3]([https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) & MIT. All code can outputs are subject to Crown Copyright.

## Contact
Rachel Bryant - rcahel.bryant7@nhs.net 

## Scripting Guidance
 
Please refer to the Internal Scripting Guide documentation for instructions on setting up coding projects including virtual environments (venv).
 
The Internal Scripting Guide is available here: [Internal Scripting Guide](https://nhs.sharepoint.com/:w:/r/sites/msteams_38dd8f/Shared%20Documents/Document%20Library/Documents/Git%20Integration/Internal%20Scripting%20Guide.docx?d=wc124f806fcd8401b8d8e051ce9daab87&csf=1&web=1&e=qt05xI)
