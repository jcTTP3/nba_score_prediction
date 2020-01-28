# Predicting Fantasy Basketball Points with Multiple Linear Regression

## The Goal
The aim of this project is to try to predict daily fantasy performance, as measured by the DraftKings [formula](https://www.draftkings.com/help/rules/nba) using a multiple regression model.

## The Data
The National Basketball Association provides historical game information that is available to the public through their API. For the purpose of this project, we collected team and player box score data for all games during the 2017-2018, 2018-2019 seasons, and the games through November 24 for the 2019 season.
* 50,000+ data points
* 700+ individual players

We took the original data and calculated Draft Kings fantasy points (DK_PTS), as well as rolling three game averages for each statistic for each player for each game (variables ending in _TRAIL3).

### Untransformed Data
<img src = "https://github.com/rweng18/nba_score_prediction/blob/master/Images/fig1_untransformed_variables.jpg" width = "600" height = "600">

### Transformed Data
<img src = "https://github.com/rweng18/nba_score_prediction/blob/master/Images/fig2_transformed_variables.jpg" width = "600" height = "600">

## The Model
Using traditional box score data for each of the games in our data set, we calculated rolling three game averages for each player to predict their performance in the following game. While boxscores provide around 20 different counting statistics for each player per game, many of these are correlated to one another. Therefore our final linear model only includes trailing 4 game averages for field goal attempts, assists, turnovers, and rebounds. 

In order make the variables in our model more normally distributed and thus comply with the principles of linear regression, we applied a power transformation to them using the Yeo-Johnson method, which allows for negative values. 

<img src = "https://github.com/rweng18/nba_score_prediction/blob/master/Images/yeo-johnson.jpeg">

We used 70% of the data to train the model and then tested the model on 30% of the data.

### Correlation Matrix of Final Model
<img src = "https://github.com/rweng18/nba_score_prediction/blob/master/Images/fig4_correlation_matrix_final_vars.jpg" width = "400" height = "300">

## Results & Future Work
Our final model achieved an r-squared of 0.495, with an F-Stat of 9,079 and a p-value for each of our predictor variables close to zero. However the average mean squared error for our model is more than 10% of the range for our target variable (in power transformed terms). The model produces significant results, however could be improved through the incorporation of additional predictors like strength of opponent, rest days, travel, and others. This model is satisfactory, although we would like to explore the use of other models such as ridge regression and time series analysis in order to better explain the variation in daily fantasy points.

<img src = "https://github.com/rweng18/nba_score_prediction/blob/master/Images/table3_final_model_test.jpeg">

### Residuals Q-Q Plot
<img src = "https://github.com/rweng18/nba_score_prediction/blob/master/Images/fig5_final_model_residuals.jpg">
