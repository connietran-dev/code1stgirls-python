# Calculate how many cans of food you need for:
# 10 cats
# Use a variable for the # of cats and # of cans, a print() function to output the result
# Extension: Change the calculation to work out the amount needed for 7 days

number_of_cats = 10
cans_per_cat = 2
number_of_days = 7

total_cans = number_of_cats * cans_per_cat * number_of_days

print(f"Meowwww! {number_of_cats} cats need {total_cans} of cans over the course of {number_of_days} days!")

# The previous alternative to fstrings was:
print('This is the alternative to fstrings back in the day: {} cats need {} cans for {} days'.format(number_of_cats, cans_per_cat, number_of_days))

# FYI for the homework:
# print(f'You need to buy {message} nails')