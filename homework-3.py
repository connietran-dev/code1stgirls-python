"""
Homework: Session 3

Question 1
Create a program that tells you whether or not you need an umbrella when you leave the house.
The program should:
1. Ask you if it is raining using input()
2. If the input is 'y', it should output 'Take an umbrella'
3. If the input is 'n', it should output 'You don't need an umbrella'

"""

is_raining = input('Is it raining: y/n? ')

if is_raining == 'y':
    print('Take an umbrella')
else:
    print('You don\'t need an umbrella')


"""
Question 2
I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've written a program to check that I can afford the cost, but something doesn't seem right. 
Have a look at my program and work out what I've done wrong 

my_money = input('How much money do you have? ') 
boat cost = 20 + 5
if my_money < boat_cost: 
print('You can afford the boat hire') 
else: 
print('You cannot afford the board hire') 

"""

# I added float() to ensure my_money is a number rather than string
my_money = float(input('How much money do you have? '))

boat_cost = 20 + 5

# I also made it greater than, because logically you'd want more money than the boat_cost
if my_money > boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')


"""

Question 3 
Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to quickly categorise books by the century and decade that they were written. 

Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Nineteenth Century, Seventies") 

"""

import datetime

from datetime import datetime
from datetime import date

book_question = datetime.fromtimestamp(int(input('What year was your book written?: ')))

print(book_question)

print(book_question.strftime("%Y"))
# book_date = datetime.date.book_question.year

# book_question = datetime.fromtimestamp((int(input('What year was your book written?: '))))
#
# # book_year = (book_question)
#
# print(book_question.year)


# current_date = datetime.datetime.now()
# print(current_date)

# From ChatGPT:
def categorize_year(year):
    # Determine the century
    century = (year - 1) // 100 + 1

    # Determine the decade
    decade = ((year - 1) % 100 // 10) * 10

    # Define century and decade names
    century_names = {
        1: "First",
        2: "Second",
        3: "Third",
        4: "Fourth",
        # Add more centuries as needed
    }

    decade_names = {
        0: "Noughties",
        10: "Tens",
        20: "Twenties",
        30: "Thirties",
        40: "Forties",
        50: "Fifties",
        60: "Sixties",
        70: "Seventies",
        80: "Eighties",
        90: "Nineties",
    }

    # Output the result
    century_name = century_names.get(century, "Unknown Century")
    decade_name = decade_names.get(decade, "Unknown Decade")

    return f"{century_name} Century, {decade_name}"

# Example usage:
year_input = int(input("Enter a year (e.g., 1872): "))
result = categorize_year(year_input)
print(result)
