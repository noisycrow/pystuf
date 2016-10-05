def average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    avg = total/len(numbers)
    return avg

numbers = [1,2,3,4]
my_average = average(numbers)
print(my_average)

daily_sales = [10,14,8]
result = average(daily_sales)
print("Daily Sales Average:",result)

prices = [2.50, 3, 4.50, 5]
result = average(prices)
print(result)
