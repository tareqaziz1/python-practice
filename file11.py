ages = [23,25,21,26,28,32,28,30]

# append method

ages.append(40)
print(ages) #output - [23, 25, 21, 26, 28, 32, 30, 40]

#insert method (index, new item)

ages.insert(0, 50)
print(ages) #output - [50, 23, 25, 21, 26, 28, 32, 30, 40] 50 added in 0th position.

# remove method
ages.remove(23)
print(ages) #output - [50, 25, 21, 26, 28, 32, 30, 40] 23 is removed.

# pop method (removes the last item)
ages.pop()
print(ages) #[50, 25, 21, 26, 28, 32, 30] last item is removed.

# index method (finds the index of an item).

print(ages.index(21)) #output - 2

# 'in' is another method to check if a value exists.

print(47 in ages) #output- False
print(50 in ages) #output - True

#count method (to count how many same items).

print(ages.count(28)) #output - 2

# sort method

print(ages.sort()) # returns none (absense of value)
print(ages) # now returns sorted list - [21, 25, 26, 28, 28, 30, 32, 50]

# reverse method (simply reverse the list)

print(ages.reverse())
print(ages) #output - [50, 32, 30, 28, 28, 26, 25, 21] sorted in decending order.

# copy method (copies the
# clear method (makes it empty)
