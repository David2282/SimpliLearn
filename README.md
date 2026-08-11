# Microsoft AI Engineer Program | Project Portfolio

This repository contains projects completed throughout the **Simplilearn Microsoft AI Engineer Program**. The work documents my progression from Python-based data analysis and visualization through machine learning, deep learning, transformer architectures, and applied generative AI.

Across these projects, I have practiced the complete data science lifecycle: defining a problem, exploring and preparing data, engineering features, selecting an appropriate validation strategy, comparing models, evaluating results, and translating technical findings into practical conclusions.

## Featured Projects

### Employee Turnover Analytics

A classification and employee-retention analysis focused on identifying workers who may be at risk of leaving an organization.

Key components included:

* Exploratory analysis of employee satisfaction, workload, tenure, promotions, and other workplace factors
* K-means clustering to identify groups among employees who left
* SMOTE applied to the training data to address class imbalance
* Logistic Regression, Random Forest, and Gradient Boosting classifiers
* Cross-validation and holdout-set model comparison
* Evaluation using accuracy, precision, recall, F1 score, confusion matrices, and ROC-AUC
* Employee risk rankings and retention-priority zones

The Random Forest model produced the strongest overall results. The project also demonstrated why model selection should reflect the business problem: in employee-retention analysis, missing a likely departure can be more costly than investigating a false positive, making recall especially important.

### Restaurant Sales Forecasting

A forecasting and regression project built from approximately 110,000 sales records covering six restaurants and 100 menu items.

Key components included:

* Merging restaurant, item, and transaction datasets
* Date parsing and calendar-based feature engineering
* Analysis of monthly, quarterly, weekday, restaurant, and item-level patterns
* Rolling-average features for capturing recent sales behavior
* A time-aware train/test split using the final six months as the test period
* Linear Regression, Random Forest, and XGBoost model comparison
* RMSE-based model evaluation
* Next-year sales forecasting and business-focused visualizations

Random Forest achieved the lowest test RMSE among the evaluated models.

One of the most valuable lessons from this project was that a result can be numerically correct while still being misleading. For example, an item may appear to be the overall top seller primarily because one high-volume restaurant drives most of its sales. Meaningful analysis requires separating raw volume from patterns that generalize across restaurants.

### D&D Encounter Feasibility Transformer

A custom deep-learning project that uses a Transformer encoder to classify whether a proposed tabletop role-playing encounter is appropriately balanced for a player party.

The project involved:

* Designing and generating a custom structured dataset
* Representing party characteristics, monster information, challenge ratings, and encounter descriptions
* Building a binary classification model with PyTorch
* Implementing Transformer encoder components
* Training with cross-entropy loss and the Adam optimizer
* Tracking validation performance and using early stopping
* Evaluating whether attention-based models can learn relationships within mixed encounter data

This project provided hands-on experience moving beyond traditional machine-learning estimators and into custom neural-network architecture design.

### AI-Assisted Storytelling

A smaller generative-AI demonstration exploring how language models can support creative writing.

The project included the development of a longer story chapter and a separate scene through iterative prompting, revision, and human direction. It demonstrates the importance of prompt clarity, narrative consistency, tone control, and human review when using generative AI for creative work.

### Microsoft Malware Detection Capstone — In Development

My current capstone project explores transformer-based malware detection using the large-scale **Microsoft Malware Prediction** dataset.

The planned workflow includes:

* Memory-conscious processing of multi-gigabyte training and testing files
* Data sampling and chunk-based loading
* Missing-value and high-cardinality categorical-feature analysis
* Feature encoding and preprocessing
* A Transformer encoder classifier implemented in PyTorch
* Comparison with a traditional machine-learning baseline such as XGBoost
* Evaluation using accuracy, precision, recall, F1 score, ROC-AUC, and confusion matrices

The goal is to investigate whether a Transformer can learn useful relationships among a large number of categorical and numerical machine attributes while maintaining a reproducible workflow on local hardware.

## Technical Toolkit

| Area                 | Libraries and Tools       | Practical Experience                                                                                                    |
| -------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Data preparation     | pandas, NumPy             | Cleaning, merging, filtering, aggregation, missing-value analysis, and feature engineering                              |
| Visualization        | Matplotlib, Seaborn       | Trend analysis, distributions, correlations, heatmaps, model comparisons, and business reporting                        |
| Machine learning     | scikit-learn              | Preprocessing, encoding, train/test splitting, cross-validation, clustering, regression, classification, and evaluation |
| Imbalanced learning  | imbalanced-learn          | Applying SMOTE correctly to training data                                                                               |
| Gradient boosting    | XGBoost                   | Regression, model comparison, baseline development, and hyperparameter experimentation                                  |
| Deep learning        | PyTorch                   | Tensors, neural-network modules, training loops, loss functions, optimization, and Transformer encoders                 |
| Development workflow | Jupyter Notebook, VS Code | Interactive development, experimentation, documentation, and notebook reporting                                         |
| Version control      | Git, GitHub               | Project organization, staged commits, branching, repository maintenance, and reproducible project sharing               |

## Data Science Knowledge Developed

Through the applied data science portion of the program, I gained experience with:

* Exploratory data analysis and data-quality assessment
* Numerical and categorical feature preparation
* One-hot encoding and feature scaling
* Regression, classification, clustering, and forecasting problems
* Random and time-aware validation strategies
* Cross-validation and model comparison
* Class imbalance and resampling techniques
* Feature importance and risk ranking
* Hyperparameter experimentation
* Data leakage awareness
* Selecting metrics based on the real cost of model errors
* Communicating analytical findings to a nontechnical audience

## Deep Learning Knowledge Developed

The deep-learning specialization introduced both the theory and implementation of:

* Neural-network training and backpropagation
* Activation functions, loss functions, and optimizers
* Training, validation, and test workflows
* Overfitting, regularization, and early stopping
* Embeddings and learned feature representations
* Attention and multi-head attention
* Feed-forward layers, residual connections, and layer normalization
* Transformer encoders
* Binary classification with neural networks
* Generative AI and iterative prompt development

## What This Portfolio Represents

These projects range from guided coursework to independently designed extensions and capstone development. Together, they demonstrate my ability to work through a technical problem methodically, understand the reasoning behind modeling decisions, evaluate results critically, and communicate what the data actually supports.

The most important lesson I have gained is that building a successful model involves much more than producing a high score. Validation design, data quality, metric selection, reproducibility, and business context all determine whether a model is genuinely useful.
