import pandas as pd
from flask import Flask, jsonify, request
import joblib
import sys

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    req = request.get_json()
    input_data = req['data']
    input_data_df = pd.DataFrame.from_dict(input_data)

    model = joblib.load('fraud_detection_model.pkl')
    
    # Preprocessing
    # scale_obj = joblib.load('scale.pkl')

    # input_data_scaled = scale_obj.transform(input_data_df)

    # print(input_data_scaled)

    # Making predictions with the loaded model
    prediction = model.predict(input_data_df)

    if prediction[0] == 1:
        fraud_type = 'Fraudulent transaction'
    else:
        fraud_type = 'Not fraudulent'
    
    return jsonify({'output': {'fraud_type': fraud_type}})

# Homepage
@app.route('/')
def home():
    return 'Welcome to the Fraud Detection Web App (FFDA II)'

# write the main function
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # incase a command line port argument is specified use it as default port
    except:
        port = 5200 # if not use this
    print(sys.argv)
    app.run(port = port, debug = True)
