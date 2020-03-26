# Application

Once we have determined K Mean Model where K = 6 is the best model. The application would use such hyperparameter to build the model with K mean algorithm with Python and Scikit-learn.
<br>
Before building the model, there is a concern on Cold Start Problem.

## Cold Start Problem
There are 3 situtation we have to consider for this application:
<ul>
	<li>The consumer has his/her favorite whisky and wants to find a similar one.</li>
	<li>The consumer does not know any whisky but he/she knows what flavor he/she likes.</li>
	<li>The consumer does not know anything.</li>
</ul>
<br>
<br>

### Case 1: The consumer has his/her favorite whisky and wants to find a similar one.
In this case, we simply recommend a whisky very similar to the whisky consumer likes. The application would return a list of whiskies in the same group. There are 2 approaches of how the list is sorted.
<ul>
	<li>Physical Distance between distilleries</li>
	<li>Euclidean Distance of qualitified flavor between whiskies </li>
</ul>
<br>
If sorted by the physical distance between distilleries, the application calculates the euclidean distance of latitude and longitude of the distilleries.
<br>
If sorted by the Euclidean distance of qualitified flavor between whiskies, the application calculates the euclidean of the 12 characters and flavor of the whiskies.
<br>
The code in here will be defaulted to sort by the the Euclidean distance of qualitified flavor between whiskies. If you prefer another, comment out the block of the current method and uncomment another block of codes.

### Case 2: The consumer does not know any whisky but he/she knows what flavor he/she likes.
In this case, our goal is to figure out what whisky fits best to the consumer's preference. The application would list all the features we have in the data set and ask the consumer to pick one and score between 1–4 (Cannot pick 0), which the score represents: Light, Medium, Strong, and Very Strong.
<br>
Once the consumer has picked and scored the features, the application use pandas to filter the list of whiskies that meets the criteria and sorted by alphabetical order. The whiskies do not cluster into the same group. The goal is to have a list of whiskies that meets the consumer's expectation from what he/she has picked. 
<br>
If there is no whisky meets the criteria, the application score down the strength until there is at least one whisky is generated in a list. The reason I score down because the assumption is that people are more likely to accept lighter flavor than heavier flavor.

### Case 3: The consumer does not know anything.
If the person has no idea where to start, we would recommend a whisky which is well-known to non-whisky drinker and does not contain very aggressive flavor. Macallan is a well-known single-malt whisky which gives more confidence to whisky beginners. Secordly, it is not peaty nor having an aggressive flavor. Thirdly, it provides a fruity and sweet texture to drinkers that whisky beginners are more likely to accept.
<br>
Based on these reasons, the application recommends Macallan if there is no a lot of input.

## How it works
There is 2 code files and 1 csv file required.
<ul>
	<li> whisky_recommender.py - The UI file in Python</li>
	<li> script.py - The Python file prints the options for users</li>
	<li> whisky_with_cluster.csv - CSV file with assigned group</li>
</ul>
<br>
First, you need to have use <a href="../Clusters/whisky_recommendation.py">whisky_recommendation.py file</a> to assign each distillery to a group and save to whisky_with_cluster.csv (So that, it does not require the application to train the model every time it runs). Then, whisky_recommender.py would ask which method to recommend whisky, by entering distillery name, selecting flavor and its strength, or input nothing (That represents the 3 cases discussed in last section).
<br>
