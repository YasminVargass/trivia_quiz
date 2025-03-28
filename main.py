from question_model import Question
from questions import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

def generate_question():
    for questions in question_data:
        question_text = questions["question"]
        question_answer = questions["correct_answer"]
        question = Question(question_text, question_answer)
        question_bank.append(question)

generate_question()
quiz = QuizBrain(question_bank)
window = QuizInterface(quiz)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")

