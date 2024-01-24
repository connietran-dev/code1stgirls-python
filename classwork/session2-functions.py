# functions

def hello():
    print(f'Hello everyone!')

hello()

def hello_with_args(name):
    print(f'Hello, {name}')

hello_with_args('Connie')

def hello_with_args(name, job):
    print(f'Hello, {name}. You\'re a great {job}!')

hello_with_args('Connie', 'Software Programmer')

# Keyword arguments
hello_with_args(job="Project Manager", name="Connie Joanna!")


def hardcoding(name, job='Software Engineer'):
    print(f'{name} is a {job}')

hardcoding('Connay')
hardcoding('Jo, the instructor')
# You can overwrite arguments
hardcoding('Jo, the instructor', job='Goldsmith')


# Returning values from a function
def sum(x, y):
    return x + y

result = sum(245, 694)

print(result)

print(sum(6729,19))

