# Customer Churn Prediction

Predicts whether a telecom customer is likely to churn (leave the company), using an XGBoost model served through a Streamlit web app.

**Live demo:** [rossi-telco-churn-prediction-app.streamlit.app](https://rossi-telco-churn-prediction-app.streamlit.app/)

> The free Streamlit plan puts apps to sleep when nobody is using them. If you see a "Wake up" button, click it and wait about a minute.

## Overview

| | |
|---|---|
| **Problem** | Predict customer churn from account, service, and billing information |
| **Dataset** | [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn): 7,043 customers, 21 columns |
| **Model** | XGBoost classifier inside a scikit-learn `Pipeline` with a `ColumnTransformer` for preprocessing |
| **Accuracy** | About 0.80 on the held-out test set |
| **App** | Streamlit form that returns whether the customer will stay or churn |

## Project Structure

```
churn-prediction/
├── churn_analysis_v1.ipynb                # EDA, preprocessing, model training
├── churn_model.pkl                        # Saved pipeline (preprocessing + XGBoost)
├── predictions.py                         # Streamlit app
├── requirements.txt                       # Python dependencies
├── data_dictionary.md                     # Description of each column
├── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Dataset
├── .gitignore
└── README.md
```

## How the Model Works

The file `churn_model.pkl` holds one scikit-learn pipeline:

```
raw customer data -> ColumnTransformer (preprocessing) -> XGBoost -> prediction
```

Preprocessing lives inside the pipeline, so the app sends raw values such as `"Month-to-month"` and no manual transformation is needed.

### Input features

The model takes 19 features (`customerID` and `Churn` are excluded):

| Group | Features |
|---|---|
| Demographics | `gender`, `SeniorCitizen`, `Partner`, `Dependents` |
| Account | `tenure`, `Contract`, `PaperlessBilling`, `PaymentMethod` |
| Services | `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies` |
| Charges | `MonthlyCharges`, `TotalCharges` |

See `data_dictionary.md` for details on each column.

## Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/AndariRohith/churn-prediction.git
cd churn-prediction
```

**2. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

The model was trained with Python 3.14, numpy 2.5.0, scikit-learn 1.9.0 and xgboost 3.4.1. Pickle files depend on library versions, so keep the versions pinned in `requirements.txt`.

**3. Start the app**

```bash
python -m streamlit run predictions.py
```

The app opens at `http://localhost:8501`.

## Using the App

1. Fill in the customer details (demographics, services, billing).
2. Click **Churn Test Result**.
3. The app shows whether the customer is likely to stay or churn.

**Keep the inputs consistent.** The form does not block impossible combinations, so choose them yourself:

- If *Phone Service* is "No", set *Multiple Lines* to "No phone service".
- If *Internet Service* is "No", set Online Security, Online Backup, Device Protection, Tech Support, Streaming TV and Streaming Movies to "No internet service".

## Retraining the Model

Open `churn_analysis_v1.ipynb` and run all cells to train the model and save a new `churn_model.pkl`. Train and run the app in the same environment, with the same library versions, or the pickle may fail to load.

## Deployment

The app is deployed on [Streamlit Community Cloud](https://share.streamlit.io) straight from this repository (`main` branch, main file `predictions.py`). Every push to `main` redeploys it automatically.

## Tech Stack

Python, pandas, NumPy, scikit-learn, XGBoost, Streamlit

## Limitations

This is a learning project. The model was trained on one public dataset and should not be used for real business decisions without further validation.

## Author

**Andari Rohith**: [GitHub](https://github.com/AndariRohith)