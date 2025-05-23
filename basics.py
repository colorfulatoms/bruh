print("Hello, World!")
#python KEYWORDS
# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# # break      except     in         raise

# Python provides a special module for listing its keywords called keyword. 
# To find the current keyword list, you use the following code:

# import keyword

# print(keyword.kwlist)

# he Python interpreter will treat the backslash character (\) special. 
# If you don’t want it to do so, you can use raw strings by adding the letter r before the first quote.

# message = r'C:\python\bin'
# print(message)

# for multiple line string we use '''
# help_message = '''
# Usage: mysql command
#     -h hostname     
#     -d database name
#     -u username
#     -p password 
# '''

# print(help_message)

# to use the values of variables in a string -> put f(a format string) before quotation mark:
# name = 'John'
# message = f'Hi {name}'
# print(message) # Hi John

# string[start:end] start is included and end is excluded [start idx, end idx)
# omit the start -> default to zero & omit the end -> default to the lenght
# Python strings are immutable(you can't change a character using [])


# The division of two integers always returns a float
# to get the floor we use //
 
# To make the long numbers more readable, you can group digits using underscores(since python 3.6), like this:
#count = 10_000_000_000  (python ignores the underscores)

# The following are falsy values in Python:

# The number zero (0)
# An empty string ''
# False
# None
# An empty list []
# An empty tuple ()
# An empty dictionary {}

# The bad news is that Python doesn’t support constants.
# To work around this, you use all capital letters to name a variable to indicate that the variable should be treated as a constant. For example:
# These variables are constant by convention, not by rules.

# FILE_SIZE_LIMIT = 2000
# print(FILE_SIZE_LIMIT)

# Python provides three kinds of comments:
# block comment, inline comment, and documentation string.

########### COMMENTING YOUR CODE #########
# A block comment explains the code that follows it
# # increase price by 5%
# price = price * 1.05

# When you place a comment on the same line as a statement, you’ll have an inline comment.
# salary = 120000
# salary = salary * 1.02   # increase salary by 2%

# print(salary)

# A documentation string is a string literal 
# that you put as the first lines in a code block, for example, a function.
# Use docstrings for functions, modules, and classes.

# Unlike a regular comment, a documentation string can be accessed at run-time using 
# obj.__doc__ attribute where obj is the name of the function.

# Documentation strings is called docstrings.

# Technically speaking, docstrings are not the comments.
# They create anonymous variables that reference the strings.
# Also, they’re not ignored by the Python interpreter.

##############GET INPUT FROM USER AND TYPE CONVERSION ############
# To get input from users, you use the input() function. For example:

# value = input('Enter a value:')
# print(value)

# However, the input() function returns a string, not an integer

# float(str) – convert a string to a floating-point number.
# bool(val) – convert a value to a boolean value, either True or False.
# str(val) – return the string representation of a value.

# To get the type of value, you use the type(value) function.

# Python has three logical operators:

# and
# or
# not

# age = input('Enter your age: ')
# if int(age) >= 18:
#     print("You're eligible to vote.")
#     print("DO NOT VOTE!")
# else:
#     print("HA! YOU ARE SMOL!")    

# height = input("Enter your height: ")
# if int(height) <= 150:
#     print("SHORTY!")
# elif int(height) > 150 and  int(height) <= 160:
#     print("You can be a libero")
# elif int(height) == 163:
#     print("Hinata?")
# else:
#     print("YOU CAN A VOLLEYBALL PLAYER!")

# we can write:
# age = 200
# ticket = 20 if age >= 20 else 5 **************IMPORTANT********** ternary operator
# instead of:
# age = 200 
# if age >= 20:
#     ticket = 20 
# else:
#     ticket = 5
# SYNTAX: value_if_true if condition else value_if_false

############## pyhton loops ################

# for index in range(n):
#     statement
# In this syntax, the index is called a loop counter.
# And n is the number of times that the loop will execute the statement.

# The range(n) generates a sequence of n integers starting at zero.
# It increases the value by one until it reaches n.

# range(start, stop, step) -> by default it starts with zero and step is 1

