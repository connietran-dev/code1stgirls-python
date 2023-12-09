# HOMEWORK: SESSION 1

'''
Question 1
I am building some very high quality chairs and need exactly four nails for each chair. I've written a
program to calculate how many nails I need to buy to build these chairs.
chairs = '15'
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))
When I run the program it tells me that I need to buy 15151515 nails. This seems like a lot of nails. Is
my program calculating the total number of nails correctly? What is the problem? How do I fix it?
'''

chairs = 15
nails = 4
total_nails = chairs * nails

# Rewriting the following with an f-string
# message = 'I need to buy {} nails'.format(total_nails)
# print('You need to buy {} nails'.format(message))

message = f'I need to buy {nails} nails'

print(f'You need to buy {total_nails} nails for {chairs} chairs.')


'''
Question 2
I'm trying to run this program, but I get an error. What is the error telling me is wrong? How do I fix
the program?
my_name = Penelope
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)
'''

my_name = 'Penelope'
my_age = 29

# Rewriting into fstring
# message = 'My name is {} and I am {} years old'.format(my_name, my_age)

message = f'My name is {my_name} and I am {my_age} years old.'

print(message)


'''
Question 3

I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can
make. Write a program to calculate this.

Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be
able to easily change these values if I want. The output should say something like "You can make 9
omelettes with 6 boxes of eggs".
'''

eggs_per_box = 6
eggs_per_omeltte = 4

boxes_of_eggs = 6

total_omelettes = (eggs_per_box * boxes_of_eggs) / eggs_per_omeltte

print(f'You can make {total_omelettes} omelettes with {boxes_of_eggs} boxes of eggs.')