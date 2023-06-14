# -Capstone-Project1-Data-analysis-on-Quality-of-life-

## Problem statement
THe goal of this projectis to gather data by scrapping both dynamic and static websites for data analysis on Quality of life based on World population, GDP, inflation and life expectency of each countries.<br/>
The source for these data are:<br/>
1.https://www.worldometers.info/world-population/population-by-country/<br/>
2.https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP) <br/>
3.https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy <br/>
4.https://en.wikipedia.org/wiki/List_of_countries_by_literacy_rate <br/>
5.https://tradingeconomics.com/country-list/inflation-rate?continent=world<br/>

Please visit the public dashboard to checkout the analysis here:<br/>
## 1.Quality of life world wide<br/>
This dashboard contains 5 graphs<br/>
1. A barchart that demonstrates population in all 5 regions including their most populated countries(Asia have the most amount of populaiton of over 4 billion)
2. A barchart demonstrating the Land mass of each region in ascencing order including the countries with biggest land mass(Americas has most amount of land mass compare to Asia where the population is over double)
3. Compare 3 barhcart that estimates GDP From IMF,world bank and CIA for all 5 regions and all their countries based(IMF recorder the highest amount of GDP, and later used as base GDP to compare diffrent regions)
4. A barchart that compares the inflation rate in all 5 region and their countries(Americas have most amount of inflation, Venezuela=436)
5. A Line chart comparing the Life expectency in all the regions including both male and female data(Africa has the lowest life expectency of 66.36 on average while rest of the world have over 75)<br/>

#### Please visit this Link to checkout the public dashboard: https://public.tableau.com/app/profile/sanjid.hossain/viz/CP1QualityoflifeRegionalworldwide/Regionalgraph?publish=yes <br/>


## 2.Quality of Life in Asian countries<br/>
This dashboard contains 3 graphs<br/>
1. Compares three barcharts that demonstrates total population, Land mass and fertility rate in Asian countries(While china and India has the most amount of population, compare to india, China has almost three times more land mass as well as a lower fertilty rate of 1.7 which one of the lowest in Asia)
2. A barchart and a linechart, where the barhcart shows the etsimated GDP from IMF in asia (where China has the bigest GDP, almost over twice of it's 2nd richest nation India) as for the linechart, it compares the inflation rate of previous years to it's current years in asian country(expectedly China and Brunei has the lowest inlation has the, However Countries such as Iran, Turkey,Pakistan and Laos has very concerningly high number Inflation of 39.59,55.50,38,38.86. While Sri-Lanka was deaking with high inflation rate for past few years, their inflation rate hase started to decrease as it's current inflation rate is 25.20 which was previously 35.30)  
3. A Linechart, that compare between Average Life expectency, male and female life expectency for all the asian countries(Singapore and Japan has highest life expectency of 86 and 85, where their female life expectency is 89 and 88, male life expectency is 84 and 81. India has the lowest life expectency of 69 out of all the asian countries despite being 2nd in top for it's economy and land mass, as for china , the average life expectency is 77.78 )<br/>
#### Please visit this Link to checkout the public dashboard: https://public.tableau.com/app/profile/sanjid.hossain/viz/QualityofLifeinAsianContinenet/QualityoflifeinAsia?publish=yes<br/>
### out of all the countries, comparing economy, population growth and the life expectency, it can be assumed that China might have one of the best quality of life in Asian Countries<br/>
<br/>

2.Quality of Life in Asian countries<br/>
Tableau public view3:https://public.tableau.com/app/profile/sanjid.hossain/viz/QualityofLifeinAfricanContinenet/QualityoflifeinAfrica?publish=yes

Tableau public view4:https://public.tableau.com/app/profile/sanjid.hossain/viz/QualityofLifeinAmericanContinenet/Dashboard4?publish=yes

## Build from sources
1. clone the repo
```bash
git clone https://github.com/SanjidHossain/-Capstone-Project1-Data-analysis-on-Quality-of-life-.git
```
2. intialize and activate virtual environment(for linux)
```bash
virtualenv --no-site-packages venv
source venv/bin/activate
```
3. install dependencies
```bash
pip install -r requirments.txt
```
4.download chrome webdriver from https://chromedriver.chromium.org/downloads


