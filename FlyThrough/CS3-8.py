import requests

my_request = requests.get('http://go.codeschool.com/spamvanmenu')
menu_list = my_request.json()
# print(menu_list)

print("Today's Menu:")
for item in menu_list:
    print(item['name'], ': ', item['desc'], ', $', item['price'], sep='')

