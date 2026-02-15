# While loop syntax - ( while condistion: )
# As long as the condition is true the code will be executed

i = 1
while i <= 5:
    print(i)
    i += 1
print("finished")


# Print half pyramid with asterisks
j = 1
while j <= 5:
    print(j * "*")
    j += 1

# Make a 6 row pyramid

row = 6
z = 1

while z <= row:
    spaces = row - z
    stars = 2 * z - 1

    print(" " * spaces + "*" * stars)
    z += 1





