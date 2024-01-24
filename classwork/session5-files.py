# **Exercise 5.1:** Create a to-do list program that writes user input to a file
#
# The program should:
# - Ask the user to input a new to-do item
# - Add the new to do item to the existing to-do items
# - Save the updated to-do items
# - Read the contents of the existing to-do items
#
# You will need to manually create a new file called todo.txt in the same folder as your program before you start

new_item = input(f'Add an item to your to-do list: ')

with open('todo.txt', 'a') as todo_list:
    todo_list.write(new_item + '\n')

with open('todo.txt', 'r') as todo_list:
    contents = todo_list.read()

print(contents)

