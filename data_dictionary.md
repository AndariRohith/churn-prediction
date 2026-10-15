# Data Dictionary — Telco Customer Churn Dataset

Column-level reference for `WA_Fn-UseC_-Telco-Customer-Churn.csv` (7,043 rows, 21 columns).

| Column Name | Description | Data Type | Possible Values | Notes |
| --- | --- | --- | --- | --- |
| customerID | Customer's unique ID | str | Unique alphanumeric ID (e.g., 7590-VHVEG) | Unique identifier; not useful for prediction. Usually dropped before model training. |
| gender | Customer's gender | str | Female, Male | Categorical feature representing the customer's gender. |
| SeniorCitizen | Whether customer is a senior citizen | int64 | 0 = No, 1 = Yes | Binary numerical feature (0 = No, 1 = Yes). |
| Partner | Whether customer has a partner/spouse | str | Yes, No | Binary categorical feature indicating marital/partner status. |
| Dependents | Whether customer has dependents | str | Yes, No | Binary categorical feature indicating whether the customer has dependents. |
| tenure | Number of months customer has stayed | int64 | 0–72 months | Numerical feature showing customer tenure in months. |
| PhoneService | Whether customer has phone service | str | Yes, No | Binary categorical feature indicating phone service availability. |
| MultipleLines | Whether customer has multiple phone lines | str | Yes, No, No phone service | Categorical feature; depends on PhoneService. |
| InternetService | Type of internet service | str | DSL, Fiber optic, No | Categorical feature indicating the type of internet service. |
| OnlineSecurity | Online security add-on | str | Yes, No, No internet service | Categorical feature; applicable only for customers with internet service. |
| OnlineBackup | Online backup add-on | str | Yes, No, No internet service | Categorical feature; applicable only for customers with internet service. |
| DeviceProtection | Device protection add-on | str | Yes, No, No internet service | Categorical feature; applicable only for customers with internet service. |
| TechSupport | Technical support add-on | str | Yes, No, No internet service | Categorical feature; applicable only for customers with internet service. |
| StreamingTV | Streaming TV service | str | Yes, No, No internet service | Categorical feature; applicable only for customers with internet service. |
| StreamingMovies | Streaming movies service | str | Yes, No, No internet service | Categorical feature; applicable only for customers with internet service. |
| Contract | Customer contract type | str | Month-to-month, One year, Two year | Important feature that may influence customer churn. |
| PaperlessBilling | Paperless billing enrollment | str | Yes, No | Binary categorical feature indicating paperless billing enrollment. |
| PaymentMethod | Payment method used | str | Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic) | Categorical feature representing the customer's payment method. |
| MonthlyCharges | Monthly amount billed | float64 | Continuous numeric values (approximately 18.25–118.75) | Continuous numerical feature representing monthly billing amount. |
| TotalCharges | Total amount billed over customer tenure | str | Continuous numeric values stored as strings (contains blank values) | Stored as string; convert to numeric and handle blank values before analysis. |
| Churn | Whether customer left the company (Target Variable) | str | Yes, No | Target variable indicating whether the customer left the company. |
