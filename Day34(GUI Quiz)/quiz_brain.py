from html import unescape


class QuizBrain:

    def __init__(self, q_list: list):
        """
        Back-end for quiz.

        :param q_list: list with questions in Question class from inner module question_model.py
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        """
        Check if any questions are still in

        :return: True if it does, or False if it doesn't
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """
        Prepare next question in the list

        :return: question number + question text in string
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {unescape(self.current_question.text)}"

    def check_answer(self, user_answer: str):
        """
        Check user answer

        :param user_answer: True of False in string type
        :return: True if it's right False if it isn't
        """
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
