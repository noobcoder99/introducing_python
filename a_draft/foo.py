while True:
    value = input("Interger, please [q to quit]:")
    if value == 'q': #quit
        break
    number = int(value)
    if number % 2 == 0: #an even number
        continue
    print(number, "squared is", number*number)
