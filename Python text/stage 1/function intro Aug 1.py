# A function can run without inputs when it does not need any information.
def say_hello():
    print("Hello!")

# Call the function by writing its name followed by parentheses.
say_hello()
say_hello()
say_hello()

# A parameter is a variable named in the function definition.
# Use parameters when a function needs information that can change between calls (when I call the function).
def greet(name):
    print("Hello", name)

# An argument is the actual value passed to a function when it is called.
# Here, "Bob" is the argument received by the name parameter.
greet("Bob")

# a and b are parameters; the function uses them as its input values.
def add(a, b):
    return a + b

# 5 and 3 are arguments passed to a and b, respectively.
answer = add(5, 3)

print(answer)


# d and c are parameters that receive the two values to multiply.
def multiplication(d,c):
    return d * c

# 7 and 8 are arguments passed to d and c, respectively.
answer2 = multiplication(7, 8)

print(answer2)