# for idx in range(2, 20, 3):
#     print(idx + 1)

# sum = 0
# for num in range(101):
#     sum += num
# print(sum)    

# num = 0
# while num < 10:
#     num += 2
#     print("WOOHOO!")

# print("Ah man ...")

# Note that the command.lower() returns the command in lowercase format
# command = ''

# while command.lower() != 'quit':
#     command = input('> ')
#     print(f"Echo: {command}")

# for x in range(0, 2):
#     for y in range(0, 2):
#         if y > 1:
#             break
#         print(f"({x}, {y})")

# counter = 1
# max = 10
# if counter <= max:
#     counter += 1
# else:
#     pass
# The pass statement is a statement that does nothing.
# It’s just a placeholder for the code that you’ll write in the future.
# you use the pass statement to mark the function and class empty

######### PYTHON FUNCTIONS #########
# def greet(name):
#     """Display a greeting to the user"""
#     print(f"Oh! Hi {name}:)")

# def greet2(name):
#     return f"Hi, {name}!"

# greet("John")
# print(greet2("Mary"))

# you can default valus for parameters when you don't pass any arguments

# To use default parameters,
# you need to place parameters with the default values after other parameters. 
# Otherwise, you’ll get a syntax error.
# for example:
# def function_name(param1=value1, param2, param3):

# def greet(name = 'Kuro', message = 'Hi'):
#     return f"{message}, {name}"

# greeting = greet(message = 'Hello')
# greeting2 = greet('Mira')
# greeting3 = greet('Hello')
# greeting4 = greet()

# print(greeting)
# print(greeting2)
# print(greeting3)
# print(greeting4)

# we use an f-string to format the output number with two decimal places (f'{net_price: .2f}').

# To improve the readability, Python introduces keyword arguments.
# fn(parameter2=value2,parameter1=value1)

# def get_net_price(price, discount):
#     return price * (1-discount)

# net_price = get_net_price(
#     price=100, 
#     discount=0.1
# )

# print(f'{net_price: .2f}')

# Once you use a keyword argument, you need to use keyword arguments for the remaining parameters.

# Recursive function:
# def sum(n):
#     return n + sum(n-1) if n > 0 else 0


# result = sum(100)
# print(result)

# Python lambda expressions allow you to define anonymous functions.

# Anonymous functions are functions without names. 
# The anonymous functions are useful when you need to use them once.

# A lambda expression typically contains one or more arguments, but it can have only one expression.

# lambda parameters: expression
# equivalent to:
# def anonymous(parameters):
#     return expression

# In Python, you can pass a function to another function or return a function from another function.
# def get_full_name(first_name, last_name, formatter):
#     return formatter(first_name, last_name)

# def get_full_name(first_name, last_name, formatter):
#     return formatter(first_name, last_name)

# def first_last(first_name, last_name):
#     return f"{first_name} {last_name}"


# def last_first(first_name, last_name):
#     return f"{last_name}, {first_name}"

# full_name = get_full_name('John', 'Doe', first_last)
# print(full_name) # John Doe

# full_name = get_full_name('John', 'Doe', last_first)
# print(full_name) #  Doe, John

# Instead of defining the first_last and last_first functions, you can use lambda expressions.

# def get_full_name(first_name, last_name, formatter):
#     return formatter(first_name, last_name)


# full_name = get_full_name(
#     'John',
#     'Doe',
#     lambda first_name, last_name: f"{first_name} {last_name}"
# )
# print(full_name)

# full_name = get_full_name(
#     'John',
#     'Doe',
#     lambda first_name, last_name: f"{last_name}, {first_name}"
# )
# print(full_name)

# def times(n):
#     return lambda x: x * n

# double = times(2)

# result = double(2)
# print(result)

# result = double(3)
# print(result)

# Python provides a built-in function called help() that allows you to show the documentation of a function.

# Note that you can use the help() function to show the documentation of modules,
# classes, functions, and keywords. This tutorial focuses on function documentation only.

def add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """
    return a + b

print(add.__doc__)