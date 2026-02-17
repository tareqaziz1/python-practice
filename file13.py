#Dictionary
# Dictionary is used to store information that comes as key value pairs.
# key always should be unique. key below - name, email and phone.
customar = {
    "name": "John Smith",
    "email": "john@gmail.com",
    "phone": 123456789,
    "is_varified": True,
}

#Get the value using key-
name = customar["name"]
print(name)
print(customar["email"])

# get method can be used for the same action

my_name = customar.get("name")
print(my_name)

# Add new key value pair

customar["birth_year"] = 1999
print(customar)

# Delete a key value from dictionary

del customar["is_varified"]
print(customar)

# Delete by pop method

customar.pop("birth_year")
print(customar)

# if the key is not there, it is possible to print a default value.

print(customar.get("age", 55)) #output- 55

# Exercise convert number to string

digit_mapping_dict = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

your_number = input("What is your number? : ")

output = " "

for num in your_number:
    converted = digit_mapping_dict.get(num, "not found!") + " "
    output += converted
print(output)

