# Financial Fraud Detection Model
![image](https://www.nice.com/engage/blog/wp-content/webp-express/webp-images/doc-root/engage/blog/wp-content/uploads/2019/11/Blog-682X325-83.png.webp)

Fraud detection is a set of activities undertaken to prevent money or property from being obtained through false pretenses. Fraud detection is applied to many industries such as banking or insurance. In banking, fraud may include forging checks or using stolen credit cards. Other forms of fraud may involve exaggerating losses or causing an accident with the sole intent for the payout.
With an unlimited and rising number of ways someone can commit fraud, detection can be difficult to accomplish. Activities such as reorganization, downsizing, moving to new information systems or encountering a cybersecurity breach could weaken an organization's ability to detect fraud. This means techniques such as real-time monitoring for frauds is recommended. Organizations should look for fraud in financial transactions, location, devices used, initiated sessions and authentication systems.

### Fraud Detection Techniques
Fraud is typically an act which involves many repeated methods; making searching for patterns a general focus for fraud detection. For example, data analysts can prevent insurance fraud by making algorithms to detect patterns and anomalies. Statistical data analysis techniques include the use of:
* Calculating statistical parameters
* Regression analysis
* Probability distributions and models.
* Data Matching

A.I techniques used to detect fraud include the use of:
* Data mining- Which can classify, group and segment data to search through up to millions of transactions to find patterns and detect fraud.
* Neural networks- Which can learn suspicious looking patterns, and use those patterns to detect them further.
* Machine learning- Which can automatically identify characteristics found in fraud.
* Pattern recognition- Which can detect classes, clusters and patterns of suspicious behavior.

For the purpose of this project, I focused on the A.I techniques of fraud detection, in particular Machine learning using Decision Tree Model.

### [The Dataset](https://github.com/Josiah-Jovido/Fraud_detection/tree/main/Datasets)

There is a lack of public available datasets on financial services and specially in the emerging mobile money transactions domain. Part of the problem is the intrinsically private nature of financial transactions, that leads to no publicly available datasets. As such the dataset used for this analysis was generated using PaySim. PaySim uses aggregated data from the private dataset to generate a synthetic dataset that resembles the normal operation of transactions and injects malicious behaviour to later evaluate the performance of fraud detection methods.
PaySim simulates mobile money transactions based on a sample of real transactions extracted from one month of financial logs from a mobile money service implemented in an African country. The original logs were provided by a multinational company, who is the provider of the mobile financial service which is currently running in more than 14 countries all around the world.

### The Models([fraud_detection_model](https://github.com/Josiah-Jovido/Fraud_detection/blob/main/Fraud_detection_model.ipynb), [app.py](https://github.com/Josiah-Jovido/Fraud_detection/blob/main/app.py))

The Model was built using Decision tree classifier, my preference as to this was from the results obtained from the model(app.py). App.py is a web based machine learning algorithm that runs comparison between different machine learning models and draws suggestion on the right model to use based on the accuracy score. I built the app using the streamlit library. The [requirement.txt](https://github.com/Josiah-Jovido/Fraud_detection/blob/main/requirements.txt) file for running the web based app can be found in the repo.
After building and testing the model which worked sufficiently well, the model was saved in a pickle format for reuse. Next, i created a flask web app ([flask_app.py](https://github.com/Josiah-Jovido/Fraud_detection/blob/main/flask_app.py)) for easy accessibilty of the model for running predictions. The requests were made on postman, find below the steps for running a request on postman. I successfully established a model that can predict fraudulent transactions from a financial data. 

### Deployment
After building the model and running on flask, i took the project a step further by deploying the model in a production environment. This was done using Docker. Docker is a great tool for light weight containerization and deployment. I started off by creating a [requirements_1.txt](https://github.com/Josiah-Jovido/Fraud_detection/blob/main/requirements_1.txt) file for running the flask app, then i wrapped the command in a [Dockerfile](https://github.com/Josiah-Jovido/Fraud_detection/blob/main/Dockerfile) before deployment. The steps i took for deploying on docker can be found below. Through this, you can easily run the FFDA II model on any machine.

### Steps to run the web app
Firstly, **Create** a conda virtual environment:
```
conda create -n lazypredict python=3.7.9
```
Secondly, **Activate** the created lazypredict env with:
```
conda activate lazypredict
```
Thirdly, **Install** the requirements.txt file using pip:
```
pip install -r requirements.txt
```
To **run** the app:
```
streamlit run app.py
```
## The Web App
![image](https://i.ibb.co/jV8YzYv/Screenshot-174.png)

### Steps to run the Flask App
**Create** a Python Virtual Env
```
python3 -m virtualenv flask
```
**Activate** the virtualenv
```
source flask/bin/activate
```
**Install** Packages
```
pip install flask, pandas, sklearn, joblib
```
**Run** flask app
```
python3 flask_app.py
```
## The Flask App
![image](https://i.ibb.co/wdtmPJB/Screenshot-176.png)

![image](https://i.ibb.co/tQKRgxg/Screenshot-175.png)

### Steps to make requests on postman
NB: Set the method type to **'POST'**

In the url box input 
```
http://127.0.0.1:5200/predict
```
The body format to query the data is
```
{
    "data": [
        {
            "step": 1,
            "amount": 9839.64,
            "oldbalanceOrig": 170136.0,
            "newbalanceOrig": 160296.36,
            "oldbalanceDest": 0.0,
            "newbalanceDest": 0.0,
            "balancediffOrig": -9839.64,
            "balancediffDest": 0.0,
            "merchant": 1,
            "type_CASH_IN": 0,
            "type_CASH_OUT": 0,
            "type_DEBIT": 0,
            "type_PAYMENT": 1,
            "type_TRANSFER": 0
        }
    ]
}
```

### Steps to deploy on Docker
**Build** an image from the Dockerfile in the PWD
```
docker build -t fraud_detection_class:1.0 .
```
**Run** the container
```
docker run -d -p 6000:5200 fraud_detection_class:1.0
```
Once the container is running you can now query on postman. The new port code for running on postman will be **6000**

#### Find the hosted app on heroku [here](https://ffda.herokuapp.com/)
