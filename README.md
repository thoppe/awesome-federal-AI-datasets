# Awesome Federal AI datasets

A list of high quality accessible datasets for training AI from the US Federal government.

Our primary aim is to provide a convenient platform for discovering these datasets, ensuring their accessibility, and upholding a standard of quality, as defined by rigorous criteria. The datasets are organized based on their respective originating Department or independent agency.


| Status| Dept. | Agency  | Title |
| ----  | ----  | ----    | ----- |
 | [:green_circle:](data/datasets/HHS_NIH_clinical-trials.yaml) | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [Clinical Trials](https://classic.clinicaltrials.gov/ct2/resources/download) | 
 | [:green_circle:](data/datasets/HHS_NIH_bibliometric-publication-citation-graph-links.yaml) | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [Bibliometric publication citation graph links](https://icite.od.nih.gov/api) | 
 | [:green_circle:](data/datasets/HHS_CDC_vaccine-adverse-event-reporting-system-vaers.yaml) | [HHS](https://www.hhs.gov/) | [CDC](https://www.cdc.gov/) | [Vaccine Adverse Event Reporting System (VAERS)](https://vaers.hhs.gov/data/datasets.html) | 
 | [:green_circle:](data/datasets/HHS_CDC_covid-19-case-surveillance-public-use-data-with-geography.yaml) | [HHS](https://www.hhs.gov/) | [CDC](https://www.cdc.gov/) | [COVID-19 Case Surveillance Public Use Data with Geography](https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4) | 
 | [:green_circle:](data/datasets/Legislative_GPO_us-federal-register.yaml) | [Legislative](https://www.congress.gov/) | [GPO](https://www.gpo.gov/) | [US Federal Register](https://www.govinfo.gov/bulkdata/FR) | 
 | [:green_circle:](data/datasets/HHS_NIH_pubmed-biomedical-publication-abstract.yaml) | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [PubMed: Biomedical publication abstract](https://pubmed.ncbi.nlm.nih.gov/download/) | 
 | [:green_circle:](data/datasets/HHS_NIH_pubmed-central-full-text-biomedical-publications.yaml) | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [PubMed Central: Full text biomedical publications](https://www.ncbi.nlm.nih.gov/pmc/tools/ftp/) | 
 | [:green_circle:](data/datasets/HHS_NIH_exporter-nih-grant-funding.yaml) | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [ExPORTER: NIH Grant funding](https://reporter.nih.gov/exporter) | 
 | [:green_circle:](data/datasets/HHS_FDA_drug-adverse-events-device-adverse-events-animal-veterinary-adverse-events.yaml) | [HHS](https://www.hhs.gov/) | [FDA](https://www.fda.gov/) | [Drug Adverse Events, Device Adverse Events, Animal & Veterinary Adverse Events](https://open.fda.gov/data/downloads/) | 
 | [:green_circle:](data/datasets/HHS_CMS_open-payments-dataset-downloads.yaml) | [HHS](https://www.hhs.gov/) | [CMS](https://www.cms.gov/) | [Open Payments Dataset Downloads](https://www.cms.gov/OpenPayments/Data/Dataset-Downloads) | 
 | [:green_circle:](data/datasets/DOC_USPTO_us-trademarks-filings-and-registration-images.yaml) | [DOC](https://www.commerce.gov/) | [USPTO](https://www.uspto.gov/) | [US Trademarks: Filings and registration images](https://bulkdata.uspto.gov/) | 
 | [:green_circle:](data/datasets/DOC_USPTO_us-patents-full-text-and-images.yaml) | [DOC](https://www.commerce.gov/) | [USPTO](https://www.uspto.gov/) | [US Patents: full text and images](https://bulkdata.uspto.gov/) | 
 | [:red_circle:](data/datasets/GSA__regulations-gov-federal-rulemaking-process.yaml) | [GSA](https://www.gsa.gov/) | []() | [Regulations.gov, Federal rulemaking process](https://www.regulations.gov/bulkdownload) | 
 | [:red_circle:](data/datasets/DOJ_NSD_foreign-agents-registration-act-registrants-and-pdfs.yaml) | [DOJ](https://www.justice.gov/) | [NSD](https://www.justice.gov/nsd) | [Foreign Agents Registration Act : Registrants and PDFs](https://efile.fara.gov/ords/fara/f?p=API:BULKDATA) | 
 | [:question:](data/datasets/DOC_NOAA_weather-and-climate-quick-links-national-centers-for-environmental-information.yaml) | [DOC](https://www.commerce.gov/) | [NOAA](https://www.noaa.gov/) | [Weather and Climate Quick Links : National Centers for Environmental Information](https://www.ncei.noaa.gov/weather-climate-links) | 

## Development of AI Ready

Questions and scores for the AI dataset can be found at [AI_ready_questions.yaml](src/AI_ready_questions.yaml)

## Development

Built with :purple_heart: by [@metasemantic](https://twitter.com/metasemantic).
Code is linted by [black](https://github.com/psf/black) and conforms to standards by [flake8](https://github.com/PyCQA/flake8).
New projects should be added to [data/datasets.yaml](data/datasets.yaml), run `make build`, and submit a PR.