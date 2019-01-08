numbers = [2,2,3]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
        position =+ 1
    else: #break not called
        print("No")
