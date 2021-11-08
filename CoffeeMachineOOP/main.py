from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    drinks = Menu()
    machine = CoffeeMaker()
    money = MoneyMachine()

    machine_on = True

    while machine_on:
        # Prompt User for Selection
        selection = input("What would you like? " + "(" + drinks.get_items() + "): ").lower()

        # Perform Actions
        if selection == "off":
            machine_on = False
        elif selection == "report":
            machine.report()
            money.report()
        elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
            # Create the drink order
            new_order = drinks.find_drink(selection)
            # Check resources
            if machine.is_resource_sufficient(new_order):  # If there are sufficient resources, proceed with the order
                # Process the coins
                if money.make_payment(new_order.cost):  # If payment is successful, proceed with the order
                    # Make the order
                    machine.make_coffee(new_order)
        else:
            print("Invalid selection")


coffee_machine()
