#this is a program that accepts user inputs and adds the integers
myList = []
#asks the user for the number of integers they want to input
tries = int(input('How many numbers do you want to add? '))
for x in range (tries):
    #to loop through the number of tries. 
        num = int(input('Enter a number: '))
        myList.append(num)
    
#compute the sum
total = sum(myList)

#display the result
print(f'These are the numbers you entered; {myList}')
print(f'The sum of the numbers you entered is {total}')





