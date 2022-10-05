class Question():

    counter = 0

    def __init__(self, question, correct_answer, other_answers):
        self.question = question
        self.correct_answer = correct_answer
        self.other_answers = other_answers
        self.all_answer = self.add(self.correct_answer, self.other_answers)
        Question.counter += 1

    def add(self, a, b):
        b += [a]
        return b