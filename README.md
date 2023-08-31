# Awesome Federal AI datasets

A list of high quality accessible datasets for training AI from the US Federal government.

Our primary aim is to provide a convenient platform for discovering these datasets, ensuring their accessibility, and upholding a standard of quality, as defined by rigorous criteria. The datasets are organized based on their respective originating Department or independent agency.


| Dept. | Agency  | Title |
| ----  | ----    | ----  |
 | [DOC](https://www.commerce.gov/) | [NOAA](https://www.noaa.gov/) | [Weather and Climate Quick Links : National Centers for Environmental Information](https://www.ncei.noaa.gov/weather-climate-links) | 
 | [DOC](https://www.commerce.gov/) | [USPTO](https://www.uspto.gov/) | [US Patents: full text and images](https://bulkdata.uspto.gov/) | 
 | [DOC](https://www.commerce.gov/) | [USPTO](https://www.uspto.gov/) | [US Trademarks: Filings and registration images](https://bulkdata.uspto.gov/) | 
 | [DOJ](https://www.justice.gov/) | [NSD](https://www.justice.gov/nsd) | [Foreign Agents Registration Act : Registrants and PDFs](https://efile.fara.gov/ords/fara/f?p=API:BULKDATA) | 
 | [GSA](https://www.gsa.gov/) | []() | [Regulations.gov, Federal rulemaking process](https://www.regulations.gov/bulkdownload) | 
 | [HHS](https://www.hhs.gov/) | [CDC](https://www.cdc.gov/) | [COVID-19 Case Surveillance Public Use Data with Geography](https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4) | 
 | [HHS](https://www.hhs.gov/) | [CDC](https://www.cdc.gov/) | [Vaccine Adverse Event Reporting System (VAERS)](https://vaers.hhs.gov/data/datasets.html) | 
 | [HHS](https://www.hhs.gov/) | [CMS](https://www.cms.gov/) | [Open Payments Dataset Downloads](https://www.cms.gov/OpenPayments/Data/Dataset-Downloads) | 
 | [HHS](https://www.hhs.gov/) | [FDA](https://www.fda.gov/) | [Drug Adverse Events, Device Adverse Events, Animal & Veterinary Adverse Events](https://open.fda.gov/data/downloads/) | 
 | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [Bibliometric publication citation graph links](https://icite.od.nih.gov/api) | 
 | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [Clinical Trials](https://classic.clinicaltrials.gov/ct2/resources/download) | 
 | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [ExPORTER: NIH Grant funding](https://reporter.nih.gov/exporter) | 
 | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [PubMed Central: Full text biomedical publications](https://www.ncbi.nlm.nih.gov/pmc/tools/ftp/) | 
 | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [PubMed: Biomedical publication abstract](https://pubmed.ncbi.nlm.nih.gov/download/) | 
 | [Legislative](https://www.congress.gov/) | [GPO](https://www.gpo.gov/) | [US Federal Register](https://www.govinfo.gov/bulkdata/FR) | 

## Development of AI Ready

Questions and scores for the AI dataset can be found at [AI_ready_questions.yaml](src/AI_ready_questions.yaml)

## Development

Built with :purple_heart: by [@metasemantic](https://twitter.com/metasemantic).
Code is linted by [black](https://github.com/psf/black) and conforms to standards by [flake8](https://github.com/PyCQA/flake8).
New projects should be added to [data/datasets.yaml](data/datasets.yaml), run `make build`, and submit a PR.