import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# to print report
coffee=CoffeeMaker()
money=MoneyMachine()
menu=Menu()

is_on=True

while is_on:
    options=menu.get_items()
    choices=input(f"What would you like?({options}):")
    if choices=="off":
        print("Switching off the machine...")
        is_on=False
    elif choices=="report":
        coffee.report()
        money.report()
    else:
        drink=menu.find_drink(choices)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)


