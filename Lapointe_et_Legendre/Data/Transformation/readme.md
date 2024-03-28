# Data Transformation
You may find the scripts transforming the original data to the transformed data for the project, as well as the transformed data (Save as CSV files or any modern data format).

## Files
### columns.json
This JSON file defines the hierarachy structure on Feature type and character columns.

### distillery.csv
This CSV file map the distillery names to each row entries used in the Original Data folder

### transform.py
This script combins all character files in the original data folder and distillery names, and transform the format and saved in a CSV file <i>whisky_characters.csv</i>

### whisky_characters.csv
The dataset transformed from the original data folder and saved in CSV format. All the columns found in the original data folder are combined into one file. Any analytical work should be utilizing this file.
