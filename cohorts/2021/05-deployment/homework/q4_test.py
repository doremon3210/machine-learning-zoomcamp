
import requests

url = "http://localhost:9696/predict"

customer = {"contract": "two_year", "tenure": 1, "monthlycharges": 10}
respose = requests.post(url, json=customer).json()


print(respose)

