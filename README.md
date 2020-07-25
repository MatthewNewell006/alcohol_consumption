# Alcohol-Consumption                                                     
<h3>Correlating Alcohol Consumption within Cold and Warm climates</h3>



From cocktails to craft brews, the "art of the drink" is a way of life for some, a pitfall for others, but coveted by many. Where is the line bewteen creation and consumption? What allows some to maintian a responsible approach to alcohol while others simply lose themelves in it? I wil be looking into the rate of consumptions in both warm and cold climates. Do the "dog days of summer" attribute to the mentality of "cracking open a cold one"? Or does life in cooler regions make you want to bundle up and get down? Here I will being taking a look at alcohol consumption at different temperatures to see if there is a pattern.
<br><br>

<h3>Data Mining</h3>

The process of finding adequate data to compare how temperature effects liquor sales was daunting. The information was spoty at best across multiple data sites like Kaggle and Data.Gov. I found a lot of insufficient data and most of it pertained to a global parsing. I was looking for something pertaining to the United States. I finally found info that I was looking for. The closest year I could find to align properly, was for 2015. Once I had what I was looking for, I proceeded to streamline it best I could. Originaly I was going to compare amount of sales against temperatures in every state. However looking for a munging took up most of the time to simply attain a solid comoparison. Below is a comparison of the number of drinks that were sold in the year 2015.

<hr>

<li>There were 17 missing cells in May. Fortunately They were in the middle of the month so I was able to average the first part and last part of May and fill these missing areas with an average of averages.</li>

<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/gallons_total.jpg" alt="alt text" width="45%" height="45%">

<hr>

<h3>Analysis</h3>

<li>A closer inspection reveals that the ideal temperature for the most sales of beer, wine, and liquor is 94°</li>  

<h3>Correlation Testing: Drink Consumption</h3>

<h3><ul>Beer</ul></h3>
<li>Total Drinks/Gallons/Average Gallons Per Capita: 443.26, 1.87, 1.17</li>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_beer_gallons.jpg" width="50%" height="50%">

<h3><ul>Wine</ul></h3>
<li>Total Drinks/Gallons/Average Gallons Per Capita: 226.27, 1.14, 1.95</li>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_wine_gallons.jpg" width="50%" height="50%">

<h3><ul>Shot</ul></h3>
<li>Total Drinks/Gallons/Average Gallons Per Capita: 404.87, 1.14, 0.87</li>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_shot_gallons.jpg" width="50%" height="50%">

<h3><ul>Annual</ul></h3>
<li>Drinks/Gallons: 1002.67, 4.7</li>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_annual_gallons.jpg" width="50%" height="50%">
<br><br>
<hr>
<h3><ul>Spike in Consumption</ul></h3>
<li>Study showed that more shots was consumed at low temperatures, while wine peaked at mid to lower temperatures and beer spiking in higher temperatures</li>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/combined_drinks.jpg" alt="alt text" width="50%" height="50%">

<h3>PLotting the PDF</h3>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/probability_density_function.jpg" width="50%" height="50%">
<li>Probability Density Function shows that the information suggests a Normal Distribution.</li>

<hr>

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

<b>Performing a couple of correlation tests I was able to deduce that there is a good significance between the amount of alcohol comsumed as it pertains to how high or low the temperature is.</b>

<hr>

<h3>Conclusion</h3>
After working thhrough the data, I have found that people do in fact tend to drink more alcohol in warmer temperatures. Given more time I would use my findings and further my analysis into how this compares against geographical locations. I still have quesitons about the quality of life in areas with warmer and colder temps. Knowing what I've learned from the dataset, I would hope to find if there is a correlation between alcohol consumption and the standard of living in these areas. Deducing a different approach for people to consider when contemplating questions like where would be a good place to move.
