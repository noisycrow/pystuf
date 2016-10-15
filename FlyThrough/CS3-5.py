def print_menu(menu):
    for name, price in menu.items():
        print(name, ': $', format(price, '.2f'), sep='')

def get_order(menu):
    orders = []
    while (True):
        order = input("What would you like to order? (Q for Quit)")
        if order == 'Cheeky Spam':
            print("Sorry, we're out of that!")
            continue
        if order.upper() == 'Q':
            break
        found = menu.get(order)
        if found:
            orders.append(order)
        else:
            print("Menu item doesn't exist")
    return orders

def main():
    menu = {"Knackered Spam": 0.50, "Pip pip Spam": 1.50, "Cheeky Spam": 2.50, "Smashing Spam": 3.50}
    print_menu(menu)
    orders = get_order(menu)
    total = bill_total(orders, menu)
    print("You ordered: ", orders, "\nYour Total is: $", format(total, '.2f'), sep='')

def bill_total(orders, menu):
    total = 0
    for order in orders:
        total += menu[order]
    return total

main()

