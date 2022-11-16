In Project Bangaluru House Price Prediction

 At first dataset was converted into pandas dataframe to to data cleaning 
 * like removing outliers in BHK colums,
 * dropping missing values,
 * categorical text to numarical by one hot encoding in Locations

 then a grid of different model were applied 
   * like simple linear regression
   * Lasso regression
   * decision Tree
 to chose best performing model.

 Dumped the model as pickle file and columns info as json file to apply it on unseen data. 
