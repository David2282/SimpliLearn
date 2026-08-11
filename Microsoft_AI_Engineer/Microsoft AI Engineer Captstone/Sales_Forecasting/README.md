# Restaurant Sales Forecasting

## Project Overview

This capstone project analyzes historical restaurant sales data and develops a machine-learning model to forecast item-level demand for 2022. The goal is to help restaurants make more informed decisions about inventory, staffing, purchasing, and future sales planning.

The project combines restaurant, menu-item, and daily sales data into a single analytical dataset covering six restaurants and 100 menu items.

## Project Objectives

* Examine overall sales patterns and seasonal trends
* Analyze demand across weekdays, months, quarters, and years
* Compare sales and revenue performance among restaurants
* Identify popular products and leading items within each restaurant
* Evaluate the relationship between menu prices, calories, and demand
* Build a complete item-level sales forecast for 2022

## Modeling Approach

Three regression models were developed and compared:

* Linear Regression
* Random Forest Regressor
* XGBoost Regressor

Calendar-based features such as year, quarter, month, day of the week, day of the month, and cyclical seasonal indicators were created for model training.

The final six months of historical data were reserved as a chronological test set. Model performance was evaluated using Root Mean Squared Error (RMSE), with Random Forest producing the best forecasting performance.

The selected model was retrained using all available historical data before generating daily predictions for every menu item throughout 2022.

## Business Analysis

Because restaurant sales volumes differed substantially, the project distinguishes between:

* Absolute item demand, which supports inventory and purchasing decisions
* Restaurant-adjusted item performance, which compares each product with the average item sold at its own restaurant

This prevents the largest restaurant from dominating every product comparison and provides a more meaningful view of menu performance across locations.

## Deliverables

The project includes:

* A complete exploratory data analysis
* Restaurant and item-level sales comparisons
* Machine-learning model evaluation
* A full 2022 daily sales forecast
* Monthly and restaurant-level forecast summaries
* Restaurant-adjusted item rankings
* Forecast visualizations and business recommendations
* Exported CSV files containing the final results

## Technologies Used

* Python
* Jupyter Notebook
* pandas
* NumPy
* Matplotlib
* Seaborn
* scikit-learn
* XGBoost

## Conclusion

The completed forecasting system provides both operational demand estimates and scale-adjusted menu insights. It demonstrates how historical sales data and machine learning can support more effective planning across restaurants with substantially different sales volumes.
