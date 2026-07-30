# 📊 Customer Churn Prediction

An end-to-end **Data Science Project** to analyse customer churn using **MySQL, Python, Machine Learning, and Tableau**. This project follows an industry-standard workflow, covering database design, data validation, exploratory data analysis, predictive modelling, and business intelligence dashboards.

---

# 🎯 Project Objective

Customer churn is one of the biggest challenges faced by subscription-based businesses. The objective of this project is to:

- Analyse customer behaviour using SQL.
- Perform comprehensive data validation and quality assessment.
- Explore customer churn patterns through data analysis.
- Build machine learning models to predict customer churn.
- Develop an interactive Tableau dashboard for business stakeholders.
- Provide actionable business recommendations to improve customer retention.

---

# 🌟 Project Highlights

- ✅ End-to-End Data Science Project
- ✅ SQL Business Analysis
- ✅ Data Validation & Quality Assessment
- ✅ Python Data Cleaning Pipeline
- ✅ Exploratory Data Analysis (EDA)
- ⏳ Machine Learning Classification Models
- ⏳ Tableau Interactive Dashboard
- ⏳ Business Recommendations

---

# 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| MySQL | Database creation, SQL analysis, KPI reporting |
| Python | Data cleaning, EDA, Machine Learning |
| Jupyter Notebook | Data analysis & model development |
| Pandas | Data manipulation |
| NumPy | Numerical computation |
| Matplotlib | Data visualisation |
| Seaborn | Statistical visualisation |
| Scikit-learn | Machine Learning |
| Tableau | Business dashboard |
| Git & GitHub | Version control & project documentation |

---

# 📂 Project Structure

```text
Customer-Churn-Prediction/
│
├── data/
│   ├── raw/
│   │   └── synthetic_customer_churn_100k.csv
│   │
│   └── processed/
│       └── customer_churn_cleaned.csv
│
├── sql/
│   ├── 01_database_setup.sql
│   ├── 02_data_validation.sql
│   └── 03_business_analysis.sql
│
├── notebooks/
│   └── 01_Data_Cleaning_and_Validation.ipynb
│
├── reports/
│   ├── Day1_Business_Insights.md
│   └── Day2_DataCleaning.md
│
├── tableau/
│
├── models/
│
├── images/
│
└── README.md
```

---

# 📁 Dataset

**Dataset:** Synthetic Customer Churn Dataset

| Metric | Value |
|---------|--------|
| Records | 100,000 |
| Features | 9 |
| Target Variable | Churn |

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

# 📊 Dataset Quality Summary

| Metric | Result |
|---------|--------|
| Total Records | 100,000 |
| Missing Values | 0 |
| Duplicate Records | 0 |
| Negative TotalCharges | 265 (0.27%) |
| Outliers | Present only in TotalCharges |
| Data Types | Valid |
| Dataset Status | Ready for Exploratory Data Analysis |

---

# 📅 Project Progress

## ✅ Phase 1 – SQL Database & Business Analysis

### Database Setup

- Created MySQL database.
- Created Customers table.
- Imported 100,000 customer records.

### Data Validation

Performed comprehensive validation including:

- Total record verification
- Duplicate Customer ID check
- Missing value analysis
- Data type validation
- Categorical value validation
- Numerical summary statistics
- Investigation of negative TotalCharges

### Business KPI Analysis

Calculated key business metrics including:

- Total Customers
- Overall Churn Rate
- Average Monthly Charges
- Average Total Charges
- Average Customer Tenure

---

## ✅ Phase 2 – Python Data Cleaning & Validation

### Data Import

- Connected MySQL with Python.
- Loaded dataset into Pandas DataFrame.

### Data Quality Assessment

Performed:

- Dataset shape analysis
- Data type verification
- Descriptive statistics
- Missing value analysis
- Duplicate record check
- Negative TotalCharges investigation

### Data Cleaning

- Removed CustomerID (identifier column)
- Performed outlier analysis
- Analysed feature distributions
- Generated correlation matrix
- Saved cleaned dataset for modelling

---

# 📈 Key Business Findings

## KPI 1 – Total Customers

- **100,000 Customers**

---

## KPI 2 – Overall Churn Rate

| Metric | Value |
|---------|--------|
| Total Customers | 100,000 |
| Churned Customers | 33,144 |
| Churn Rate | **33.14%** |

### Business Insight

Approximately **one in every three customers has churned**, indicating a significant customer retention challenge.

Future analysis will focus on identifying high-risk customer segments based on:

- Contract Type
- Payment Method
- Customer Tenure
- Monthly Charges
- Age Groups

---

# 📊 Data Cleaning Summary

During Python preprocessing:

- No missing values were detected.
- No duplicate records were found.
- Only **0.27%** of records contained negative TotalCharges.
- Outliers were observed only in TotalCharges and retained because they represent valid business behaviour.
- Correlation analysis confirmed expected relationships between numerical variables.

---

# 🚀 Project Roadmap

## ✅ Phase 1 — SQL Database & Business Analysis

- Database Creation
- Data Validation
- KPI Analysis

---

## ✅ Phase 2 — Data Cleaning & Validation

- Data Import
- Data Quality Assessment
- Outlier Analysis
- Distribution Analysis
- Correlation Analysis

---

## ⏳ Phase 3 — Exploratory Data Analysis

- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis
- Business Insights
- Customer Segmentation

---

## ⏳ Phase 4 — Machine Learning

- Data Preprocessing
- Feature Engineering
- Train/Test Split
- Classification Models
- Hyperparameter Tuning
- Model Evaluation

---

## ⏳ Phase 5 — Tableau Dashboard

- Executive Dashboard
- Churn KPIs
- Customer Segmentation
- Interactive Filters
- Business Dashboard

---

## ⏳ Phase 6 — Business Recommendations

- Churn Driver Analysis
- Customer Retention Strategies
- Business Recommendations
- Final Report

---

# 📌 Current Status

| Phase | Status |
|--------|--------|
| Database Setup | ✅ Completed |
| Data Validation | ✅ Completed |
| SQL Business Analysis | ✅ Completed |
| Python Data Cleaning | ✅ Completed |
| Exploratory Data Analysis | ⏳ In Progress |
| Feature Engineering | ⏳ Pending |
| Machine Learning | ⏳ Pending |
| Tableau Dashboard | ⏳ Pending |
| Business Recommendations | ⏳ Pending |

---

# 📈 Expected Deliverables

By the completion of this project, the repository will include:

- SQL Business Analysis
- Data Validation Reports
- Python Data Cleaning Notebook
- Exploratory Data Analysis Notebook
- Machine Learning Models
- Model Performance Comparison
- Feature Importance Analysis
- Tableau Dashboard
- Business Insights Report
- Final Recommendations

---

# 📬 Author

## Nihil John Sundar S

📍 Chennai, India

💼 Aspiring Data Scientist

🔗 LinkedIn: https://linkedin.com/in/nihil-john-3bab411b9

💻 GitHub: https://github.com/Nihiljohn75

---

# ⭐ Repository Status

This repository documents the complete lifecycle of an end-to-end Customer Churn Prediction project using SQL, Python, Machine Learning, and Tableau.

The project is being developed phase by phase, following an industry-standard data science workflow, with each stage documented through code, reports, and business insights.
