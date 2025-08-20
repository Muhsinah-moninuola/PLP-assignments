#creating a calculate discount function
def calculate_discount(price, discount_percent):
    #conditional block to check if discount is applicable
    if discount_percent >= 20:
        discount = (discount_percent/100)*price #calculate discpunt
        new_price = price - discount
        print("You're eligible for a discount")
        return f"The new price of '{item}' after discount is {new_price}" 
    else:
        print(f'Discount not appliable on "{item}"')
        return f'The price of {item} is {price}'
#user input
item = input('What did you buy? ')
item_price = float(input(f'How much is the "{item}"? '))
discount_percent = float(input(f'What is the discount percent on "{item}": '))

print(calculate_discount(item_price, discount_percent))