class Question:
    def __init__(self, text: str, answer: str) -> None:
        """
        Simple question model. Question. Answer.
        :param text: takes the question
        :param answer: takes the answer
        """
        self.text = text
        self.answer = answer
