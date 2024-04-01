from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_machine_on = True

while is_machine_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}): ")
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            is_payment_enough = money_machine.make_payment(drink.cost)
            if is_payment_enough:
                coffee_maker.make_coffee(drink)
