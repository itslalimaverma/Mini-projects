from main import MENU as m
from main import resources as data
print("Welcome to Coffee-Coding Machine!")
profit=0
coffee_finished = False


def is_resource_sufficient(ingredients):
    for i in ingredients:
        if ingredients[i]>data[i]:
            print(f"Sorry there isn't enough {i}")
            return False
        return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    for i in ingredients:
        data[i] -= ingredients[i]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while not coffee_finished:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input=="off":
        print("Switching off the machine!...")
        coffee_finished=True
        exit()
    elif user_input == "report":
        print("Water available: ",data["water"],"ml")
        print("Milk available: ",data["milk"],"ml")
        print("Coffee available: ",data["coffee"],"g")
        print("Money:$",profit)
    else:
        drink=m[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(user_input,drink["ingredients"])








