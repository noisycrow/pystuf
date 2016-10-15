prices = [2.50, 3.50, 4.50]
total = 0
for price in prices:
    print('Price is',price)
    total = total + price
    print('Total is', total)

average = total / len(prices)
print('Average is', average)

import random
r1 = random.random()
print(r1)
r2 = random.choice([1,2,3,4,5])
print(r2)
r3 = random.randint(1,1000)
print(r3)
print()

for i in range(10):
    ticket = random.randint(1,1000)
    print(ticket)

print()
