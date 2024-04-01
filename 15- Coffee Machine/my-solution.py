MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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


def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney: ${money}")


def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    penny = int(input("how many penny?: "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + penny * 0.01


def check_resource(coffee_type):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    if water < MENU[coffee_type]["ingredients"]["water"]:
        print("Sorry there is not enough water")
        return False
    if coffee < MENU[coffee_type]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    if (
        MENU[coffee_type]["ingredients"]["milk"]
        and milk < MENU[coffee_type]["ingredients"]["milk"]
    ):
        print("Sorry there is not enough milk")
        return False
    return True


def make_transaction(money, coffee_type):
    money += MENU[coffee_type]["cost"]
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    if MENU[coffee_type]["ingredients"]["milk"]:
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]


is_machine_on = True
money = 0

while is_machine_on:
    action = input("What would you like? (espresso/latte/cappuccino): ")
    if action == "report":
        print_report()
    elif action == "off":
        is_machine_on = False
    else:
        is_enough_resource = check_resource(action)
        if is_enough_resource:
            inserted_money = process_coins()
            if inserted_money < MENU[action]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = inserted_money - MENU[action]["cost"]
                print(f"Here is ${change} in change.")
                print(f"Here is your {action} ☕️.Enjoy!")
                make_transaction(money, action)
