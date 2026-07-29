# 📊 Customer Churn Prediction

An end-to-end Data Science project to analyse customer churn using **MySQL, Python, Machine Learning, and Tableau**. This project follows an industry-standard workflow, from data validation to predictive modelling and business intelligence dashboards.

---

## 🎯 Project Objective

Customer churn is a major challenge for subscription-based businesses. The objective of this project is to:

- Analyse customer behaviour using SQL.
- Identify factors contributing to customer churn.
- Build a machine learning model to predict customer churn.
- Create an interactive Tableau dashboard for business stakeholders.
- Provide data-driven recommendations to improve customer retention.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| MySQL | Database creation, data validation and business analysis |
| Python | Data preprocessing, EDA and machine learning |
| Jupyter Notebook | Data analysis and model development |
| Pandas & NumPy | Data manipulation |
| Matplotlib & Seaborn | Data visualisation |
| Scikit-learn | Machine learning |
| Tableau | Interactive dashboard |
| Git & GitHub | Version control and project documentation |

---

# 📂 Project Structure

```text
Customer-Churn-Prediction
│
├── data
│   ├── raw
│   └── processed
│
├── sql
│   ├── 01_database_setup.sql
│   ├── 02_data_validation.sql
│   └── 03_business_analysis.sql
│
├── notebooks
│
├── reports
│   └── Day1_Business_Insights.md
│
├── tableau
│
├── models
│
└── README.md
```

---

# 📁 Dataset

- **Dataset:** Synthetic Customer Churn Dataset
- **Total Records:** 100,000
- **Target Variable:** `Churn`

### Features

- CustomerID
- Age
- Gender
- Tenure
- MonthlyCharges
- Contract
- PaymentMethod
- TotalCharges
- Churn

---

# ✅ Day 1 Progress

## Database Setup

- Created MySQL database.
- Created customer table.
- Imported 100,000 customer records.

## Data Validation

Performed the following validation checks:

- Verified total record count.
- Checked duplicate Customer IDs.
- Checked NULL values.
- Validated categorical values.
- Analysed numerical column statistics.
- Identified negative values in `TotalCharges`.

## Initial Business Analysis

Calculated key business metrics including:

- Total Customers
- Overall Churn Rate
- Average Monthly Charges
- Average Total Charges
- Average Customer Tenure
- Customer Distribution by Contract
- Churn Rate by Contract
- Churn Rate by Gender
- Churn Rate by Payment Method

---

# 📈 Key Business Insight

- **Total Customers:** 100,000
- **Churned Customers:** 33,144
- **Overall Churn Rate:** **33.14%**

### Observation

Approximately one out of every three customers has churned, indicating a significant customer retention challenge. Further analysis will focus on identifying high-risk customer segments and the key drivers of churn.

---

# 🚀 Project Roadmap

### ✅ Phase 1 - Business Understanding & SQL Analysis
- Database setup
- Data validation
- Business KPI analysis

### ⏳ Phase 2 - Data Cleaning & Preprocessing
- Handle invalid values
- Feature engineering
- Data preparation

### ⏳ Phase 3 - Exploratory Data Analysis
- Univariate analysis
- Bivariate analysis
- Multivariate analysis
- Correlation analysis

### ⏳ Phase 4 - Machine Learning
- Data preprocessing
- Train multiple classification models
- Hyperparameter tuning
- Model evaluation

### ⏳ Phase 5 - Tableau Dashboard
- Executive dashboard
- Churn KPIs
- Customer segmentation
- Interactive visualisations

### ⏳ Phase 6 - Business Recommendations
- Identify churn drivers
- Customer retention strategies
- Final business report

---

# 📌 Current Status

| Phase | Status |
|--------|--------|
| Database Setup | ✅ Completed |
| Data Validation | ✅ Completed |
| Business Analysis | ✅ Completed |
| Data Cleaning | ⏳ In Progress |
| Exploratory Data Analysis | ⏳ Pending |
| Feature Engineering | ⏳ Pending |
| Machine Learning | ⏳ Pending |
| Tableau Dashboard | ⏳ Pending |
| Final Report | ⏳ Pending |

---

# 📬 Author

**Nihil John Sundar S**

- 📍 Chennai, India
- 💼 Aspiring Data Scientist
- 🔗 LinkedIn: https://linkedin.com/in/nihil-john-3bab411b9
- 💻 GitHub: https://github.com/Nihiljohn75

---

⭐ **This repository will be updated daily as the project progresses through SQL, Python, Machine Learning, and Tableau.**
