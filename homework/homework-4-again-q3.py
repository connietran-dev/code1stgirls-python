"""

Question 3
Write a program that simulates a lottery. The program should have a list of seven numbers that represent a lottery ticket. It should then generate seven random numbers. After comparing the two sets of numbers, the program should output a prize based on the number of matches:
● £20 for three matching numbers
● £40 for four matching numbers
● £100 for five matching numbers
● £10000 for six matching numbers
● £1000000 for seven matching numbers

"""

import random

"""
Let user choose lottery numbers
"""
# users_numbers = []
#
# for i in range(1, 8):
#     new_number = input('Pick a random number from 1-49, 7 times: ')
#     users_numbers.append(new_number)
#     print(users_numbers)

"""
Used for testing
"""
users_numbers = []

while len(users_numbers) < 7:
    number = random.randint(1, 49)
    users_numbers.append(number)
print(users_numbers)


"""
Generate lottery numbers
"""
lottery_numbers = []

while len(lottery_numbers) < 7:
    number = random.randint(1, 49)
    lottery_numbers.append(number)
print(lottery_numbers)

"""
Used for testing
"""
# users_numbers = [1,2,3,4,5,12,7]
# lottery_numbers = [1,12,31,4,51,6,7]


"""
Compare numbers and count matches
"""
number_matches = 0

for index in range(7):
    if users_numbers[index] == lottery_numbers[index]:
        number_matches += 1
        print('yayy')
    else:
        print('nayyy')


"""
Print prize based on number of matches
"""
print(number_matches)

if number_matches == 3:
    print('You get £20!')
elif number_matches == 4:
    print('You get £40!')
elif number_matches == 5:
    print('You get £100!')
elif number_matches == 6:
    print('You get £10000!')
elif number_matches == 7:
    print('You get £1000000!!')
else:
    print('Sorry no numbers matched!')