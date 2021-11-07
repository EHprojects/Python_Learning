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
    }
}


def print_report(money, avail_resources):
    """Takes the current cash on hand and available resources and prints a report."""
    print(f"Water: {avail_resources['water']}ml")
    print(f"Milk: {avail_resources['milk']}ml")
    print(f"Coffee: {avail_resources['coffee']}g")
    print(f"Money: ${money}")


def coin_insert(item_selection):
    """Takes the chosen item and prompts for coins to be inserted. The cost of the selected item is subtracted and
    the appropriate amount of change is refunded. Returns TRUE if enough money is inserted, otherwise FALSE."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    coin_in = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    selection_cost = MENU[item_selection]["cost"]

    if coin_in >= selection_cost:
        change_given = round(coin_in - selection_cost, 2)
        print(f"Here is ${change_given} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def check_resources(item_selection, avail_resources):
    """Takes the chosen item and available resources, then checks that enough resources are available to make it.
    Returns TRUE if yes, otherwise FALSE. """
    suffcnt_res = True

    for key in MENU[item_selection]["ingredients"]:
        if avail_resources[key] < MENU[item_selection]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            suffcnt_res = False

    return suffcnt_res


def update_resources(item_selection, avail_resources):
    """Takes the item selection and current resources and returns the updated resources after the selected item
    has been made."""
    for key in MENU[item_selection]["ingredients"]:
        avail_resources[key] = avail_resources[key] - MENU[item_selection]["ingredients"][key]

    return avail_resources


def coffee_machine():
    machine_on = True

    # Starting Resources
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    cash_on_hand = 0

    while machine_on:
        # Prompt User for Selection
        selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if selection == "report":
            print_report(cash_on_hand, resources)
        elif selection == "off":
            machine_on = False
        elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
            if check_resources(selection, resources):
                if coin_insert(selection):
                    print(f"Here is your {selection} ☕️. Enjoy!")
                    cash_on_hand += MENU[selection]["cost"]
                    resources = update_resources(selection, resources)
        else:
            print("Invalid selection.")


coffee_machine()
