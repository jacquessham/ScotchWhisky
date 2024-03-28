# Data for Lapointe and Legendre's Paper
This folder stores all the data saved for the model training and was downloaded from <a href=http://www.numericalecology.com/data/scotch.html>Legendre's site</a>. However,the data was not suitable to ingest directly for Pandas or Numpy as the dataset is not saved in CSV files. We would transform the original dataset to a CSV file.

## Original Data
The original dataset contains the following files:
<ul>
	<li>Characters by feature type (5 files):
		<ul>
			<li><i>body</i> (8 columns)</li>
			<li><i>color</i> (14 columns)</li>
			<li><i>finish</i> (19 columns)</li>
			<li><i>nose</i> (12 columns)</li>
			<li><i>palate</i> (15 columns)</li>
			<li><i>Scotch</i> (68 columns): Combined all columns with all above files</li>
		</ul>
	</li>
	<li>Geography files: <ul>
		<li><i>Dist geo:Scotch</i></li>
		<li><i>Distillery coordinates</i></li>
		<li><i>Regions</i></li>
	</ul>
	<li>Readme: Documentation on the dataset</li>
	</li>
</ul>
<br>

The dataset package is saved in [Unix](Data/OriginalData/unix) and [Dos](Data/OriginalData/dos) format in two different folders. The dataset are the same. For the purpose of this project, we will convert the dataset to CSV format for convenience - This folder only serve the purpose of storing the data from this <a href="http://www.numericalecology.com/labo/Scotch/ScotchData.zip">link</a>.

## Transformation
In the [Transformation](Transformation) folder, you may find the scripts transforming the original data to the transformed data for the project, as well as the transformed data (Save as CSV files or any modern data format).

### Transformation Scripts
You may find <i>transform.py</i> that it will transform all the character files in Unix files from the Original Data folder to one modern CSV file <i>whisky_characters.csv</i>.

### Transformed Data
You may find <i>whisky_characters.csv</i> in the [Transformation](Transformation) folder. Any analytical work should be utilizing this file.
