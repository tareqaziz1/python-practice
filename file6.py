# conditions (if, else, elif )

is_sunny = True

if is_sunny:
    print("It's a sunny day!")
else:
    print("It's a cold day!")
print("Have a good day!!") # it will be executed without any condition

''' Qns: Price of a chair is 100.
    If buyer is a returning customer, 10% discount will be given.
    Otherwise 5% discount will be given. Pring the payment.
'''

''''
is_returning_customer = True
price = 100

if is_returning_customer:
    discounted_price = price - (price * 0.1)
    print(discounted_price)
else:
    customer_price = price - (price * 0.05)
    print(customer_price)
print("Check the price above")
''
# When is_returning_customer = True outcome is 90
# When is_returning_customer = False outcome is 95

#using elif for 2 or more conditions

If the customar is older than 50 he gets 20% discount. Print the price.'''

is_returning_customer = False
price = 100
customer_age = 51

if is_returning_customer:
    discounted_price = price - (price * 0.1)
    print(discounted_price)

elif customer_age > 50:
    discounted_price = price - (price * 0.2)
    print(discounted_price)

else:
    customer_price = price - (price * 0.05)
    print(customer_price)
