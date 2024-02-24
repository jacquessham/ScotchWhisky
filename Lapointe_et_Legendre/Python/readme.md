# Python Files (Whisky Analysis by Lapointe and Legendre)
In folder contains the program written in Python.

## Files
<ul>
	<li><i>adj_distance.py</i>: Script to calculate distance among distilleries with the algorithm suggested by Lapointe and Legendre</li>
	<li><i>distance.py</i>: Script to calculate distance among distilleries without any adjustment suggested by Lapointe and Legendre</li>
	<li><i>display_result.py</i>: Script to display the result calculated by <i>adj_distance.py</i></li>
	<li><i>adj_distance.txt</i>: The result calculated by <i>adj_distance.py</i></li>
	<li><i>distance.txt</i>: The result calculated by <i>distance.py</i></li>
</ul>

## Workflow
### distance.py
<ol>
	<li>Load the whisky character score data</li>
	<li>Calculate the similarity score by directly calculate the norm of the similarity matrix</li>
	<li>Save the result in a distance matrix and save in <i>distance.txt</i></li>
</ol>

### adj_distance.py
<ol>
	<li>Load the whisky character score data</li>
	<li>Prepare metadata for the calculation helper</li>
	<li>Calculate the similarity score by calculate the norm of the similarity with adjustment formula into a matrix</li>
	<li>Save the result in a distance matrix and save in <i>adj_distance.txt</i></li>
</ol>

