#This is a basic calculator program
print('Hi, this is a simple calculator') #simple greeting
print("1: Addition \n2: Subtraction \n3: Multiplication \n4: Division")#providing user with choices
operation = int(input('Enter an option: '))#collects their choice as an integer

#user inputs two numbers
a = int(input('\nEnter first number: '))
b = int(input('Enter second number: '))

#conditional statements based on user's choice
if operation == 1:
    c = a+b
    print(f'{a}+{b} = {c}' )
elif operation == 2:
    c = a-b
    print(f'{a}-{b} = {c}' )
elif operation == 3:
    c = a*b
    print(f'{a}x{b} = {c}' )
elif operation == 4:
    c = a/b
    print(f'{a}/{b} = {c}' )
else: #when user enters a wrong option
    print('Kindly check the options and pick from 1-4')
