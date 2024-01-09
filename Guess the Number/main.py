from art import logo
import random
easy_level_turns = 10
hard_level_turns = 5
def actual_answer(guess,answer,turns):
  if guess<answer:
    print("Too low")
  elif guess>answer:
    print("Too high")
  else:
    print(f"You got it! The answer was {answer}.")
  
def difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy_level_turns
  elif level=="hard":
    return hard_level_turns
  else:
    print("Invalid choice")

def game():
  print(logo)
  print("WELCOME TO THE NUMBER GUESSING GAME!")
  print("I'm thinking of a number between 1 and 100.")
  choose=difficulty();
  player_choice=random.randint(1,100)
  guess=0
  while guess!=player_choice:
    print(f"You have {choose} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    actual_answer(guess,player_choice,choose)
    choose-=1
    if choose==0:
      print("You've run out of guesses, you lose.")
      return
    elif guess!=player_choice:
      print("Guess again.")
game()
  
  