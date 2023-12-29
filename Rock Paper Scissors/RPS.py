print("Welcome to ROCK, PAPER, SCISSORS!!!!!!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ls = [rock, paper, scissors]
print("User mode")
user = int(input("Enter Your choice: 0-Rock, 1-Paper, 2-Scissors: "))
print(ls[user])
print("Computer mode")
import random

n = len(ls)

choice = random.randint(0, n - 1)
print(ls[choice])

if ((user == 0 and choice == 0) or (user == 1 and choice == 1)
        or (user == 2 and choice == 2)):
    print("Draw")

elif ((user == 0 and choice == 1)):
    print("Computer wins")

elif ((user == 0 and choice == 2)):
    print("User wins")

elif ((user == 1 and choice == 0)):
    print("User wins")

elif ((user == 1 and choice == 2)):
    print("Computer wins")

elif ((user == 2 and choice == 0)):
    print("Computer wins")

elif ((user == 2 and choice == 1)):
    print("User wins")

else:
    print("Invalid Input. GAME OVER")

print("GAME OVER! Thank you for playing!")

