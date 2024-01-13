from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for i in question_data:
    question_text=i["text"]
    question_ans=i["answer"]
    newq=Question(question_text,question_ans)
    question_bank.append(newq)

# print(question_bank)

quiz=Quiz(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score: {quiz.score}/{quiz.quesnum}")



