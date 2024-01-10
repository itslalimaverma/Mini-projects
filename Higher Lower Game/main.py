from art import logo, vs
from game_data import data
from replit import clear
import random

print(logo)
print("Welcome to the Higher Lower Game!")
print("Guess who has more followers on Instagram!")
print("Let's start!")

length = len(data)

def game():
    score = 0
    game_over = False

    while not game_over:
        player_choice = random.randint(0, length - 1)
        player_choice_name = data[player_choice]['name']
        player_choice_description = data[player_choice]['description']
        player_choice_country = data[player_choice]['country']
        player_choice_followers = data[player_choice]['follower_count']

        print(f"Compare A: {player_choice_name}, a/an {player_choice_description}, from {player_choice_country}.")
        print(vs)

        player_choice2 = random.randint(0, length - 1)
        while player_choice == player_choice2:
            player_choice2 = random.randint(0, length - 1)

        player_choice2_name = data[player_choice2]['name']
        player_choice2_description = data[player_choice2]['description']
        player_choice2_country = data[player_choice2]['country']
        player_choice2_followers = data[player_choice2]['follower_count']

        print(f"Against B: {player_choice2_name}, a/an {player_choice2_description}, from {player_choice2_country}.")

        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

        if (user_input == 'A' and player_choice_followers > player_choice2_followers) or (user_input == 'B' and player_choice2_followers > player_choice_followers):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

        if not game_over:
            print("Next round...")
            clear()

    play_again = input("Do you want to play again? Type 'Y' or 'N': ").upper()
    if play_again == 'Y':
        clear()
        game()
    else:
        print("Thanks for playing!")

game()
