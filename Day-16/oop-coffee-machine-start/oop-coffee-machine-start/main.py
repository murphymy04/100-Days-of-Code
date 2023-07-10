from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

choices = menu.get_items()
loop = True
while loop:
    drink = input(f"What would you like? {choices}: ")
    if drink == 'off':
        quit()
    elif drink == 'report':
        machine.report()
    else:
        choice = menu.find_drink(drink)
        if machine.is_resource_sufficient(choice) and money.make_payment(choice.cost):
            machine.make_coffee(choice)