#Tuple

# Tuple is used to store items. Tuple cannot be modified. (no add or remove option).
# Tuple is immutable (not changable).


numbers = (1,2,3,4,5,1,2,3)

print(numbers[0])

# Cound function
print(numbers.count(1)) #output- 2

# Index function

print(numbers.index(4)) ##output- 3

# Unpacking
coordinates = (1,2,3)

# simple way --
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# better way --

x, y, z = coordinates

print(f"x,y & z - {x,y,z}") #x,y & z - (1, 2, 3)

# It also works with list

new_coordinates = [4,5,6]

p, q, m = new_coordinates
print(f"p,q & m - {p,q,m}") #output- p,q & m - (4, 5, 6)


