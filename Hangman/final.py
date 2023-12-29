import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

length = len(word_list)
word = random.randint(0, length - 1)
chosen_word = word_list[word]
#print(chosen_word)
word_length = len(chosen_word)
end_of_game = False
lives = 6
display = ["_" for _ in range(word_length)]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    else:
        for i in range(word_length):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = letter

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print("The Word was: ",chosen_word)

        Joining=''.join(display)
        print("The final Word is : ",Joining)

        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])
