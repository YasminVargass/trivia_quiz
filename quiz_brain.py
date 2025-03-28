from question_model import Question
from questions import question_data


class QuizBrain():
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list
    
    def next_question(self,):
        
        for numb_question in range(0, len(self.question_list)):
                current_question = self.question_list[self.question_number]
                user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
                self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
         return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
         if user_answer.lower() == correct_answer.lower():
              self.score += 1
              print("Correct")
         else:
              print("Incorrect")
    


