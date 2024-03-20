# Whisky Analysis by Lapointe and Legendre
After reading the paper written by Lapointe and Legendre, it inspires many whisky and data lovers to recommend whiskies to the boarder auidence through a quantitative approach. In this exercise, we will explore the approach taken by Lapointe and Legendre and apply for the whisky recommendation system.


## Data
The original data provided by Lapointe and Legendre can be downloaded at this <a href="http://www.numericalecology.com/labo/Scotch/ScotchData.zip">link</a>, and can be found in the <i>Original Data</i> folder in the [Data](/Data) folder. The original data is saved into multiple files, and the aggregated version may be found in the [Data](/Data) folder.

## Algorithm Suggested by Lapointe and Legendre
Instead of computing the similiarity among distilleries, Lapointe and Legendre suggested that the boarder feature types are also as important as the individual character:

```
When computing the similarities, each of the five feature types was given the same importance. To achieve this, the characteristics were weighted by the inverse of the number of characteristic in their type.
```

<br>
Note: This quotation can be found on page 5 on this <a href="http://www.numericalecology.com/reprints/Appl%20Stat%2043,%201994.pdf">PDF</a>.

<br><br>
In order to do this, we will sum the sum of the weighted characteistic similarities was divided by the sum of the weights to rescale the coefficients between 0 (No characteristic in common) and 1 (Complete similarity).
<br><br>
For example:<br>
Given Bunnahabhain has a descriptors:
<ul>
	<li>Color: Gold</li>
	<li>Nose: Firm, light, smooth</li>
	<li>Body: Sweet, fruit, clean</li>
	<li>Palate: Fresh, sea</li>
	<li>Finish: Full</li>
</ul>

<br>
And given Tullibardine has a descriptors:
<ul>
	<li>Color: Gold</li>
	<li>Nose: Firm, light, smooth</li>
	<li>Body: Sweet, grass</li>
	<li>Palate: Fresh, grass</li>
	<li>Finish: None</li>
</ul>

The calculation would be:<br>
Coming soon...


## R
Folder link: [R](R)
<br><br>
Coming soon...

## Python
Folder link: [Python](Python)


## Reference
* Paper <a href="http://www.numericalecology.com/data/scotch.html">link</a>
* Example: Whiskey Analytics, Ch 6: Similarity, Neighbors, Clusters, p.145, <i>Data Science for Business</i>, Foster Provost & Tom Fawcett