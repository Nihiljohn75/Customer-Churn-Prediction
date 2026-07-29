/*
===========================================================
Project : Customer Churn Prediction
File    : 02_data_validation.sql
Author  : Nihil John Sundar S
Purpose : Validate data quality before business analysis
===========================================================
*/

USE Customer_churn;

-- =========================================================
-- Validation 1 : Total Records
-- Purpose:
-- Verify that all records have been imported successfully.
-- =========================================================

SELECT COUNT(*) AS Total_Customers
FROM customers;

-- =========================================================
-- Validation 2 : Sample Data Preview
-- Purpose:
-- Display the first 10 records for a quick inspection.
-- =========================================================

SELECT *
FROM customers
LIMIT 10;

-- =========================================================
-- Validation 3 : Duplicate Customer IDs
-- Purpose:
-- Ensure each customer has a unique identifier.
-- =========================================================

SELECT
    CustomerID,
    COUNT(*) AS Duplicate_Count
FROM customers
GROUP BY CustomerID
HAVING COUNT(*) > 1;

-- =========================================================
-- Validation 4 : Missing Values
-- Purpose:
-- Check for NULL values in important columns.
-- =========================================================

SELECT *
FROM customers
WHERE Age IS NULL
   OR Gender IS NULL
   OR Tenure IS NULL
   OR MonthlyCharges IS NULL
   OR Contract IS NULL
   OR PaymentMethod IS NULL
   OR TotalCharges IS NULL
   OR Churn IS NULL;

-- =========================================================
-- Validation 5 : Category Distribution
-- Purpose:
-- Verify categorical values.
-- =========================================================

SELECT Gender, COUNT(*) AS Total_Customers
FROM customers
GROUP BY Gender;

SELECT Contract, COUNT(*) AS Total_Customers
FROM customers
GROUP BY Contract;

SELECT PaymentMethod, COUNT(*) AS Total_Customers
FROM customers
GROUP BY PaymentMethod;

SELECT Churn, COUNT(*) AS Total_Customers
FROM customers
GROUP BY Churn;

-- =========================================================
-- Validation 6 : Numerical Column Statistics
-- Purpose:
-- Check minimum, maximum and average values.
-- =========================================================

SELECT
    MIN(Age) AS Min_Age,
    MAX(Age) AS Max_Age,
    AVG(Age) AS Avg_Age
FROM customers;

SELECT
    MIN(Tenure) AS Min_Tenure,
    MAX(Tenure) AS Max_Tenure,
    AVG(Tenure) AS Avg_Tenure
FROM customers;

SELECT
    MIN(MonthlyCharges) AS Min_MonthlyCharges,
    MAX(MonthlyCharges) AS Max_MonthlyCharges,
    AVG(MonthlyCharges) AS Avg_MonthlyCharges
FROM customers;

SELECT
    MIN(TotalCharges) AS Min_TotalCharges,
    MAX(TotalCharges) AS Max_TotalCharges,
    AVG(TotalCharges) AS Avg_TotalCharges
FROM customers;

-- =========================================================
-- Validation 7 : Negative TotalCharges
-- Purpose:
-- Identify invalid TotalCharges values.
-- =========================================================

SELECT COUNT(*) AS Negative_TotalCharges
FROM customers
WHERE TotalCharges < 0;

SELECT
    CustomerID,
    Tenure,
    MonthlyCharges,
    TotalCharges,
    Gender,
    Churn
FROM customers
WHERE TotalCharges < 0;