# Data for Lapointe and Legendre's Paper
This folder stores all the data saved for the model training and was downloaded from <a href=http://www.numericalecology.com/data/scotch.html>Legendre's site</a>. However,the data was not suitable to ingest directly for Pandas or Numpy as the dataset is not saved in CSV files. We would transform the original dataset to a CSV file.

## Original Data
Coming soon...

## Transformation
Coming soon...

## Transformed Data
In the [Transformation](Transformation) folder, you may find <i>transform.py</i> that it will transform all the character files in Unix files from the [Original Data](OriginalData) folder to one modern CSV file <i>whisky_characters.csv</i>. Any analytical work should be utilizing <i>whisky_characters.csv</i>.