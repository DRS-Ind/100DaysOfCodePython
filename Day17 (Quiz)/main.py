from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


# question bank for prepared questions
# question_bank = [Question(text=question_row["text"], answer=question_row["answer"]) for question_row in question_data]

# question bank for questions from open trivia DB
question_bank = [Question(text=question_row["question"], answer=question_row["correct_answer"])
                 for question_row in question_data]

# fill quiz brain with questions
quiz = QuizBrain(question_list=question_bank)

# start answering
while quiz.still_has_questions():
    quiz.next_question()

print(f"You have complete the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}")
