# Awesome Federal AI datasets

A list of high quality accessible AI-ready datasets from the US Federal government.

This repo aims to provide a convenient platform for discovering these datasets, ensuring their accessibility, and upholding a standard of quality as defined by an objective criteria.

## Catalog status

**Local verification: passed on 2026-07-16.** Last run: `make lint`, `make validate`,
`make verify`, `make test`, and `make check-urls`; 20 manifests validated and
20 publisher landing pages were reachable. Hosted checks are intentionally not
used for this repository. Run the same commands locally after each major
catalog change; [the contracts](docs/README.md) define the required handoff.


| Status| Dept. | Agency  | Title |
| ----  | ----  | ----    | ----- |
| [:green_circle:](data/datasets/HHS_NIH_clinical-trials.yaml) | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [Clinical Trials](https://clinicaltrials.gov/data-api/how-download-study-records) |
| [:green_circle:](data/datasets/HHS_CDC_covid-19-case-surveillance-public-use-data-with-geography.yaml) | [HHS](https://www.hhs.gov/) | [CDC](https://www.cdc.gov/) | [COVID-19 Case Surveillance Public Use Data with Geography](https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4) |
| [:green_circle:](data/datasets/HHS_NIH_pubmed-biomedical-publication-abstract.yaml) | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [PubMed: Biomedical publication abstract](https://pubmed.ncbi.nlm.nih.gov/download/) |
| [:green_circle:](data/datasets/HHS_NIH_pubmed-central-full-text-biomedical-publications.yaml) | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [PubMed Central: Full text biomedical publications](https://pmc.ncbi.nlm.nih.gov/tools/ftp/) |
| [:question:](data/datasets/HHS_NIH_exporter-nih-grant-funding.yaml) | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [ExPORTER: NIH Grant funding](https://reporter.nih.gov/exporter) |
| [:green_circle:](data/datasets/HHS_FDA_drug-adverse-events-device-adverse-events-animal-veterinary-adverse-events.yaml) | [HHS](https://www.hhs.gov/) | [FDA](https://www.fda.gov/) | [Drug, Device, Animal, and Veterinary Adverse Events](https://open.fda.gov/data/downloads/) |
| [:green_circle:](data/datasets/HHS_CMS_open-payments-dataset-downloads.yaml) | [HHS](https://www.hhs.gov/) | [CMS](https://www.cms.gov/) | [Open Payments Data](https://www.cms.gov/priorities/key-initiatives/open-payments/data/explore) |
| [:question:](data/datasets/HHS_CDC_vaccine-adverse-event-reporting-system-vaers.yaml) | [HHS](https://www.hhs.gov/) | [CDC](https://www.cdc.gov/) | [Vaccine Adverse Event Reporting System (VAERS)](https://vaers.hhs.gov/data/datasets.html) |
| [:green_circle:](data/datasets/EPA_EPA_air-quality-system-pre-generated-data.yaml) | [EPA](https://www.epa.gov/) | [EPA](https://www.epa.gov/) | [Air Quality System pre-generated data](https://aqs.epa.gov/aqsweb/airdata/download_files.html) |
| [:green_circle:](data/datasets/DOI_USGS_landsat-collection-2.yaml) | [DOI](https://www.doi.gov/) | [USGS](https://www.usgs.gov/) | [Landsat Collection 2](https://www.usgs.gov/landsat-missions/landsat-collection-2) |
| [:green_circle:](data/datasets/DOC_CENSUS_american-community-survey-public-use-microdata-sample.yaml) | [DOC](https://www.commerce.gov/) | [CENSUS](https://www.census.gov) | [American Community Survey Public Use Microdata Sample](https://www.census.gov/programs-surveys/acs/microdata.html) |
| [:question:](data/datasets/USDA_ARS_fooddata-central-full-download.yaml) | [USDA](https://www.usda.gov/) | [ARS](https://www.ars.usda.gov/) | [FoodData Central full download](https://fdc.nal.usda.gov/download-datasets/) |
| [:question:](data/datasets/Legislative_GPO_us-federal-register.yaml) | [Legislative](https://www.congress.gov/) | [GPO](https://www.gpo.gov/) | [US Federal Register](https://www.govinfo.gov/bulkdata/FR) |
| [:question:](data/datasets/HHS_NIH_bibliometric-publication-citation-graph-links.yaml) | [HHS](https://www.hhs.gov/) | [NIH](https://www.nih.gov/) | [Bibliometric publication citation graph links](https://support.icite.nih.gov/hc/en-us/articles/9513563045787-Bulk-Data-and-API) |
| [:question:](data/datasets/DOJ_NSD_foreign-agents-registration-act-registrants-and-pdfs.yaml) | [DOJ](https://www.justice.gov/) | [NSD](https://www.justice.gov/nsd) | [Foreign Agents Registration Act : Registrants and PDFs](https://efile.fara.gov/ords/fara/f?p=API:BULKDATA) |
| [:question:](data/datasets/DOE_NREL_end-use-load-profiles-us-building-stock.yaml) | [DOE](https://www.energy.gov/) | [NREL](https://www.nrel.gov/) | [End-use load profiles for the United States building stock](https://data.openei.org/submissions/4520) |
| [:question:](data/datasets/DOC_USPTO_us-patents-full-text-and-images.yaml) | [DOC](https://www.commerce.gov/) | [USPTO](https://www.uspto.gov/) | [US Patents text and images](https://data.uspto.gov/) |
| [:question:](data/datasets/DOC_NOAA_weather-and-climate-quick-links-national-centers-for-environmental-information.yaml) | [DOC](https://www.commerce.gov/) | [NOAA](https://www.noaa.gov/) | [Weather and Climate Quick Links : National Centers for Environmental Information](https://www.ncei.noaa.gov/resources/weather-climate-links) |
| [:question:](data/datasets/GSA__regulations-gov-federal-rulemaking-process.yaml) | [GSA](https://www.gsa.gov/) | [TTS](https://tts.gsa.gov/) | [Regulations.gov, Federal rulemaking process](https://open.gsa.gov/api/regulationsgov/) |
| [:question:](data/datasets/DOC_USPTO_us-trademarks-filings-and-registration-images.yaml) | [DOC](https://www.commerce.gov/) | [USPTO](https://www.uspto.gov/) | [US Trademarks: Filings and registration images](https://data.uspto.gov/) |

## AI Ready scores

Questions and scores for the AI dataset can be found at [AI_ready_questions.yaml](src/AI_ready_questions.yaml). 

## Development

Built with :purple_heart: by [@metasemantic](https://twitter.com/metasemantic).
Code is linted by [black](https://github.com/psf/black) and conforms to standards by [flake8](https://github.com/PyCQA/flake8).
New projects should be added to [data/datasets](data/datasets). Run `make validate`,
`make build`, `make verify`, and `make test` before committing a catalog change.
