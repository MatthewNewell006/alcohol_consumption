# Alcohol-Consumption                                                     
<h3>Correlating Alcohol Consumption within Cold and Warm climates</h3>



From cocktails to craft brews, the "art of the drink" is a way of life for some, a pitfall for others, but coveted by many. Where is the line bewteen creation and consumption? What allows some to maintian a responsible approach to alcohol while others simply lose themelves in it? I wil be looking into the rate of consumptions in both warm and cold climates. Do the "dog days of summer" attribute to the mentality of "cracking open a cold one"? Or does life in cooler regions make you want to bundle up and get down? Here I will being taking a look at alcohol consumption at different temperatures to see if there is a pattern.
<br><br>

<h3>Data Mining</h3>

The process of finding adequate data to compare how temperature effects liquor sales was daunting. The information was spoty at best across multiple data sites like Kaggle and Data.Gov. I found a lot of insufficient data and most of it pertained to a global parsing. I was looking for something pertaining to the United States. I finally found info that I was looking for. The closest year I could find to align properly, was for 2015. Once I had what I was looking for, I proceeded to streamline it best I could. Originaly I was going to compare amount of sales against temperatures in every state. However looking for a munging took up most of the time to simply attain a solid comoparison. Below is a comparison of the number of drinks that were sold in the year 2015.
<br><br>
<li>There were 17 missing cells in May. Not sure why there was this gap but still had 250 observations to continue analysis.</li>

<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/gallons_total.jpg" alt="alt text" width="45%" height="45%">
<br><br>

<h3>Analysis</h3>

<li>A closer inspections reveals that the ideal temperature for the most sales of beer, wine, and liquor is 102°</li>  
<br><br>

<h3>Correlation Testing: Drink Consumption</h3>

<h3><ul>Beer</ul></h3>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_beer_gallons.jpg" width="50%" height="50%">

<h3><ul>Wine</ul></h3>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_wine_gallons.jpg" width="50%" height="50%">

<h3><ul>Shot</ul></h3>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_shot_gallons.jpg" width="50%" height="50%">

<h3><ul>Annual</ul></h3>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_annual_gallons.jpg" width="50%" height="50%">
<br><br>

<h3>PDF</h3>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/probability_density_function.jpg" width="50%" height="50%">
<li>Probability Density Function shows that the information suggests a Normal Distribution.</li>

<h3>Corellation Significance</h3>

| Spearmanr: Number of Gallons |
| --- |
| Correlation (Beer): -0.339638537681751 |
| Pvalue (Beer): 3.869617173537449e-08 |
| Correlation (Wine): -0.3008408600008164 |
| Pvalue (Wine): 1.32615598730314e-0 |
| Correlation (Shots): -0.22470174841968737 |
| Pvalue (Shots): 0.0003519710919161753 |


| MannWhitneyU: Number of Drinks |
| --- |
| Statisitc (Beer): 0.0 |
| Pvalue (Beer): 1.955263257631872e-83 |
| Statistic (Wine): 14136.0 |
| Pvalue (Wine): 3.939313034921851e-26 |
| Statisitc (Shots): 929.0 |
| Pvalue (Shots): 1.2869623103039633e-78 |


| Pearsonr: Number of Drinks |
| --- |
| Beer: (0.03879235442721353, 0.5423373090312318) |
| Wine: (-0.28972604526774554, 3.337259516630482e-06) |
| Shots: (-0.4066398894076336, 2.4714372269605796e-11) |
<br><br>

Performing a couple of correlation tests I was able to deduce that there is a good significance between the amount of alcohol comsumed as it pertains to how high or low the temperature is.


<h3>Conclusion</h3>
