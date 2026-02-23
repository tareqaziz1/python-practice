# Functions

# Make a function that prints "Hello World"

def hello_world():
    print("Hello World")

hello_world()

# Make function with parameters

def greeting(name):
    print(f"Good morning {name}")

greeting("John")
greeting("Sarah")


def custom_greeting(first_name, last_name, message):
    print(f"Hey, {first_name} {last_name}, {message}")

custom_greeting("Tareq", "Aziz", "Welconme aboard!")

# Keyword argument ( position does not matter if it is used)

custom_greeting(last_name="Aziz", message="Good evening", first_name="Tareq")

# fucntion with return statement

def square (number):
    return number * number

result = square(4)
print(result)
#or
print(square(5))    # without return it will return "None"







