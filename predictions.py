import pickle
import pandas as pd
import streamlit as st

# load the saved pipeline (preprocessing + model)
loaded_model = pickle.load(open("churn_model.pkl", "rb"))


# create a function for prediction
def churn_prediction(input_data):

    # the pipeline was trained on a DataFrame, so we need column names
    columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
               'PhoneService', 'MultipleLines', 'InternetService',
               'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
               'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
               'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges',
               'TotalCharges']

    # one row DataFrame
    input_df = pd.DataFrame([input_data], columns=columns)

    prediction = loaded_model.predict(input_df)
    print(prediction)

    if prediction[0] == 0:
        return 'The customer will stay'
    else:
        return 'The customer will churn'


def main():
    st.title("Customer Churn Prediction Web App")

    # input data
    gender = st.selectbox("Gender", ["Female", "Male"])
    SeniorCitizen = st.selectbox("Senior Citizen (0 = No, 1 = Yes)", [0, 1])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=100)
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check",
                                                    "Bank transfer (automatic)",
                                                    "Credit card (automatic)"])
    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
    TotalCharges = st.number_input("Total Charges", min_value=0.0)

    # prediction
    diagnosis = ""

    # creating button for prediction
    if st.button("Churn Test Result"):
        diagnosis = churn_prediction([gender, SeniorCitizen, Partner, Dependents, tenure,
                                      PhoneService, MultipleLines, InternetService,
                                      OnlineSecurity, OnlineBackup, DeviceProtection,
                                      TechSupport, StreamingTV, StreamingMovies, Contract,
                                      PaperlessBilling, PaymentMethod, MonthlyCharges,
                                      TotalCharges])
        st.success(diagnosis)


if __name__ == "__main__":
    main()