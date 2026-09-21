# Function 1 - double: Takes a number and returns it multiplied by 2
def double(number):
    return number * 2

# Function 2 - is_pass: Returns True if score is 50 or more, False otherwise
def is_pass(score):
    return score >= 50

# Function 3 - greet: Returns a customized greeting with a default of "Hello"
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"# Test calls
print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))