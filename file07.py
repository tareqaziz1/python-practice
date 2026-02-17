# Logical operators (and, or, not)

'''if a candidate has high score and skills he gets the job'''

has_high_score = True
has_good_skills = False
#logical AND
if has_high_score and has_good_skills:
    print("He is eligible for the job!")
else:
    print("He is not eligible for the job!")

'''if a candidate has good score OR good skills he can get an internship.'''
#logical OR
if has_high_score or has_good_skills:
    print("He is eligible for an intership")
else:
    print("He is not eligible for anything!")

#logical NOT (reverse the boolean value)

if has_high_score and not has_good_skills:
    print("Boolean value is reversed")

# program -  weight converter

weight = int(input("Weight: "))
unit = input("(L) for pounds or (K) for kilograms")

if unit.upper() == "L":
    converted_weight = weight*0.4535
    print(f"Your weight is {converted_weight}")
else:
    converted_weight = weight / 0.4535
    print(f"Your weight is {converted_weight}")

