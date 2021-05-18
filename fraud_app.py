import streamlit as st
import pandas as pd
from sklearn import datasets
import joblib

# App Title
st.title('Financial Fraud Detection App')
st.markdown('''
The FFDA II Web app was build using streamlit library \n
Authored by: Josiah Oborekanhwo \n
[Github](https://github.com/Josiah-Jovido)
''')

# Sidebar
st.sidebar.header('User Input Parameters')

def user_input_features():
    step = st.sidebar.slider('Step', 1, 95, 20)
    #type = st.sidebar.select_slider('Type', options=[1,2,3,4,5])
    amount = st.sidebar.slider('Amount', 1, 10000, 5000)
    oldbalanceOrig = st.sidebar.slider('Old Balance Origin', 0, 3890, 1000)
    newbalanceOrig = st.sidebar.slider('New Balance Origin', 0, 3890, 2000)
    oldbalanceDest = st.sidebar.slider('Old Balance Destination', 0, 4210, 500)
    newbalanceDest = st.sidebar.slider('New Balance Destination', 0, 4220, 300)
    balancediffOrig = st.sidebar.slider('Balance Diff Origin', 0, 1800, 50)
    balancediffDest = st.sidebar.slider('Balance Diff Destination', 0, 3884, 150)
    merchant = st.sidebar.select_slider('Merchant', options=[0,1])
    type_CASH_IN = st.sidebar.select_slider('Type of cash IN', options=[0,1])
    type_CASH_OUT = st.sidebar.select_slider('Type of cash OUT', options=[0,1])
    type_DEBIT = st.sidebar.select_slider('Type of Debit', options=[0,1])
    type_PAYMENT = st.sidebar.select_slider('Type of Payment', options=[0,1])
    type_TRANSFER = st.sidebar.select_slider('Type of Transfer', options=[0,1])
    data = {'step': step,
            'amount': amount,
            'oldbalanceOrig': oldbalanceOrig,
            'newbalanceOrig': newbalanceOrig,
            'oldbalanceDest': oldbalanceDest,
            'newbalanceDest': newbalanceDest,
            'balancediffOrig': balancediffOrig,
            'balancediffDest': balancediffDest,
            'merchant': merchant,
            'type_CASH_IN': type_CASH_IN,
            'type_CASH_OUT': type_CASH_OUT,
            'type_DEBIT': type_DEBIT,
            'type_PAYMENT': type_PAYMENT,
            'type_TRANSFER': type_TRANSFER}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Main page
st.subheader('User Input parameters')
st.write(df)

# Load the model
loaded_model = joblib.load('fraud_detection_model.pkl')
prediction = loaded_model.predict(df)
if prediction[0] == 1:
    fraud_type = 'Fraudulent transaction'
else:
    fraud_type = 'Not fraudulent'

st.subheader('Model Prediction')
#code('if prediction[0] == 1: fraud_type="Fraudulent transaction"; else: fraud_type="Not fraudulent"')
st.write(fraud_type)
