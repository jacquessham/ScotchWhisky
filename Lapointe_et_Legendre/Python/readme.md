# Python Files (Whisky Analysis by Lapointe and Legendre)
In folder contains the program written in Python. This is the effort to replicate the suggested algorithm used to recommend whiskies suggested by Lapointe and Legendre using Python. The goal is to produce the result and display on an UI using Python.

## Files
<ul>
	<li><i>adj_distance.py</i>: Script to calculate distance among distilleries with the algorithm suggested by Lapointe and Legendre</li>
	<li><i>distance.py</i>: Script to calculate distance among distilleries without any adjustment suggested by Lapointe and Legendre</li>
	<li><i>display_result.py</i>: Script to display the result calculated by <i>adj_distance.py</i></li>
	<li><i>adj_distance.txt</i>: The result calculated by <i>adj_distance.py</i></li>
	<li><i>distance.txt</i>: The result calculated by <i>distance.py</i></li>
	<li><i>display_result.py</i>: (Coming soon...)</li>
</ul>

## Workflow
### distance.py
The workflow of this script is:
<ol>
	<li>Load the whisky character score data</li>
	<li>Calculate the similarity score by directly calculate the norm of the similarity matrix</li>
	<li>Save the result in a distance matrix and save in <i>distance.txt</i></li>
</ol>

### adj_distance.py
The workflow of this script is:
<ol>
	<li>Load the whisky character score data</li>
	<li>Prepare metadata for the calculation helper</li>
	<li>Calculate the similarity score by calculate the norm of the similarity between 2 whiskies with adjustment formula using the <i>calculate_distance</i> function and store the results into a matrix, repeat that until the matrix is fully filled</li>
	<li>Save the result in a distance matrix and save in <i>adj_distance.txt</i></li>
</ol>
<br>

The workflow of <i>calculate_distance</i> function is:
<ol>
	<li>Calculate the coefficient for each character:
		<ul>
			<li>For each feature type, find the total numbers of characters can be found between two whiskies (Whisky A characters union whisky B characters)</li>
			<li>The coefficient is total number of characters in both whiskies divided by the number of characters in such feature type</li>
			<li>Assign the coefficient for each character</li>
		</ul>
	</li>
	<li>Calculate the similarity score for each whiskies-pair:
		<ul>
			<li>Get the weighted characteristic similarity: Square the difference of character scores between 2 whiskies and multiply by the assigned coefficients</li>
			<li>Sum all the weighted characteristic similarities from the previous steps</li>
			<li>Divided the sum all the weighted characteristic similarities by the sum of weights.</li>
			<li>Take the square root of it to get the Euclidean distance.</li>
		</ul>
	</li>
	<li>Return the Eclidean distance</li>
</ol>

### display_result.py
Coming soon...

## Recommendation Application
The plan of displaying the recommendation on an UI will be released in the next version.<br>
Coming soon...