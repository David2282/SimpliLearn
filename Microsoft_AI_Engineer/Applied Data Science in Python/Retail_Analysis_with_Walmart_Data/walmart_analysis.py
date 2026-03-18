import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor

# Load the dataset
df = pd.read_csv('Walmart_Store_sales.csv')
print("Dataset loaded successfully.")
print(df.shape)


# Data Cleaning
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Create a clean working copy
df_clean = df.copy()
df_clean.info()
df_clean["Year"] = df_clean["Date"].dt.year
df_clean["Quarter"] = df_clean["Date"].dt.quarter
df_clean["Month"] = df_clean["Date"].dt.month


# Store with Maximum Sales
store_sales = df_clean.groupby('Store')['Weekly_Sales'].sum()
max_store = store_sales.idxmax()
max_value = store_sales.max()

print("Store with highest sales:", max_store)
print("Total sales:", f"{max_value:,.2f}")

# Store with highest standard deviation in sales
store_std = df_clean.groupby('Store')['Weekly_Sales'].std()
max_std_store = store_std.idxmax()
max_std_value = store_std.max()

print("Store with highest sales variability:", max_std_store)
print("Standard deviation:",f"{max_std_value:,.2f}")

# Coefficient of Variation for each store
store_mean = df_clean.groupby('Store')['Weekly_Sales'].mean()
store_cv = store_std / store_mean
max_cv_store = store_cv.idxmax()
max_cv_value = store_cv.max()

print("Store with highest sales variability (coefficient of variation):", max_cv_store)
print("Coefficient of variation:", f"{max_cv_value:.2f}")

print(df_clean["Date"].min())
print(df_clean["Date"].max())

# Q3 Growth in 2012
sales_2012 = df_clean[df_clean["Year"] == 2012]
quarter_sales = sales_2012.groupby('Quarter')['Weekly_Sales'].sum()
q2_sales = quarter_sales[2]
q3_sales = quarter_sales[3]

q3_growth = (q3_sales - q2_sales) / q2_sales

print(quarter_sales)
print("Q3 2012 Growth Rate:", f"{q3_growth:.2%}")

# Holiday Sales Analysis
holiday_avg = df_clean.groupby("Holiday_Flag")["Weekly_Sales"].mean()
non_holiday_mean = df_clean[df_clean["Holiday_Flag"] == 0]["Weekly_Sales"].mean()
holiday_sales = df_clean[df_clean["Holiday_Flag"] == 1]
high_holiday_sales = holiday_sales[holiday_sales["Weekly_Sales"] > non_holiday_mean]

print("Non-holiday mean:", f"{non_holiday_mean:,.2f}")
print("Holiday weeks above non-holiday mean:", len(high_holiday_sales))

# Hight holiday sales preview
print(high_holiday_sales[["Date", "Store", "Weekly_Sales"]].head(10))  


# Monthly Sales Analysis
monthly_sales = df_clean.groupby('Month')['Weekly_Sales'].sum()

print("Monthly Sales:")
print(monthly_sales)

# Monthly Sales Totals
total_sales_all_data = monthly_sales.sum()
print("Total Sales (All Data):", f"{total_sales_all_data:,.2f}")


# Average weekly sales per month
monthly_avg = df_clean.groupby('Month')['Weekly_Sales'].mean()
print("Average Weekly Sales by Month:")
print(monthly_avg)

# Semester Sales
df_clean["Semester"] = df_clean["Month"].apply(lambda x: 1 if x <= 6 else 2)
semester_sales = df_clean.groupby('Semester')['Weekly_Sales'].sum()
print("Semester Sales:", semester_sales)

# Filter dataset for Store 1
store1 = df_clean[df_clean["Store"] == 1].copy()

print("\nStore 1 Dataset Shape:", store1.shape)

# Convert Date to Days 
start_date = store1["Date"].min()
store1["Days"] = (store1["Date"] - start_date).dt.days

print("\nDate converted to day index:")
print(store1[["Days", "Date"]].head()) 


# Predictive Model: Linear Regression

# Features (X) and Target (y)
features = ["Days", "Fuel_Price", "CPI", "Unemployment"]
X = store1[features]
y = store1["Weekly_Sales"]

# Split the Dataset into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("\n--- Store 1Linear Regression Results ---")
print("MSE:", f"{mse:,.2f}")
print("RMSE:", f"{np.sqrt(mse):,.2f}")
print("R-squared:", f"{r2:.4f}")

# Coefficients of the model
coeffs = pd.Series(model.coef_, index=features).sort_values(key=abs, ascending=False)

print("\nCoefficients (sorted by impact):")
print(coeffs)
print("Intercept:", model.intercept_)


# Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=200, random_state=42)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

rf_mse = mean_squared_error(y_test, rf_pred)
rf_rmse = rf_mse ** 0.5
rf_r2 = r2_score(y_test, rf_pred)

print("\n--- Random Forest Results ---")
print("MSE:", f"{rf_mse:,.2f}")
print("RMSE:", f"{rf_rmse:,.2f}")
print("R-squared:", f"{rf_r2:.4f}")

# Model Comparison
comparison = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "MSE": [mse, rf_mse],
    "RMSE": [np.sqrt(mse), rf_rmse],
    "R2": [r2, rf_r2]
})

print("\nModel Comparison:")
print(comparison)

# Model Comparison by Best Accuracy
best_comparison = comparison.sort_values("R2", ascending=False)


