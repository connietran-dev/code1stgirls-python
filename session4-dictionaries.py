"""
Exercise 4.5: Print the values of name, post_code and street_number from the dictionary

Extension: Print the values of longitude and latitude from the inner dictionary

"""

place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
        }
}

print(place['name'])
print(place['post_code'])
print(place['street_number'])
print(place['location']['longitude'])
print(place['location']['latitude'])


"""
Exercise 4.6: Using a for loop, output the values name, colour and price of each dictionary in the list

"""

fruits = [

    {'name': 'apple', 'colour': 'red', 'price': 0.12},

    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},

    {'name': 'pear', 'colour': 'green', 'price': 0.19},

]

for fruit in fruits:
    print(fruit['name'])
    print(fruit['colour'])
    print(fruit['price'])
    print() # Prints an empty line for better readability

