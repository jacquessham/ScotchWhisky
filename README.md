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

## Goal of this Project
The goal of this project is to build a content-based recommendation system for whiskies. It means recommending a whisky based on the similarity between two whiskies. There are more than 86 brands of Scotch whisky and I want a model/system to recommend other brands based on the characters and flavor.

## Region Classification
The first approach is to classify which Whisky Region the whisky distilleries are classified. The idea is that each region has its general flavor and characters of the whiskies. The assumption is that a person who likes one highland whisky, I will recommend other highland whisky to that person. The plan of this approach is that once we have trained with a model from 86 distilleries, we can classify the region of the 87th whisky distillery from the model.
<br>
<br>
I will train the models with 4 algorithm: Logistic Regression, SVC, Descision Tree, and Random Forest.
<br>
<br>

This is the code of <a href="whisky_classify_regions.py">Evaluating models</a>.
<br>
Result is the following:<br>
![Screenshot](model_results.png)
<br>
As the result, I found that logistic regression model has the best accuracy among all models. 
<br>
<a href="whisky_clf.py">Logistic Regression</a><br>
<a href="Whisky_CorrectLabel.twb">Tableau (Correct Label)</a><br>
<a href="Whisky_WrongLabel.twb">Tableau (Wrong Label)</a><br>
Label Visualization:<br>
![Screenshot](WhiskyRegion_correctlabel.jpg)<br>
![Screenshot](WhiskyRegion_wronglabel.jpg)
<br>
<br>
The result of region classification is disappointing: The best model only achieves 58% of accuracy, my expectation of a good classification model should have achieved above 80% accuracy. (Explain the models are no good)
<br>
(The data set is not balanced, not good for classification model)
<br>
(What about Bourbons, Irish, Japanese?)
<br>
<br>
I would say this approach is not a good system to recommend whiskies.

## Dendrogram
<a href="whisky_dendrogram.py">Dendrogram Python code</a>
![Screenshot](whisky_dendrogram.png)

## Clustering
<a href="whisky_clustering.py">Clustering</a>
