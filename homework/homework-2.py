'''
Homework: Session 2

Question 1
Explain what this program does
for number in range(100):
output = 'o' * number
print(output)

'''

for number in range(100):
    print(number)
    output = 'o' * number
    print(output)

# Concatenates and prints out 'o' the times of the index (including 0) up until 100


'''
Question 2
Your boss really likes calculating VAT on their purchases. It is their favourite hobby. They've written this code to calculate VAT and need your help to fix it. 

def calculate_vat(amount): 
amount * 1.2 

total = calculate_vat(100)
print(total) 

When your boss runs the program they get the following output: 
None 
Your boss expects the program to output the value 120. What is wrong? How do you fix it? 

'''


def calculate_vat(amount): 
    return amount * 1.2 # You need to add a return here

total = calculate_vat(100)
print(total)