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

### The Dataset

There is a lack of public available datasets on financial services and specially in the emerging mobile money transactions domain. Part of the problem is the intrinsically private nature of financial transactions, that leads to no publicly available datasets. As such the dataset used for this analysis was generated using PaySim. PaySim uses aggregated data from the private dataset to generate a synthetic dataset that resembles the normal operation of transactions and injects malicious behaviour to later evaluate the performance of fraud detection methods.
PaySim simulates mobile money transactions based on a sample of real transactions extracted from one month of financial logs from a mobile money service implemented in an African country. The original logs were provided by a multinational company, who is the provider of the mobile financial service which is currently running in more than 14 countries all around the world.

### The Models([fraud_detection_model](https://github.com/Josiah-Jovido/Fraud_detection/blob/main/Fraud_detection_model.ipynb), [app.py](https://github.com/Josiah-Jovido/Fraud_detection/blob/main/app.py))

The Model was built using Decision tree classifier, my preference as to this was from the results obtained from the model(app.py). App.py is a web based machine learning algorithm that runs comparison between different machine learning models and draws suggestion on the right model to use based on the accuracy score. I built the app using the streamlit library. The [requirement.txt](https://github.com/Josiah-Jovido/Fraud_detection/blob/main/requirements.txt) file for running the web based app can be found in the repo.
After building and testing the model which worked sufficiently well, the model was saved in a pickle format for reuse. I successfully established a model that can trace fraudulent transactions from a financial data. 

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
