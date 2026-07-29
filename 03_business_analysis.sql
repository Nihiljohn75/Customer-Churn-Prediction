-- =========================================================
-- KPI 1 : Total Customers
-- Business Question:
-- How many customers are available in the dataset?
-- =========================================================

SELECT COUNT(*) AS Total_Customers
FROM customers;

-- =========================================================
-- KPI 2 : Overall Churn Rate
--
-- Business Question:
-- What percentage of customers have churned?
--
-- Expected Output:
-- Total Customers
-- Churned Customers
-- Churn Rate
-- =========================================================

SELECT COUNT(*) AS Total_Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2) AS Churn_Rate
FROM customers;


-- =========================================================
-- KPI 3 : Average Monthly Charges
-- Business Question:
-- What is the average monthly amount paid by customers?
-- =========================================================

SELECT
ROUND(AVG(MonthlyCharges),2) AS Avg_Monthly_Charges
FROM customers;


-- =========================================================
-- KPI 4 : Average Customer Lifetime Value
-- Business Question:
-- What is the average total amount paid by customers?
-- =========================================================

SELECT
ROUND(AVG(TotalCharges),2) AS Avg_Total_Charges
FROM customers;


-- =========================================================
-- KPI 5 : Average Customer Tenure
-- Business Question:
-- What is the average customer tenure?
-- =========================================================

SELECT
ROUND(AVG(Tenure),2) AS Avg_Tenure
FROM customers;


-- =========================================================
-- Business Question 1
-- How are customers distributed across contract types?
-- =========================================================

SELECT
Contract,
COUNT(*) AS Customers
FROM customers
GROUP BY Contract
ORDER BY Customers DESC;


-- =========================================================
-- Business Question 2
-- Which contract type has the highest churn rate?
-- =========================================================

SELECT
Contract,
COUNT(*) AS Customers,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),
2
) AS Churn_Rate
FROM customers
GROUP BY Contract
ORDER BY Churn_Rate DESC;


SELECT
Gender,
COUNT(*) AS Customers,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),
2
) AS Churn_Rate
FROM customers
GROUP BY Gender;

SELECT
PaymentMethod,
COUNT(*) AS Customers,
ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2) AS Churn_Rate
FROM customers
GROUP BY PaymentMethod
ORDER BY Churn_Rate DESC;

SELECT
Contract,
ROUND(SUM(TotalCharges),2) AS Revenue
FROM customers
GROUP BY Contract
ORDER BY Revenue DESC;