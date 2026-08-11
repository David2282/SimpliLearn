# ===== 1. SETUP =====
# %% Imports  
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# optional (add later if needed)
# from scipy import stats
# import statsmodels.api as sm
# import numpy as np

# %% Load Dataset
df= pd.read_csv('marketing_data.csv')


# ===== 2. DATA CLEANING =====
# %% clean column names and datatypes
df.columns = df.columns.str.strip()
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%m/%d/%y')
df['Income'] = df['Income'].str.replace('$', '', regex=False)
df['Income'] = df['Income'].str.replace(',', '', regex=False)
df['Income'] = df['Income'].str.strip()
df['Income'] = pd.to_numeric(df['Income'])

print(df.columns.tolist()) 
print(df.shape)
df.info()
print(df.head())

# %% clean categorical values
print(df['Education'].value_counts())
print(df['Education'].unique())

df['Marital_Status'] = df['Marital_Status'].replace({
    'Together': 'Married',
    'Alone': 'Single',
    'YOLO': 'Single',
    'Absurd': 'Single',
})

print(df['Marital_Status'].value_counts())

DEBUG = False
if DEBUG:
    # Income analysis by group
    print(df.groupby(['Education', 'Marital_Status'])['Income'].count())
    print(df.groupby(['Education', 'Marital_Status'])['Income'].median())

    # Inspect missing distribution
    print(df[df['Income'].isnull()][['Education', 'Marital_Status']])
    print(
        df[df['Income'].isnull()]
        .groupby(['Education', 'Marital_Status'])
        .size()
    )
    

# %% impute missing income
df['Income'] = df['Income'].fillna(
    df.groupby(['Education', 'Marital_Status'])['Income'].transform('median')
)

print(df['Income'].isnull().sum())
print(df['Income'].describe())

# ===== 3. FEATURE ENGINEERING =====
# %% create new variables
df['Total_Spending'] = (
    df['MntWines'] +
    df['MntFruits'] +
    df['MntMeatProducts'] +
    df['MntFishProducts'] +
    df['MntSweetProducts'] +
    df['MntGoldProds']
)

df['Total_Purchases'] = (
    df['NumWebPurchases'] +
    df['NumCatalogPurchases'] +
    df['NumStorePurchases']
)

current_year = datetime.now().year
df['Age'] = current_year - df['Year_Birth']

df['Children'] = df['Kidhome'] + df['Teenhome']

df['Deal_Purchase_Ratio'] = df['NumDealsPurchases'] / df['Total_Purchases'].replace(0, 1)

print(df[['Total_Spending', 'Total_Purchases', 'Age', 'Children', 'Deal_Purchase_Ratio']].head())

# ===== 4. DATA PREPARATION =====
# %% outlier inspection/treatment
print(df[['Total_Spending', 'Total_Purchases', 'Age', 'Children', 'Deal_Purchase_Ratio']].describe())
features = ['Total_Spending', 'Total_Purchases', 'Age', 'Children']

for feature in features:
    plt.figure()
    sns.boxplot(x=df[feature])
    plt.title(f'Boxplot of {feature}') 
    plt.show()

for feature in features:
    plt.figure()
    df[feature].hist(bins=30)
    plt.title(f'Histogram of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()

df = df[df['Age'] < 100]  # filter out unrealistic ages
upper_limit = df['Total_Spending'].quantile(0.99)
df['Total_Spending'] = df['Total_Spending'].clip(upper=upper_limit)

print("Upper Limit:", upper_limit)
print("Max after clipping:", df['Total_Spending'].max())

# %% encoding
education_order = {
    'Basic': 0,
    '2n Cycle': 1,
    'Graduation': 2,
    'Master': 3,
    'PhD': 4
}

df['Education_Encoded'] = df['Education'].map(education_order)
print(df[['Education', 'Education_Encoded']].head())
print(df.loc[df['Education_Encoded'].isnull(), 'Education'].unique())

marital_dummies = pd.get_dummies(
    df['Marital_Status'], 
    prefix='Marital', 
    drop_first=True,
    dtype=int
    )

df = pd.concat([df, marital_dummies], axis=1)

print(marital_dummies.head())
print(df.filter(like='Marital_').head())

# ===== 5. ANALYSIS =====
# %% correlation heatmap

corr = df.select_dtypes(include=['number']).corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=False)
plt.title('Correlation Heatmap')
plt.show()

