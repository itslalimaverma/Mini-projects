print("WELCOME TO THE TIP CALCULATOR!")
bill = float(input("What was the total bill? : "))
tip = int(input("How much tip would you like to pay? (10,12,15):"))
Split = int(input("How many people to split the bill? :"))
percent = tip / 100
mul = bill * percent
total = bill + mul
split = total / Split
print(f"Each person should pay: {split:.2f}")