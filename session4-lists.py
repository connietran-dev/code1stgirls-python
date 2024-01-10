"""
Exercise 4.1: When I'm travelling in the winter I often forget to pack warm clothes. Let's write a program to help me to remember the right clothes.

The program should check if the first item in the clothes list is "shorts". If it is it should change the value to "warm coat".

"""

clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]

print(clothes)

if clothes[0] == "shorts":
    clothes[0] = "warm coat"

print(clothes)

costs = [1.2, 58, 2339.3, 0.5]

# FYI when you use reversed() it needs list() since the datatype is not a list, so you need to turn it into a list
print(list(reversed(costs)))

"""
Exercise 4.2: Make a list of game scores. Using list functions write code to output information of the scores in the following format:

Number of scores: 10

Highest score: 200

Lowest score: 3

Extension: Output all of the scores in descending order
"""

scores = [1.2, 58, 2339.3, 0.5]

print(len(scores))
print(max(scores))
print(min(scores))
print(list(reversed(sorted((scores)))))
# or
print(sorted(scores, reverse=True))


"""
Exercise 4.3: Whenever I'm shopping and I buy some bread I always forget to buy butter. Create a list and if 'bread' is in the list, add 'butter' to the shopping list.

Try running the program with and without bread in the list to check that your program works.

Remember the in operator checks if an item is in a list and the .append() method adds an item to a list.
"""

grocery_list = [
    "bread",
    "white pepper",
    "garlic",
    "hand soap"
]

print(grocery_list)

if "bread" in grocery_list:
    grocery_list.append("butter")

print(grocery_list)


"""

Exercise 4.4: I want to work out how much money I've spent on lunch this week. I've created a list of what I spent each day.

Write a program that uses a for loop to calculate the total cost

"""

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]

total_cost = 0

for item in costs:
    total_cost += item

print(total_cost)