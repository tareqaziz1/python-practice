#Built-in methods on string

subject = "Introduction to Python"
length_of_the_string = len(subject)
print(length_of_the_string)

#Converting to upper or lower case

upper = subject.upper()
lower = subject.lower()

print(f'upper = {upper}. lower = {lower}')

#Find a character
finding_p = subject.find(('P'))
print(finding_p) #sequence

#Replacing words

replacement = subject.replace("Introduction", "Road")
print(replacement)

#To make first letter upper case
string1 = "python is a programming language"
first_letter_upper = string1.title() #Python Is A Programming Language
print(first_letter_upper)

# "in" operator (boolean outcome)

print("Python" in subject) #True
print("Java" in subject) #False

