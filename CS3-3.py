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

print(menu_prices)