from data import MENU as menu
from data import resources

money = 0
def prompt():
    '''Asks the user for the type of coffee they want.

    Args: None
    '''
    p = input("What would you like? (espresso-$1.50/latte-$2.50/cappuccino-$3.00): ").lower()
    return p
def quarters():
    '''Asks for number of quarters and converts the value to a dollar amount

    Args: None
    '''
    q = int(input("How many quarters?: "))
    q *= .25
    return q
def dimes():
    d = int(input("How many dimes?: "))
    d *= .1
    return d
def nickels():
    n = int(input("How many nickels?: "))
    n *= .05
    return n
def pennies():
    p = int(input("How many pennies?: "))
    p *= .01
    return p
def change(cost, payment):
    change = format(payment - cost, ".2f")
    return change
def money_left(payment, change_returned, money):
    money_l = money + (float(payment) - float(change_returned))
    return money_l
def report():
    print(f'Water: {resources["water"]}ml \n'
          f'Milk: {resources["milk"]}ml \n'
          f'Coffee: {resources["coffee"]}g \n'
          f'Money: ${format(money, ".2f")}')

loop = True
while loop:
    drink = str(prompt())
    if drink == "report":
        report()
    elif drink == "off":
        quit()
    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        payment = quarters() + dimes() + nickels() + pennies()
        if payment >= menu[drink]["cost"] and menu[drink]["ingredients"]["water"] <= resources["water"] and menu[drink]["ingredients"]["milk"] <= resources["milk"] and menu[drink]["ingredients"]["coffee"] <= resources["coffee"]:
            if payment == menu[drink]["cost"]:
                change_returned = change(menu[drink]['cost'], payment)
                money = money_left(payment, change_returned, money)
                resources["water"] -= menu[drink]["ingredients"]["water"]
                resources["milk"] -= menu[drink]["ingredients"]["milk"]
                resources["coffee"] -= menu[drink]["ingredients"]["coffee"]
                print(f"Here is your {drink}. Enjoy!")
            else:
                print(f"Here is ${change(menu[drink]['cost'], payment)} in change.")
                change_returned = change(menu[drink]['cost'], payment)
                money = money_left(payment, change_returned, money)
                resources["water"] -= menu[drink]["ingredients"]["water"]
                resources["milk"] -= menu[drink]["ingredients"]["milk"]
                resources["coffee"] -= menu[drink]["ingredients"]["coffee"]
                print(f"Here is your {drink}. Enjoy!")
        elif payment < menu[drink]["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
        elif menu[drink]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there's not enough water.")
        elif menu[drink]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there's not enough milk.")
        elif  menu[drink]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there's not enough coffee.")
    else:
        print("You have entered an invalid response, please try again")