important_features = ['Response', 'Total_Spending', 'Total_Purchases', 'Age', 'Children', 'Education_Encoded']

corr_subset = df[important_features].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_subset, annot=True)
plt.title('Key Feature Correlation Heatmap')
plt.show()


# %% hypothesis testing 1
df[['Age', 'NumStorePurchases', 'NumWebPurchases']].corr()
df.groupby('Age')[['NumStorePurchases', 'NumWebPurchases']].mean()


# %% hypothesis testing (2) correlation 
df[['Children', 'NumStorePurchases', 'NumWebPurchases']].corr()

# %% hypothesis testing (2) mean 
df.groupby('Children')[['NumStorePurchases', 'NumWebPurchases']].mean()

# %% hypothesis testing 3 correlation 
df[['NumCatalogPurchases', 'NumWebPurchases', 'NumStorePurchases']].corr()

# %% hypothesis testing 3 mean
df.groupby('NumCatalogPurchases')[['NumWebPurchases', 'NumStorePurchases']].mean()
features = ['NumCatalogPurchases', 'NumWebPurchases', 'NumStorePurchases']
for feature in features:
    plt.figure()
    df[feature].hist(bins=30)
    plt.title(f'Histogram of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show() 

# %% hypothesis testing 4
print(df.columns)
print(df['Country'].value_counts())

# %% hypothesis testing 4 
print(df.groupby('Country')['Total_Spending'].sum().sort_values(ascending=False))

df['US_vs_Other'] = df['Country'].apply(lambda x: 'USA' if x == 'US' else 'Other')
print(df.groupby('US_vs_Other')['Total_Spending'].sum())
print(df.groupby('US_vs_Other')['Total_Spending'].mean())

# %% required visualizations
# %% Top products by total sales
products = ['MntWines', 
            'MntFruits', 
            'MntMeatProducts', 
            'MntFishProducts', 
            'MntSweetProducts', 
            'MntGoldProds'
            ]
product_totals = df[products].sum().sort_values(ascending=False)
print(product_totals)
print("Top Product:", product_totals.idxmax(), product_totals.max())
print("Bottom Product:", product_totals.idxmin(), product_totals.min())
plt.figure(figsize=(10, 6))
sns.barplot(x=product_totals.index, y=product_totals.values)
plt.title('Product Sales Totals')
plt.xlabel('Products')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# %% Age vs Acceptance Rate

# %% 

age_response = df.groupby('Age')['Response'].mean()
print(age_response)

# %%
plt.figure(figsize=(10, 6))
sns.lineplot(x=age_response.index, y=age_response.values)
plt.title('Age vs Acceptance Rate')
plt.xlabel('Age')
plt.ylabel('Acceptance Rate')
plt.show()


# %%
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 50, 70, 100], labels=['0-50', '51-70', '71+'])
print(df['Age_Group'].value_counts())
age_group_response = df.groupby('Age_Group')['Response'].mean()
print(age_group_response)

# %%
plt.figure(figsize=(10, 6))
sns.barplot(x=age_group_response.index, y=age_group_response.values)
plt.title('Age Group vs Acceptance Rate')
plt.xlabel('Age Group')
plt.ylabel('Acceptance Rate')
plt.show()

# %% Country with Highest Acceptance Rate
responders = df[df['Response'] == 1]
result = responders.groupby('Country').size().sort_values(ascending=False)
print(result)

# %% Children vs Total Spending
children_spending = df.groupby('Children')['Total_Spending'].mean()
print(children_spending)

# %%
children_spending.plot(kind='bar')
plt.title('Average Total Spending by Number of Children')
plt.xlabel('Number of Children')
plt.ylabel('Average Total Spending')
plt.show()

# %% Education vs Complaints
complainers = df[df['Complain'] == 1]
education_counts = complainers['Education'].value_counts()
print(education_counts)
education_counts.plot(kind='bar')
plt.title('Number of Complainers by Education Level')
plt.xlabel('Education Level')
plt.ylabel('Number of Complainers')
plt.show()


# %% Complaint rate by education
complaint_rate = df.groupby('Education')['Complain'].mean().sort_values(ascending=False)
print(complaint_rate)

