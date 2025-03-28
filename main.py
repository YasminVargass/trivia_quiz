import requests
import json
from question_model import Question
from questions import question_data
from quiz_brain import QuizBrain


question_bank = []

def generate_question():
    for questions in question_data:
        question_text = questions["text"]
        question_answer = questions["answer"]
        question = Question(question_text, question_answer)
        question_bank.append(question)

generate_question()
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

# def generate_quiz():
#     request = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
#     data_quiz = request.json()
        
#     try:
#         with open("data.py","r") as data_file:
#             data = json.load(data_file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         data = question_bank
#         with open ("data.py", "w") as data_file:
#             json.dump(data, data_file, indent=4)
#     data.update(data_quiz)

#     with open ("data.json", "w") as data_file:
#         json.dump(data, data_file, indent=4)
     

# generate_quiz()