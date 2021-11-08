from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    machine_on = True

    while machine_on:
        # Prompt User for Selection
        selection = input(f"What would you like? {menu.get_items()}: ").lower()

        # Perform Actions
        if selection == "off":
            machine_on = False
        elif selection == "report":
            coffee_maker.report()
            money_machine.report()
        elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
            # Create the drink order
            new_order = menu.find_drink(selection)
            # Check resources
            if coffee_maker.is_resource_sufficient(new_order):  # If resources are sufficient, proceed with order
                # Process the coins
                if money_machine.make_payment(new_order.cost):  # If payment is successful, proceed with order
                    # Make the order
                    coffee_maker.make_coffee(new_order)
        else:
            print("Invalid selection")


coffee_machine()
