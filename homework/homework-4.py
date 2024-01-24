"""

Question 1
I have a list of things I need to buy from my supermarket of choice.

I want to know what the first thing I need to buy is. However, when I run the program it shows me a different answer to what I was expecting?
What is the mistake? How do I fix it?

"""
# shopping_list = [
# "oranges",
# "cat food",
# "sponge cake",
# "long-grain rice",
# "cheese board",
# ]
# print(shopping_list[0])
#
#
# """
#
# Question 2
# I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of different chocolates that I sell.
# I've started the program and included the chocolates and their prices. Finish the program by asking the user to input an item and then output its price.
#
# """
#
# chocolates = {
# 'white': 1.50,
# 'milk': 1.20,
# 'dark': 1.80,
# 'vegan': 2.00,
# }
#
# chocolate_choice = input('What kind of chocolate do you want? ')
#
# print(f'Your choice of {chocolate_choice} will cost {chocolates[chocolate_choice]}')


# Question 3

# Write a program that simulates a lottery. The program should have a list of seven numbers that
# represent a lottery ticket. It should then generate seven random numbers. After comparing the two
# sets of numbers, the program should output a prize based on the number of matches:
# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers
import random

def get_user_numbers():
    """Gets and validates user's lottery numbers"""
    user_numbers = []
    # for i in range(1, 8):
    #     while True:
    #         number = int(input(f'Enter lottery number {i}: '))
    #         if 1 <= number <= 49 and number not in user_numbers:
    #             user_numbers.append(number)
    #             break
    #         elif number in user_numbers:
    #             print("Duplicate number. Please enter a unique number.")
    #         else:
    #             print("Invalid number. Please enter a number between 1 and 49.")

    while len(user_numbers) < 7:
        number = random.randint(1, 49)
        user_numbers.append(number)
    print(user_numbers)
    return user_numbers


def generate_lottery_numbers(seed=None):
    if seed is not None:
        random.seed(seed)
    lottery_numbers = []
    while len(lottery_numbers) < 7:
        number = random.randint(1, 49)
        if number not in lottery_numbers:
            lottery_numbers.append(number)
    return lottery_numbers


def count_matches(user_numbers, lottery_numbers):
    return sum(num in lottery_numbers for num in user_numbers)


def determine_prize(match_count):
    if match_count == 3:
        return 20
    elif match_count == 4:
        return 40
    elif match_count == 5:
        return 100
    elif match_count == 6:
        return 10000
    elif match_count == 7:
        return 1000000
    return 0


def main():
    user_numbers = get_user_numbers()
    lottery_numbers = generate_lottery_numbers(28)
    match_count = count_matches(user_numbers, lottery_numbers)
    prize = determine_prize(match_count)

    print(f"The lottery numbers are: {lottery_numbers}")
    if prize > 0:
        print(f"Congratulations! You have won £{prize} with {match_count} matching numbers!")
    else:
        print("Sorry, no matching numbers. Better luck next time!")


if __name__ == '__main__':
    main()


