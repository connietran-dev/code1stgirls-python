# for loops!
# Variables in loops are locally. So they're not available globally

for number in range(5):
    print(number)

for character in 'Banana':
    print(character)

for name in ['Connie', 'Joanna', 'Tran']:
    print(name)

for number in range(5):
    print(f'This is loop {number + 1}') # This is a local variable

total = 4 # This is global

for number in range(3):
    oranges = 5
    print(f'The total is {total}')
    print('Adding one to the loop')
    total += 1
    print(oranges)

print(f'Oranges!! {oranges}')
print(f'Oranges: {oranges +2}')
print(f'The final total is {total}')
print(f'Is the number available? {number}') # number is the index

