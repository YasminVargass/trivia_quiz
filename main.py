import requests
import json


def generate_quiz():
    request = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
    data_quiz = request.json()
        
    try:
        with open("data.py","r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data =[]
        with open ("data.py", "w") as data_file:
            json.dump(data, data_file, indent=4)
    data.update(data_quiz)

    with open ("data.py", "w") as data_file:
        json.dump(data, data_file, indent=4)
     

generate_quiz()