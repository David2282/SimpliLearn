# Employee Turnover Analytics

This project uses exploratory data analysis and machine learning to identify patterns associated with employee turnover and predict which employees are most likely to leave.

The analysis includes:

* Data-quality checks and turnover-focused visualizations
* K-means clustering to identify distinct employee segments
* Class balancing with SMOTE
* Logistic Regression, Random Forest, and Gradient Boosting models
* Model evaluation using cross-validation, ROC-AUC, recall, precision, F1-score, and confusion matrices
* Employee risk categories with targeted retention recommendations

Random Forest was selected as the best-performing model because it provided the strongest overall results and identified the greatest proportion of employees who left while maintaining high precision. The final analysis translates its predictions into Green, Yellow, Orange, and Red risk zones to help HR prioritize retention efforts.

## Technologies

Python, Jupyter Notebook, pandas, NumPy, Matplotlib, Seaborn, scikit-learn, and imbalanced-learn.
