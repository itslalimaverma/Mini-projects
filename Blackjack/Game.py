from art import logo
from replit import clear
import random
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  length=len(cards)
  dealt_card=random.randint(0,length-1)
  return cards[dealt_card]

  # cards_dealt1=deal_card()
# cards_dealt2=deal_card()
# print(cards_dealt1,cards_dealt2)


# print(user_cards)
# print(computer_cards)

def calculate_score(cards):
  #for a blackjack
  if sum(cards)==21 and len(cards)==2:
    return 0
    
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  user_cards=[]
  computer_cards=[]

  for i in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  game_over=False
  while not game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
  
    if user_score==0 or computer_score==0 or user_score>21:
      game_over=True
      print("BUST")
      print("Game Over")
    else:
      user_input=input("Do you want to deal another card? Type 'y' for yes and 'n' for no: ")
      if user_input=="y":
        user_cards.append(deal_card())
      else:
        game_over=True
  
  
  
  
  
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()



