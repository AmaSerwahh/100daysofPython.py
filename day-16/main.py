from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
#menuitem = MenuItem()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

order = True
while order:
    print(menu.get_items())
    choice = input("what would you like to order?: ")
    if choice == "report":
        coffeemaker.report()
        moneymachine.report()
    elif choice == "off":
        order = False
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):
            money = drink.cost
            if moneymachine.make_payment(money):
                coffeemaker.make_coffee(drink)


