class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        usr_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)")
        self.question_number += 1
        self.check_answer(usr_answer, current_question.answer)

    def check_answer(self, usr_answer, correct_answer):
        if usr_answer.lower() == correct_answer.lower():
            print("you got it right")
            self.score += 1
        else:
            print("Wrong")
        print(f"the correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()