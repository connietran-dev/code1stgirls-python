age = input('What is your age?: ')
print(f'Hello! I am {age} years old.')

# Exercise 1

hometown = input('What is your hometown?: ')
print(f'I am originally from {hometown}.')


fav_food = input('What is your favorite food?: ')
print(f'I looooove eating {fav_food}.')

# input() is always expecting strings unless you state otherwise, eg, with "int()"
purchased_apples = int(input('How many apples would you like?: '))
print(type(purchased_apples))
total_apples = purchased_apples * 5
print(total_apples)


# Exercise 2
# Write a program to calculate how many pizzas you need for you and your friends

number_of_friends = int(input('How many friends are at your party? (Not including yourself): '))
slices_per_person = int(input('How many slices of pizza can each person eat?: '))

# Assumptions
slices_per_pizza = 8

number_of_partygoers = number_of_friends + 1
number_of_pizzas = (number_of_partygoers * slices_per_person) / slices_per_pizza

print(f'You\'ll need to order {number_of_pizzas} pizzas for {number_of_partygoers} people.')