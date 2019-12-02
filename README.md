# nba_score_prediction
Using multiple linear regression to predict number of fantasy basketball points scored on a given night.

## The Data
The National Basketball Association provides historical game information that is available to the public through their API. For the purpose of this project, we collected team and player box score data for all games during the 2017-2018 seasons, and the games through November 24 for the 2019 season.

## The Goal
The aim of this project is to try to predict daily fantasy performance, as measured by the DraftKings [formula](https://www.draftkings.com/help/rules/nba) using a multiple regression model

## The Model
Using traditional box score data for each of the games in our data set, we calculated rolling three game averages for each player to predict their performance in the following game. While boxscores provide around 20 different counting statistics for each player per game, many of these are correlated to one another. Therefore our final linear model only includes trailing 3 game averages for field goal attempts, assists, turnovers, and rebounds. In order make the variables in our model more normally distributed and thus comply with the principles of linear regression, we applied a power transformation to them. 

## Results
Our final model achieves an r-squared of 0.495, with an F-Stat of 9,079 and a p-value for each of our predictor variables close to zero. However the average mean squared error for our model is more than 10% of the range for our target variable (in power transformed terms). The model produces significant results, however could be improved through the incorporation of additional predictors like strength of opponent, rest days, travel, and others. This model is satisfactory, although we would like to explore the use of other models such as ridge regression and time series analysis in order to better explain the variation in daily fantasy points.
