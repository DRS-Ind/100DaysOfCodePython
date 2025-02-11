class QuizBrain:
    def __init__(self, question_list: list) -> None:
        """
        I'll make a quiz with your questions.
        :param question_list: takes the list of the questions
        """
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self) -> bool:
        """
        Check if the quiz still has questions to ask.
        :return: True or False
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> None:
        """
        Ask the question.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        """
        Check the answer.
        :param user_answer: user`s answer
        :param correct_answer: correct answer
        """
        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("No, you are wrong.")
        print(f"The correct answer was: {correct_answer}.\n"
              f"Your current score is : {self.score}/{self.question_number}\n\n")
