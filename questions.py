import requests

params = {
    "amount": "10",
    "type": "boolean"
}

request = requests.get(url="https://opentdb.com/api.php?", params= params)
request.raise_for_status()
data = request.json()

question_data = data["results"]