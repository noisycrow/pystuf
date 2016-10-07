slang = ['Knackered', 'Pip pip', 'Squidgy', 'Smashing']

menu =[]

for word in slang:
    menu.append(word + ' Spam')

print(menu)

menu_prices = {}
price = .50
for item in menu:
    menu_prices[item] = price
    price = price + 1

for name, price in menu_prices.items():
    print(name, ': $', format(price, '.2f'), sep='')

x = 1
while x != 3:
    print('x is', x)
    x = x + 1

orders = []


while (True):
    order = input("What would you like to order? (Q for Quit)")
    if order == 'Cheeky Spam':
        print("Sorry, we're out of that!")
        continue
    if order.upper() == 'Q':
        break
    found = menu_prices.get(order)
    if found:
        orders.append(order)
    else:
        print("Menu item doesn't exist")

print("You ordered:", orders)
