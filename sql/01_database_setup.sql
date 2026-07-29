/*
===========================================================
Project : Customer Churn Prediction
File    : 03_business_analysis.sql
Author  : Nihil John Sundar S
Purpose : Business KPI and Customer Churn Analysis
===========================================================
*/
Create database Customer_churn;
use Customer_churn;
create table Customers (
customerID int primary key,
Age int,
Gender varchar(10),
Tenure Int,
Monthlycahrges decimal(10,2),
Contract varchar(30),
PaymentMethod Varchar(50),
TotalCharges decimal(10,2),
Churn varchar(5)
);

