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