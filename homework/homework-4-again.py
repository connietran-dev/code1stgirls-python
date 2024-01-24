"""

Question 1
I have a list of things I need to buy from my supermarket of choice.
shopping_list = [
"oranges",
"cat food",
"sponge cake",
"long-grain rice",
"cheese board",
]
print(shopping_list[1])
I want to know what the first thing I need to buy is. However, when I run the program it shows me a different answer to what I was expecting?
What is the mistake? How do I fix it?

"""

shopping_list = [
    "oranges",
    "cat food",
    "sponge cake",
    "long-grain rice",
    "cheese board",
]

print(shopping_list[0])


"""
Question 2 
I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of different chocolates that I sell. 
I've started the program and included the chocolates and their prices. Finish the program by asking the user to input an item and then output its price. 

"""

chocolates = { 
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

chocolate_type = input('Which chocolate would you like to buy?: ')

print(chocolates[chocolate_type])
