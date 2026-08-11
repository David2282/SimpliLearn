# 📊 Marketing Campaign Data Analysis

## 🎯 Objective

The goal of this project is to analyze customer behavior and identify the key factors that influence whether a customer responds to a marketing campaign. The analysis focuses on exploratory data analysis (EDA), hypothesis testing, and deriving actionable business insights.

---

## 🧹 Data Preparation

### Income Imputation Strategy

#### Problem  
Approximately 1% of income values were missing (23 out of 2240 rows).

#### Investigation  
- Missing values were analyzed across Education and Marital_Status groups  
- Distribution of missing values was spread across multiple groups  
- No single group dominated the missing data  
- Group sizes were sufficiently large for statistical stability  

#### Observations  
- Income distribution is right-skewed (max = 666,666)  
- Mean is sensitive to outliers  
- Median is a more robust measure of central tendency  

#### Decision  
- Used **group-based median imputation**:
  - Grouped by Education and Marital_Status  

#### Justification  
- Handles skewed distributions effectively  
- Preserves relationships between demographic variables  
- Avoids bias introduced by global imputation  

---

## ⚙️ Feature Engineering

The following features were created to better represent customer behavior:

- **Total_Spending**  
  Sum of spending across all product categories:  
  Wines, Fruits, Meat, Fish, Sweets, and Gold Products  

- **Total_Purchases**  
  Total number of purchases across all channels:  
  Web, Catalog, and Store  

- **Children**  
  Total number of children in the household:  
  Kidhome + Teenhome  

- **Deal_Purchase_Ratio**  
  Proportion of purchases made using discounts:  
  NumDealsPurchases / Total_Purchases  

---

## 🔍 Exploratory Data Analysis (EDA)

### Approach

The analysis followed a hypothesis-driven EDA approach:

- Compared feature averages by campaign response  
- Analyzed categorical distributions  
- Evaluated relationships using correlation analysis  
- Examined distributions and outliers  

---

### Key Findings

- **Total Spending** showed the strongest positive relationship with response (~0.26)  
- **Total Purchases** had a moderate positive relationship (~0.16)  
- **Children** showed a negative relationship (~-0.17)  
- **Age** showed little to no relationship with response  
- **Deal Purchase Ratio** had minimal impact  

#### Marital Status Insights

- Married customers had the lowest response rate (~11%)  
- Single, Divorced, and Widowed customers had higher response rates (~20–25%)  

---

### Interpretation

- Behavioral features (spending and purchasing activity) are stronger indicators of response than demographic variables  
- Some initial assumptions (e.g., age being significant) were not supported  
- Customers with higher spending and fewer household constraints are more likely to respond  

---

## 🧪 Hypothesis Testing

### Hypothesis 1  
**Older individuals prefer in-store shopping**

- Weak positive relationship between age and both store and web purchases  
- No evidence of channel preference shift  

**Conclusion:** Not supported. Older customers purchase more overall but do not favor a specific channel.

---

### Hypothesis 2  
**Customers with children prefer online shopping**

- Both store and web purchases decrease as children increase  
- Store purchases decrease more sharply  

**Conclusion:** Partially supported. Families with children purchase less overall but show relatively greater reliance on online channels.

---

### Hypothesis 3  
**Store sales are cannibalized by other channels**

- Strong positive correlations across store, web, and catalog purchases  

**Conclusion:** Not supported. Channels are complementary rather than competitive. High-value customers use multiple channels.

---

### Hypothesis 4  
**The United States outperforms other countries in purchase volume**

- Total spending is higher outside the U.S.  
- Average spending per U.S. customer is higher  

**Conclusion:** Mixed. The U.S. has higher-value customers, but lower overall volume compared to other regions.

---

## 📊 Visual Analysis

### Product Performance
- Wines and meat products generate the highest revenue  
- These categories are the primary drivers of customer spending  

---

### Age vs Campaign Response
- Response rates are relatively consistent across age groups  
- No strong evidence that age significantly impacts response  

---

### Country-Level Response
- Spain (SP) has the highest number of campaign responders  
- Results are influenced by customer distribution across countries  

---

### Children vs Spending
- Customers with more children spend less on average  
- Indicates reduced discretionary spending in larger households  

---

### Education vs Complaints

- Graduates generate the highest number of complaints  
- However, this is influenced by their larger representation in the dataset  

- Customers with a **2nd Cycle education** have the highest complaint rate (~20%)  
- Graduates have a lower complaint rate (~12%)

**Conclusion:**  
Complaint behavior differs by education level when normalized. 2nd Cycle customers are more likely to complain relative to their group size.

---

## 💡 Business Insights & Recommendations

- **Target high-value customers**  
  Focus on customers with high spending and frequent purchases  

- **Leverage multi-channel engagement**  
  Customers use multiple channels — marketing should remain omnichannel  

- **Segment by household size**  
  Families with children show reduced engagement and spending  

- **Do not prioritize age-based targeting**  
  Age is not a strong predictor of campaign response  

- **Monitor customer expectations by education level**  
  Certain segments (e.g., 2nd Cycle) show higher complaint rates  

- **Focus on top-performing product categories**  
  Wines and meat products should remain central to marketing strategies  