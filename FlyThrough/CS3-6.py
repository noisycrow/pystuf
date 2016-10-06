#sales_log = open('spam_orders.txt', 'w')
#sales_log.write('The Spam Van\n')
#sales_log.write('Sales Log\n')
#sales_log.close()

def write_sales_log(order):
    file = open('sales.txt', 'a')
    total = 0
    for item, price in order.items():
        file.write(item + ' ' + format(price, '.2f') + '\n')
        total += price
    file.write('Total =  ' + format(total, '.2f') + '\n\n')
    file.close()

def main():
    order = {'Cheeky Spam': 1.0, 'Yonks Spam':4.0}
    write_sales_log(order)
    order = {'Smashing Spam': 2.0, 'Cheerio Spam':3.0}
    write_sales_log(order)
main()