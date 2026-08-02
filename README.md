# 📊 Customer Churn Prediction

An end-to-end Data Science project to analyze customer churn using **MySQL, Python, Machine Learning, and Tableau**. This project follows an industry-standard workflow covering database design, data validation, exploratory data analysis, predictive modeling, and business intelligence dashboards.

---

# 🎯 Project Objective

Customer churn is one of the biggest challenges faced by subscription-based businesses. The objective of this project is to:

- Analyze customer behavior using SQL.
- Perform comprehensive data validation and quality assessment.
- Explore customer churn patterns through Exploratory Data Analysis (EDA).
- Build and compare multiple machine learning models to predict customer churn.
- Identify the key factors driving customer churn.
- Develop an interactive Tableau dashboard for business stakeholders.
- Provide actionable business recommendations to improve customer retention.

---

# 🌟 Project Highlights

- ✅ End-to-End Data Science Project
- ✅ SQL Database Design & Business Analysis
- ✅ Data Validation & Quality Assessment
- ✅ Python Data Cleaning Pipeline
- ✅ Exploratory Data Analysis (EDA)
- ✅ Machine Learning Model Development
- ✅ Hyperparameter Tuning
- ✅ Feature Importance Analysis
- ✅ Model Serialization using Pickle
- ⏳ Tableau Dashboard
- ⏳ Business Recommendations

---

# 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| MySQL | Database creation, SQL analysis & KPI reporting |
| Python | Data cleaning, EDA & Machine Learning |
| Jupyter Notebook | Data analysis & model development |
| Pandas | Data manipulation |
| NumPy | Numerical computation |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine Learning |
| XGBoost | Gradient Boosting Classification |
| Tableau | Interactive Dashboard |
| Pickle | Model Serialization |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```text
Customer-Churn-Prediction
│
├── data
│   ├── raw
│   │   └── synthetic_customer_churn_100k.csv
│   │
│   └── processed
│       └── customer_churn_cleaned.csv
│
├── sql
│   ├── 01_database_setup.sql
│   ├── 02_data_validation.sql
│   └── 03_business_analysis.sql
│
├── notebooks
│   ├── 01_Data_Cleaning.ipynb
│   ├── 02_EDA.ipynb
│   └── 03_Machine_Learning.ipynb
│
├── models
│   ├── customer_churn_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── reports
│   ├── Day1_Business_Insights.md
│   └── Day2_DataCleaning.md
│
├── tableau
│
├── images
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📁 Dataset

| Metric | Value |
|---------|------|
| Dataset | Synthetic Customer Churn Dataset |
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
| Dataset Status | Ready for Machine Learning |

---

# 📈 Exploratory Data Analysis

EDA included:

- Univariate Analysis
- Bivariate Analysis
- Correlation Analysis
- Outlier Analysis
- Feature Distribution Analysis
- Churn Pattern Analysis

### Key Findings

- Month-to-month customers showed the highest churn.
- Customers with shorter tenure were more likely to churn.
- Higher monthly charges were associated with higher churn.
- Gender showed minimal influence on churn.

---

# 🤖 Machine Learning

## Data Preprocessing

- Removed CustomerID
- One-Hot Encoding
- Label Encoding
- Standard Scaling
- Train-Test Split (80:20)

## Models Evaluated

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- Tuned XGBoost (GridSearchCV)

---

## 📊 Model Performance

| Model | Accuracy | ROC-AUC | F1 Score |
|--------|----------|----------|----------|
| Tuned XGBoost | **75.95%** | **0.802** | **0.605** |
| XGBoost | 75.31% | 0.797 | 0.592 |
| Random Forest | 73.43% | 0.789 | 0.554 |
| Logistic Regression | 72.48% | 0.771 | 0.525 |
| Decision Tree | 68.15% | 0.641 | 0.521 |

### Final Model

**Tuned XGBoost** was selected as the final model due to its superior performance across Accuracy, ROC-AUC, F1 Score, and Cross-Validation Accuracy.

---

# 📈 Feature Importance

The trained XGBoost model identified the following features as the most influential:

1. Tenure
2. Contract (Two Year)
3. Contract (One Year)
4. Monthly Charges

These variables account for the majority of the model's predictive power, indicating that customer loyalty and contract commitment are the primary drivers of churn.

---

# 💾 Saved Models

The following artifacts are included for future deployment:

- customer_churn_model.pkl
- scaler.pkl
- label_encoder.pkl

---

# 🚀 Project Roadmap

| Phase | Status |
|--------|--------|
| SQL Database & Business Analysis | ✅ Completed |
| Data Cleaning & Validation | ✅ Completed |
| Exploratory Data Analysis | ✅ Completed |
| Feature Engineering | ✅ Completed |
| Machine Learning | ✅ Completed |
| Hyperparameter Tuning | ✅ Completed |
| Tableau Dashboard | ⏳ In Progress |
| Business Recommendations | ⏳ Pending |

---

# 📊 Current Status

| Phase | Status |
|--------|--------|
| Database Setup | ✅ Completed |
| SQL Analysis | ✅ Completed |
| Data Cleaning | ✅ Completed |
| Exploratory Data Analysis | ✅ Completed |
| Machine Learning | ✅ Completed |
| Model Comparison | ✅ Completed |
| Hyperparameter Tuning | ✅ Completed |
| Feature Importance | ✅ Completed |
| Model Serialization | ✅ Completed |
| Tableau Dashboard | ⏳ In Progress |

---

# 📈 Business Insights

- Approximately **33.14%** of customers have churned.
- Customer tenure is the strongest predictor of churn.
- Long-term contracts significantly reduce churn.
- Monthly charges play an important role in customer retention.
- Demographic features have relatively little impact compared to behavioral features.

---

# 📬 Author

**Nihil John Sundar S**

📍 Chennai, India

💼 Aspiring Data Scientist

🔗 LinkedIn: https://linkedin.com/in/nihil-john-3bab411b9

💻 GitHub: https://github.com/Nihiljohn75

---

# ⭐ Repository Status

This repository documents the complete lifecycle of an end-to-end Customer Churn Prediction project using **SQL, Python, Machine Learning, XGBoost, and Tableau**.

The project follows an industry-standard data science workflow and demonstrates database management, data preprocessing, exploratory analysis, predictive modeling, model evaluation, and business intelligence reporting.
