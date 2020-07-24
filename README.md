# Alcohol-Consumption                                                     
<b>Correlating Alcohol Consumption within Cold and Warm climates</b>



From cocktails to craft brews, the "art of the drink" is a way of life for some, a pitfall for others, but coveted by many. Where is the line bewteen creation and consumption? What allows some to maintian a responsible approach to alcohol while others simply lose themelves in it? I wil be looking into the rate of consumptions in both warm and cold climates. Do the "dog days of summer" attribute to the mentality of "cracking open a cold one"? Or does life in cooler regions make you want to bundle up and get down? Here I will being taking a look at alcohol consumption at different temperatures to see if there is a pattern.
<br><br>

<b>Data Mining</b>
<br><br>

The process of finding adequate data to compare how temperature effects liquor sales was daunting. The information was spoty at best across multiple data sites like Kaggle and Data.Gov. I found a lot of insufficient data and most of it pertained to a global parsing. I was looking for something pertaining to the United States. I finally found info that I was looking for. The closest year I could find to align properly, was for 2015. Once I had what I was looking for, I proceeded to streamline it best I could. Originaly I was going to compare amount of sales against temperatures in every state. However looking for a munging took up most of the time to simply attain a solid comoparison. Below is a comparison of the number of drinks that were sold in the year 2015.
<br><br>
The data still had some areas of no record. I'm not sure where this inconsisitency came from. There were 17 missing cells in May. Of course I still had 250 entries that still allowed me to continue with goal. 
<br><br>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/gallons_total.jpg" alt="alt text" width="45%" height="45%">
<br><br>


<br><br>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_beer_gallons.jpg" width="45%" height="45%">
<br><br>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_wine_gallons.jpg" width="45%" height="45%">
<br><br>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_shot_gallons.jpg" width="45%" height="45%">
<br><br>
<img src="https://github.com/MatthewNewell006/alcohol_consumption/blob/master/img/scatter_annual_gallons.jpg" width="45%" height="45%">
<br><br>

<h3>Correlation Testing: Drink Consumption</h3>

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

