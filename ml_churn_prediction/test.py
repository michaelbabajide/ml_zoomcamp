import requests

url = 'http://localhost:9696/predict'

customer = {    
     "gender": "female",
     "seniorcitizen": 1,
     "partner": "no",
     "dependents": "yes",
     "phoneservice": "yes",
     "multiplelines": "yes",
     "internetservice": "fiber_optic",
     "onlinesecurity": "yes",
     "onlinebackup": "no",
     "deviceprotection": "yes",
     "techsupport": "yes",
     "streamingtv": "yes",
     "streamingmovies": "yes",
     "contract": "month-to-month",
     "paperlessbilling": "yes",
     "paymentmethod": "electronic_check",
     "tenure": 6,
     "monthlycharges": 124.2,
     "totalcharges": 1003.5
}

response = requests.post(url, json=customer).json()
print(response)
