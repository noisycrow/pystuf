def create_dollar_menu():
    dollar_menu = open('dollar_menu.txt', 'a')
    dollar_menu.write('Cheeky Spam\n')
    dollar_menu.write('Smashing Spam\n')
    dollar_menu.write('Pip pip Spam\n')
    dollar_menu.close()

def read_dollar_menu():
    dollar_spam = open('dollar_menu.txt', 'r')
    dollar_menu = []
    for line in dollar_spam:
        line = line.strip()
        dollar_menu.append(line)
    print(dollar_menu)
    dollar_spam.close()

def main():
    create_dollar_menu()
    read_dollar_menu()

main()