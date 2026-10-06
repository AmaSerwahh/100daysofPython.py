MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money = 0

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_money}")

def resources_sufficient(drink):
    is_enough = True
    for item in MENU[drink]["ingredients"]:
        if resources[item] <= MENU[drink]["ingredients"][item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False
    return is_enough

def process_coins():
    QUARTERS = 0.25
    DIMES = 0.10
    NICKLES = 0.05
    PENNIES = 0.25

    quarters = int(input("How many quarters?: ")) * QUARTERS
    dimes = int(input("How many dimes?: ")) * DIMES
    nickles = int(input("How many nickles?: ")) * NICKLES
    pennies = int(input("How many pennies?: ")) * PENNIES

    total_coins = quarters + dimes + nickles + pennies
    return total_coins

def transaction_successful(money):
    global total_money
    if money >= MENU[choice]["cost"]:
        total_money += MENU[choice]["cost"]
        change = float(round(money - MENU[choice]["cost"], 2))
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee():
    for item in MENU[choice]["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]

    print(f"Here is your {choice}. Enjoy!")

order = True
while order:
    choice = input("What would you like?(espresso/latte/cappuccino:)\n").lower()
    if choice == "report":
        report()
    elif choice == "off":
        order = False
    else:
        if resources_sufficient(choice):
            if transaction_successful(process_coins()):
                make_coffee()


