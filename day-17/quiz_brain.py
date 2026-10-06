class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        for item in self.question_list:
            self.question_number += 1
            answer = input(f"Q{self.question_number}: {item.text} (True/False)?:")
            self.check_answer(answer, item.answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print(f"You got it right! The correct answer is {correct_answer}")
            self.score += 1
        else:
            print(f"You got it wrong! The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
