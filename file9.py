# for loop

for letter in "python":
    print(letter)


# List is a list of items. It can be numbers or strings. Syntax - []

for item in ["Tareq", "John", "Tom"]:
    print(item)

for number in [1,2,3,4,5,6]:
    print(number)

#to print a range of 1 to 9 (range has to be until 10) -

for x in range(10):
    print(x)

for z in range(20, 31):
    print(z) # it will print 20 to 30

# Range function can add a step. For example if 2 is given as a third parameter it will be forwaded with 2 steps.

for i in range(20,31,2):
    print(i) # it will print 20,22,24.26,28,30

# A list of prices given, add the total .

prices = [10.5, 14.20, 15.20, 30.10]
total_price = 0

for item_price in prices:
    total_price += item_price

print(f"Total price: {total_price}")


