# Dendrogram
Second approach is to use dendrogram to display the hierarchical relationship among distilleries. Dendrogram is one of the algorithms in hierarchical clustering. The idea is to use the quantified characters and flavor to calculate the similiarity of distilleries.

## File
whisky_dendrogram.py is the code to read the data and visualize the dendrogram through Plotly. In this code, only pandas and Plotly are the packages used. Once the data is manipulated, the code would create the dendrogram on a html page by Plotly (create_dendrogram in figure_factory). The dendrogram can be viewed on the html page on a browser.

## Result
The result looks like this:
<img src='../Images/dendrogram.png'>

