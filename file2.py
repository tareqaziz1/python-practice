#Strings

course = 'Python for "beginners"'
print(course)

#To get the first letter of a string -

language = "PythoN"

first_letter = language[0]
print(first_letter)

#To get the first letter of a string -
last_letter = language[-1]
print(last_letter)

# To get a number of characters from string (string[start:end]

first_3_letters = language[0:3]
print(first_3_letters)

#To remove a letter -

remove_first_letter = language[1:]
print(remove_first_letter)

ytho = language[1:-1]
print(ytho)

#String multiple lines

longString = '''Hello! 
This is Tareq.
I am learning python.
This is a long string'''
print(longString)

#Dynamic string (formated string)

firstName = "Tareq"
lastName = "Aziz"

message = f'{firstName} is the first name and {lastName} is the last name'
print(message)

fullName = f'[{firstName}] [{lastName}]'
print(fullName)