"""
Exercise 3.1: You have a budget of £10 and want to write a program to decide which burger restaurant to go to.

Input the price of a burger using input()

Check whether the price is less than or equal (<=) 10.00

Print the result in the format below
gi
Burger is within budget: True

Hint: remember to convert the input from a string to a decimal with float()
"""

burger = input('What\'s the price of the burger?: ')

within_budget = float(burger) <= 10.00

print(f'Burger is within budget: {within_budget}')


"""
**Exercise 3.2:** Add code to your burger program to input whether the restaurant has a vegetarian option

The output should say whether the cost is within budget **AND** has a vegetarian option

Restaurant meets criteria: True
"""

veggie_option = input('Does the restaurant have a veggie option? y/n ')

has_veggie = veggie_option == 'y'

restaurant_meets = within_budget and has_veggie

print(f'Restaurant meets criteria: {restaurant_meets}')


"""
Exercise 3.3: Rewrite the output of your burger program to use if statements

If it is a good choice it should be:

This restaurant is a great choice!

If it is not a good choice it should be:

Probably not a good idea
"""


if restaurant_meets:
    print('This restaurant is a great choice!')

if not restaurant_meets:
    print('Probably not a good idea')


"""
Exercise 3.4: Now that you've finished your burger, you want to pay for your food. Let's write a program to calculate your meal and apply a discount if applicable.

If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%. The program should print "Discount applied" or "No discount" depending on whether the discount criteria was met.

"""

meal_price = float(input('How much did the meal cost? '))

discount_choice = input('Do you have a discount? y/n ')

if meal_price > 20 and discount_choice == 'y':
    print('Discount applied')
    meal_price *= 0.9
    print(meal_price)
else:
    print('No discount')

print(f'Meal price is: {meal_price}')