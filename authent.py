import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "query": "What is the best smartphone?",
    "product_descriptions": [
        "The latest iPhone with A17 chip and excellent camera.",
        "A budget-friendly Android phone with good performance."
    ]
}

response = requests.post(url, json=data)
print("Response:", response.json())
