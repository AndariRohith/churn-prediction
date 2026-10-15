# Customer Churn Prediction

A machine learning project that predicts whether a telecom customer is likely to churn (leave the company), with a Streamlit web app for making predictions.

**Live demo:** _add your Streamlit app link here after deploying_

## Overview

- **Problem:** Predict customer churn from account, service, and billing information.
- **Dataset:** [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (`WA_Fn-UseC_-Telco-Customer-Churn.csv`), 7,043 customers with 21 columns.
- **Model:** XGBoost classifier inside a scikit-learn `Pipeline` with a `ColumnTransformer` for preprocessing.
- **Accuracy:** about 0.80 on the held-out test set.
- **App:** Streamlit form that takes customer details and shows whether the customer will stay or churn.

## Project Structure

```
data_science_project/
├── churn_analysis_v1.ipynb                # EDA, preprocessing, model training
├── churn_model.pkl                        # Saved pipeline (preprocessing + XGBoost)
├── predictions.py                         # Streamlit app
├── requirements.txt                       # Python dependencies
├── data_dictionary.md                     # Description of each column
├── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Dataset
└── README.md
```

## How the Model Works

The saved file `churn_model.pkl` is a single scikit-learn pipeline:

```
raw customer data -> ColumnTransformer (encoding / scaling) -> XGBoost -> prediction
```

Because preprocessing is inside the pipeline, the app passes raw values (for example `"Month-to-month"`) and no manual transformation is needed.

The model uses these 19 input features (`customerID` and `Churn` are removed):

`gender`, `SeniorCitizen`, `Partner`, `Dependents`, `tenure`, `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `Contract`, `PaperlessBilling`, `PaymentMethod`, `MonthlyCharges`, `TotalCharges`

See `data_dictionary.md` for details on each column.

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd data_science_project
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The model was trained with **Python 3.14**, numpy 2.5.0, scikit-learn 1.9.0 and xgboost 3.4.1. Pickle files depend on library versions, so use the versions pinned in `requirements.txt`.

### 3. Run the app

```bash
python -m streamlit run predictions.py
```

The app opens at `http://localhost:8501`.

## Using the App

1. Fill in the customer details (demographics, services, billing).
2. Click **Churn Test Result**.
3. The app shows whether the customer is likely to stay or churn.

**Note:** keep the inputs consistent. If *Phone Service* is "No", set *Multiple Lines* to "No phone service". If *Internet Service* is "No", set the internet add-ons (Online Security, Online Backup, Device Protection, Tech Support, Streaming TV, Streaming Movies) to "No internet service".

## Retraining the Model

Open `churn_analysis_v1.ipynb`, run all cells, and the final cell saves a new `churn_model.pkl`. Always retrain and run the app in the same environment so library versions match.

## Deployment

The app can be deployed for free on [Streamlit Community Cloud](https://share.streamlit.io):

1. Push the project to a GitHub repository (including `churn_model.pkl` and `requirements.txt`).
2. Sign in to Streamlit Community Cloud with GitHub.
3. Choose **New app**, select the repository, and set the main file to `predictions.py`.
4. Click **Deploy**.

## Tech Stack

Python, pandas, NumPy, scikit-learn, XGBoost, Streamlit

## Author

_Your name_