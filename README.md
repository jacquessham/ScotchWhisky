# Scotch Whisky Recommendation System

This project is aimed to build a content-based recommendation system to help Scotch whisky salesmen to recommend Scotch Whisky to a customer based on the quantified quality of the Scotch whiskies. 
<br><br>
Please refer to [Report](/Report) to understand the process of how the recommendation system is built. Also, there is a Medium Post to talk about this project. If you would like to read the Medium post, you may refer to the <a href="https://towardsdatascience.com/recommending-scotch-whisky-ea440c2eb289">link</a>
<br><br>
<b>If you are interested with the application which can recommend whisky to you, you may check out the <a href="https://github.com/jacquessham/ScotchWhisky/tree/master/RecommendationApplication">Recommendation Application</a> folder</b>. If you would like to read the Medium post about the frontend upgrade of this application, you may go to this <a href="https://medium.com/stackademic/upgrading-the-frontend-of-my-previous-machine-learning-project-da8d8005f20d">link</a>.
<br><br>
Here are the brief structure of this repository.

## Data
The original data is downloaded from <a href="https://www.kaggle.com/koki25ando/scotch-whisky-dataset">Kaggle</a> which obtained the data set from WhiskyClassified.com.
<br><br>
In the original data set contains 12 columns of characters or flavors, including body, sweetness, smoky...etc. Besides those features, there are columns of distillery name, postcode, UTM latitude and UTM longitude of the distilleries.
<br><br>
Additionally to the original 86 rows by 12 columns data set, I added three more columns:
<ul>
	<li>Latitude in degree</li>
	<li>Longitude in degree</li>
	<li>Region (Region Classification of Whisky Distillery)</li>
</ul>

<br><br>
You may find the dataset [here](Data/whisky.csv) or the documentation of the dataset in the [Data](Data) folder.

<br><br>
Here is the map of distilleries location with region classification.
<img src=Images/WhiskyRegion_correctlabel.jpg>

## Goal of this Project
The goal of this project is to build a content-based recommendation system for whiskies. It means recommending a whisky based on the similarity between two whiskies. There are more than 86 brands of Scotch whisky and I want a model/system to recommend other brands based on the characters and flavor.

## Region Classification
The first approach is to classify which Whisky Region the whisky distilleries are classified. The idea is that each region has its general flavor and characters of the whiskies. The assumption is that a person who likes one highland whisky, I will recommend other highland whisky to that person. The plan of this approach is that once we have trained with a model from 86 distilleries, we can classify the region of the 87th whisky distillery from the model.
<br><br>

The detail of the code may be found in the [Region Classification Folder](RegionClassification)

<img src="Images/WhiskyRegion_wronglabel.jpg">
<br><br>
However, the result of the classification model does not meet expectation. So, the second step is train the model in hierarchical clustering.

## Dendrogram
Second approach is to use dendrogram to display the hierarchical relationship among distilleries. Dendrogram is one of the algorithms in hierarchical clustering. The idea is to use the quantified characters and flavor to calculate the similiarity of distilleries.

<br><br>
<img src=Images/whisky_dendrogram.png>

<br><br>
However, the dendrogram is hard to find similarity among whiskies and interpret. Also, it is hard to train the salesmen to read the dendrogram when they make any recommendation.
<br><br>

This is the Python code for the <a href="Dendrogram/whisky_dendrogram.py">dendrogram</a> or the [Dendrogram Folder](Dendrogram)

## Clustering
The last approach is to cluster the similar distilleries by k-means. And here is the Python code [here](Clusters/whisky_clustering.py) The problem is find the best k for the algorithm.
<br><br>
You may go to the [Clusters folder](Clusters) to find out the process of how the recommendation system using k-means. Here is the result:
<br>

<ul>
	<li>Group 1: Aberfeldy, Aberlour, Anchroisk, BenNevis, Benrinnes, Benromach, BlairAthol, Craigallechie, Deanston, Edradour, Glenfarclas, Glenlivet, Glenturret, Knochando, Longmorn, Old Fettercairn, Scapa, Strathisla</li>
	<li>Group 2: AnCnoc, Auchentoshan, Aultmore, Bunnahabhain, Cardhu, Craigganmore, Dalwhinnie, Dufftown, Glen Elgin, Glen Grant, Glen Keith, Glen Moray, Glenallachie, Glengoyne, Glenmorangie, Mannochmore, Miltonduff, Speyside, Strathmill, Tamdhu, Tamnavulin, Tobermory</li>
	<li>Group 3: Ardbeg, Caol Illa, Clynelish, Lagavulin, Laphroaig, Talisker</li>
	<li>Group 4: Arran, Belvenie, Benriach, Bladnoch, Glen Deveron Macduff, Glen Garioch, Glen Ord, Glen Spey, Glenfiddich, Glenkinchie, Glenlossie, Glenrothes, Inchgower, Linkwood, Royal Brackla, Speyburn, Teaninich, Tomatin, Tomintoul, Tullibardine</li>
	<li>Group 5: Ardmore, Balblair, Bowmore, Bruichladdich, Glen Scotia, Highland Park, Isle of Jura, Loch Lomond, Oban, Old Pulteney, Springbank, Tormore</li>
	<li>Group 6: Balmenach, Dailuaine, Dalmore, Glendronach, Glendullan, Macallan, Mortlach, Royal Lochnagar</li>
</ul>

<br><br>
The result of the optimal clustering looks like this on the map:
<br>
<img src="Images/ClusteringDistilleries.jpg">
<br><br>
The model using the k-means algorithm is useful for recommendating Scotch Whisky. So I decided to use k-mean, with k=6, to build the recommendation system.

## Application
The application will use the k-means algorithm model, while K=6 to train a K Mean model, to calculate the recommendation quantitatively. The are three ways to return a list of recommendation:
<ul>
	<li>Enter a whisky distillery name</li>
	<li>Choose from a list of characters and flavors</li>
	<li>Nothing</li>
</ul>

<br>
<ol>
	<li>If we enter a whisky distillery name, the application return a list of whiskies within the same cluster. The list of whiskies are sorted by the flavor similarity</li>
	<li>If we choose from a list of character and flavors, the application return a list of whiskies that meets the criteria. Note that the whiskies on the list do not belong the same cluster.</li>
	<li>If nothing is entered, application suggests Macallan. (See the Application folder for explaination)</li>
</ol>

<br>
The application may be run on command line for developer or on a user-friendly GUI.
<img src=Images/method2.png>
<img src=Images/gui2.png>

<br><br>
You may find the codes and the captures in the <a href="https://github.com/jacquessham/ScotchWhisky/tree/master/RecommendationApplication">RecommendationApplication</a>

## Report
In the [Report folder](Report), there is a report of going over how the recommendation system is built by choosing the best model from Region Classification, Dendrogram, and K-means Clustering.

## Whisky Analysis by Lapointe and Legendre
In the [Lapointe et Legendre folder](Lapointe_et_Legendre), we are going to revisit the clusting approach with the algorithm suggested by Lapointe and Legendre's paper <i>A classification of pure malt Scotch whiskies</i>. Our goal is to improve the recommendation application.

## Glossary
<ul>
	<li>Whisky means life of water in Gaelic</li>
	<li><b>Whisky or Whiskey?</b> Whisky is the spelling used in Scotch whiskies, while whiskey is commonly spelled in Irish whiskeys. This repository will spell whisky for Scotch whiskies and whiskies produced with Scotch whiskies School of Thought, such as Japanese, Taiwanese whiskies, and whiskeys for Irish and American whiskeys.</li>
	<li>The pural form of whisky and whiskey are whiskies and whiskeys, respectively</li>
</ul>

