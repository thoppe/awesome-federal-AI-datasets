# Awesome Federal AI datasets

A list of high quality accessible datasets for training AI from the US Federal government. Our primary aim is to provide a convenient platform for discovering these datasets, ensuring their accessibility, and upholding a standard of quality, as defined by rigorous criteria. The datasets are organized based on their respective originating Department or independent agency.


| Dept. | Agency  | Title |
| ----  | ----    | ----  |
 | [DOC](https://www.commerce.gov/) | [NOAA](https://www.noaa.gov/) | [Weather and Climate Quick Links : National Centers for Environmental Information](https://www.ncei.noaa.gov/weather-climate-links) | 
 | [DOC](https://www.commerce.gov/) | [USPTO](https://www.uspto.gov/) | [US Patents: full text and images](https://bulkdata.uspto.gov/) | 
 | [DOC](https://www.commerce.gov/) | [USPTO](https://www.uspto.gov/) | [US Trademarks: Filings and registration images](https://bulkdata.uspto.gov/) | 
 | [DOJ](https://www.justice.gov/) | [NSD](https://www.justice.gov/nsd) | [Foreign Agents Registration Act : Registrants and PDFs](https://efile.fara.gov/ords/fara/f?p=API:BULKDATA) | 
 | [GSA](https://www.gsa.gov/) | []() | [Regulations.gov, no easy bulk download](https://www.regulations.gov/bulkdownload) | 
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


Draft ideas for AI ready:

+ Open Access: Ensure that the dataset is freely available to anyone without any access restrictions or subscription requirements. Specify the dataset's licensing terms clearly, indicating how it can be used, shared, and modified. Consider open licenses that align with the principles of open data sharing.
+ Downloadable: The dataset should be downloadable in its entirety, allowing researchers and developers to work with it offline and on their preferred hardware.
+ Format: Provide the dataset in a single, well-organized file format (such as CSV, JSON, or Parquet) to facilitate easy ingestion and processing.
+ Abundant Records: Include a substantial number of records in the dataset. A larger number of diverse examples allows for better model training and evaluation.
+ Quality Documentation: Offer clear and comprehensive documentation that explains the dataset's origin, purpose, structure, and any preprocessing steps performed on the data. This documentation aids users in understanding and effectively utilizing the dataset.
+ Data Dictionaries: Include data dictionaries or schema descriptions detailing the meaning of each field or column. This enhances transparency and helps users interpret the data accurately.
+ API Access: Consider providing API endpoints that allow users to access specific elements of the dataset programmatically. This can simplify data retrieval for specific use cases and scenarios.
+ Data Diversity: Ensure that the dataset covers a wide range of relevant cases, scenarios, or examples to promote robust model training and generalization.
+ Versioning: If updates or corrections are made to the dataset, maintain a versioning system that clearly identifies changes. This helps users stay up-to-date with improvements.

Bonus scores?
+ Regular Updates: Maintain the dataset by periodically updating it with fresh data or addressing issues that may arise.
+ Ethical Considerations: Address potential ethical concerns associated with the dataset, such as privacy, bias, and fairness, and take steps to mitigate these concerns.


## Development

Built with :purple_heart: by [@metasemantic](https://twitter.com/metasemantic).
Code is linted by [black](https://github.com/psf/black) and conforms to standards by [flake8](https://github.com/PyCQA/flake8).
New projects should be added to [data/datasets.yaml](data/datasets.yaml), run `make build`, and submit a PR.