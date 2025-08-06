from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizGUI

# generate question bank
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# load quiz`s back-end with questions
quiz = QuizBrain(question_bank)

# start quiz gui
quiz_ui = QuizGUI(brain=quiz)
