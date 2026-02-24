# Exeptions (try & except)

#try is used to run code that might fail or cause an error.
#If something goes wrong, except catches the error so the program doesn’t crash.

try:
    age = int(input("Age: "))
    income = 1000
    risk = income / age
    print(f"Age is {age} years")
    print(f"Risk is {risk}")
except ValueError:
    print("value should be a number!")
except ZeroDivisionError:
    print("Age cannot be 0!")
