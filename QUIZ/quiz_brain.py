class Quiz:
    def __init__(self,q_list):
        self.quesnum=0
        self.ques_list=q_list
        self.score=0

    def check_ans(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score+=1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.quesnum}")
        print("\n")


    def still_has_questions(self):
        if self.quesnum < len(self.ques_list):
            return True
        else:
            return False

    def next_question(self):
        current = self.ques_list[self.quesnum]
        self.quesnum += 1
        user_answer = input(f"Q.{self.quesnum}:{current.text}(True/False)")
        self.check_ans(user_answer, current.ans)

