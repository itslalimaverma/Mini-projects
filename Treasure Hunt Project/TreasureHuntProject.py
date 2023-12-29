import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

dir1 = input("Do you want to go Right/Left: ")
if (dir1 == "Right" or dir1 == "right"):
    print("Nice choice, Let's move forward.")
    print(
        "Now the time is to decide whether you want to swim or wait for the doors."
    )
    dir2 = input("Do you want to swim or wait: ")
    if (dir2 == "Swim" or dir2 == "swim"):
        print("Cross the stream to unveil the next step.")
        time.sleep(1)
        print("You swam to the shore and saw a boat.")
        time.sleep(1)
        print("The boat takes you to the three doors of decision.")
        dir3 = input("Which door do you want to choose 1/2/3: ")
        if (dir3 == "1"):
            print("You chose the door with treasure.")
            print("You found the treasure and lived happily ever after.")
        elif (dir3 == "2"):
            print("You chose the door with a snake.")
            print("You lost the game.")
            print("Game Over.")
        else:
            print(
                "You came back to the starting point with Left direction. >_<")
    else:
        print(
            "If you chose to wait, How many years are you going to wait? 10,15,20?: "
        )
        dir4 = input("Enter the number: ")
        if dir4 == "10":
            print("You patiently waited for 10 years...")
            time.sleep(1)
            print(
                "As time passed, the world outside changed. When you finally emerged,"
            )
            time.sleep(1)
            print(
                "you found the cove shrouded in a mystical mist, the entrance seemingly sealed."
            )
            time.sleep(1)
            print(
                "In the silence, a faint whisper echoed: 'Patience unveils secrets; seek the moon's blessing.'"
            )
            time.sleep(1)
            print("But alas you found No treasure.")
            print("GAME OVER.")

        elif dir4 == "15":
            print("Fifteen years is quite a long time to wait...")
            time.sleep(1)
            print(
                "The passage of time brought changes to the cove. Emerging from your wait,"
            )
            time.sleep(1)
            print(
                "you noticed ancient runes now adorning the cave walls, pulsating with energy."
            )
            time.sleep(1)
            print(
                "Amongst the inscriptions, one stood out: 'Time is the key, seasons hold the truth.'"
            )
            time.sleep(1)
            print(
                "You found the treasure!!!! YIPEEEEE. And you lived happily ever after."
            )

        elif dir4 == "20":
            print(
                "Twenty years have passed, that's a significant commitment...")
            time.sleep(1)
            print(
                "Emerging after two decades, you found the cove transformed.")
            time.sleep(1)
            print(
                "The mystical barrier had dissipated, revealing a breathtaking sight:"
            )
            time.sleep(1)
            print(
                "A garden of celestial flora and a path paved with starlight leading to the treasure."
            )
            time.sleep(1)
            print(
                "Congratulations! You've discovered the legendary treasure of the Enchanted Cove! But you didn't live much After that."
            )

else:
    print("Oh! Don't worry, you still have a chance to redeem.")
    print("You've chosen the left path leading to a moonlit beach.")
    time.sleep(1)
    print("Approaching the glowing statue, you offer starlight.")
    offering = input("What do you offer to the glowing statue?: ")

    if offering.lower() == "starlight":
        print("The statue accepts your offering, revealing a hidden passage.")
        time.sleep(1)
        print("Descending through winding tunnels, you reach a vast chamber.")
        time.sleep(1)

        print("In its heart rests an ancient chest, radiating mystical light.")
        time.sleep(1)

        print("You've found the treasure of the Enchanted Cove!")
        print("Congratulations on completing the quest!")
    else:
        print("The offering doesn't suffice; the statue remains unchanged.")
        print("A distant melody catches your attention.")
        melody = input("What melody do you play or sing?: ")

        if melody.lower() == "whispering wind":
            print("The statue resonates with the 'Whispering Wind' melody.")
            time.sleep(1)
            print("A secret passage opens, leading to winding tunnels.")
            time.sleep(1)

            print("You emerge in a chamber housing the fabled treasure.")
            print(
                "Well done! You've discovered the Enchanted Cove's treasure!")
        else:
            print("The melody doesn't evoke a response.")
            print("Perhaps there's another way to uncover the treasure.")

