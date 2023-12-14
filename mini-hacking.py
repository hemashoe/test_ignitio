import requests

# Replace with your Flask app URL
url = "http://localhost:5000/add_to_cart"

# Replace with the illegal item you want to add
illegal_item = "gun"
data = {"item": illegal_item, "quantity": "1"}

response = requests.post(url, data=data)
print(response.status_code)
