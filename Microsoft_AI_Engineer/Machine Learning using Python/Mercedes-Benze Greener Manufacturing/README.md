# Mercedes-Benz Greener Manufacturing

## Project Overview

This project focuses on reducing the time Mercedes-Benz vehicles spend on the testing bench by predicting testing time using machine learning techniques. The dataset contains different feature combinations representing customized vehicle configurations. The objective was to preprocess the data, train a predictive model, and evaluate model performance using XGBoost regression.

The final solution was implemented using a modular machine learning pipeline architecture in Python.

---

# Project Objectives

The following tasks were required by the project statement:

* Remove columns with zero variance
* Check for null and unique values
* Apply label encoding
* Perform dimensionality reduction
* Predict testing time using XGBoost

---

# Technologies Used

* Python
* Pandas
* Scikit-learn
* XGBoost
* VS Code
* Jupyter Notebook

---

# Pipeline Workflow

1. Load training and testing data
2. Preprocess data
3. Train XGBoost model
4. Evaluate model performance
5. Generate predictions

The pipeline structure allowed each stage to remain independent and reusable.

---

# Data Preprocessing

## 1. Null Value Checks

Both training and testing datasets were checked for null values.

## 2. Unique Value Analysis

Unique values were analyzed to identify low-information columns.

## 3. Zero Variance Removal

Columns containing only a single repeated value were removed because they provide no predictive value to the model.

## 4. Label Encoding

Categorical columns were encoded using `LabelEncoder` from Scikit-learn so the XGBoost model could process them numerically.

---

# Dimensionality Reduction (PCA)

Principal Component Analysis (PCA) was implemented to satisfy the dimensionality reduction requirement.

Initial preprocessing with PCA reduced the dataset from approximately:

```python
(4209, 365) → (4209, 1)
```

This caused a significant loss of predictive information. During testing:

* Model predictions became nearly constant
* R² score dropped to approximately 0.03
* The model underfit the dataset heavily

## Why PCA Was Not Helpful

XGBoost is a tree-based model that performs best when it can split on original feature relationships. PCA transforms the original features into blended continuous components, which removed much of the structured information needed for effective tree splitting.

The Mercedes-Benz dataset contains many sparse and categorical-style features, which are better handled directly by XGBoost without dimensionality reduction.

For this reason, PCA was tested, evaluated, and ultimately removed from the final training pipeline.

The PCA code was intentionally retained in comments for documentation and experimentation purposes.

---

# Model Training

The model used was:

```python
XGBRegressor
```

Final tuned hyperparameters included:

```python
n_estimators=400
learning_rate=0.03
max_depth=7
subsample=0.8
colsample_bytree=0.8
random_state=42
```

---

# Model Evaluation

The model was evaluated using:

* R² Score
* RMSE (Root Mean Squared Error)
* MAE (Mean Absolute Error)

## Final Results

| Metric   | Result |
| -------- | ------ |
| R² Score | 0.8102 |
| RMSE     | ~7.84  |
| MAE      | ~4.99  |

---

# Key Lessons Learned

* Tree-based models such as XGBoost do not always benefit from PCA
* Hyperparameter tuning can significantly improve model performance
* Modular pipeline architecture improves readability and maintainability
* Proper preprocessing is critical for model success
* Evaluating failed approaches is an important part of the machine learning workflow

---

# Conclusion

This project successfully implemented a modular machine learning pipeline capable of predicting Mercedes-Benz testing times using XGBoost regression. Multiple preprocessing and modeling approaches were tested, including PCA-based dimensionality reduction.

Through experimentation and evaluation, the final optimized pipeline achieved strong predictive performance with an R² score above 0.81.
