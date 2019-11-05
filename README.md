# Scotch Whisky Recommendation System
The project is ongoing.

## Data
The original data is downloaded from <a href="https://www.kaggle.com/koki25ando/scotch-whisky-dataset">Kaggle</a> which obtained the data set from WhiskyClassified.com. Additionally to the original 86 rows by 12 columns data set, I added three more columns:
<ul>
	<li>Latitude in degree</li>
	<li>Longitude in degree</li>
	<li>Region (Region Classification of Whisky Distillery)</li>
</ul>
<br>
Note: The original data set contains latitude and longitude in UTM that I found useful to convert to degree. 
<br>
<br>

The data set only contains selected distilleries in Scotland that makes single-malt whiskies.
<br>

Under the Region column, the whisky distilleries to the following regions based on the classification by <i>Collins gem - Whiskies</i>. In this book, it classifies distilleries to the following regions:
<ul>
	<li>Lowland</li>
	<li>Highland</li>
	<li>Speyside</li>
	<li>Islay and Islands</li>
</ul>
<br>
<br>
You may find the data set<a href="whisky.csv"> here</a>.

## Region Classificaiton
<a href="whisky_classify_regions.py">Evaluating models</a>
<br>
Result is the following:<br>
![Screenshot](model_results.png)
<br>
<a href="whisky_clf.py">Logistic Regression</a><br>
<a href="Whisky_CorrectLabel.twb">Tableau (Correct Label)</a><br>
<a href="Whisky_WrongLabel.twb">Tableau (Wrong Label)</a><br>
Label Visualization:<br>
![Screenshot](WhiskyRegion_correctlabel.jpg)<br>
![Screenshot](WhiskyRegion_wronglabel.jpg)

## Dendrogram
<a href="whisky_dendrogram.py">Dendrogram Python code</a>
![Screenshot](whisky_dendrogram.png)

## Clustering
<a href="whisky_clustering.py">Clustering</a>
