from kitchen import MENU, resources


def extract_information(coffe_type):
    coffee_info = [MENU[coffe_type]["ingredients"]["water"], MENU[coffe_type]["ingredients"]["milk"],
                   MENU[coffe_type]["ingredients"]["coffee"]]
    return coffee_info


def check_resources(water, milk, coffee):
    if resources["water"] >= water:
        if resources["milk"] >= milk:
            if resources["coffee"] >= coffee:
                return 0
            else:
                print("Not enough Coffee Powder available, Order Can not be processed")
                return 1
        else:
            print("Not enough milk available, Order can not be processed")
            return 1
    else:
        print("Not enough water available, Order can not be processed")
        return 1


def print_report(money_earned):
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money_earned}')


def process_coins():
    quarters = int(input("Insert Quarters($0.25): "))
    dimes = int(input("Insert dimes($0.10): "))
    nickles = int(input("Insert nickles($0.05): "))
    pennies = int(input("Insert pennies($0.01): "))
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total_money


def check_money(money_inserted, coffee_type):
    if money_inserted == MENU[coffee_type]["cost"]:
        print(f"Here is your {coffee_type}, Enjoy!")
        return True
    elif money_inserted > MENU[coffee_type]["cost"]:
        print(f"Here is your {coffee_type}, Enjoy!")
        change = money_inserted - MENU[coffee_type]["cost"]
        change = round(change, 2)
        print(f"Here is your change: ${change}")
        return True
    else:
        print("Money inserted is not enough for the order, Order Cancelled.")
        print(f"You have been refunded ${money_inserted}")
        return False


def making_coffee(water, milk, coffee):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee


machine_running = True
money = 0
while machine_running:
    coffee_choice = input("Type in Your Drink Name:\n1.Espresso\n2.Latte\n3.cappuccino\n").lower()
    if coffee_choice == 'off':
        machine_running = False
    elif coffee_choice == 'report':
        print_report(money)
    elif coffee_choice != "espresso" and coffee_choice != "latte" and coffee_choice != "cappuccino":
        print("Invalid Input")
    else:
        coffee_information = extract_information(coffee_choice)
        available = check_resources(coffee_information[0], coffee_information[1], coffee_information[2])
        if available == 0:
            money_entered = process_coins()
            if check_money(money_entered, coffee_choice):
                money += MENU[coffee_choice]["cost"]
                making_coffee(coffee_information[0], coffee_information[1], coffee_information[2])
