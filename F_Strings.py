#F-strings
age = 20
txt = f"My name is Hely, I am {age}"
print(txt)

price = 100
txt = f"the price is {price} dollars"
print(txt)

#Placeholder modifiers
#legal format .2f means number w 2 decimals

price = 100
txt = f"the price is {price:.2f} dollars"
print(txt)

#can also perform math operations
txt = f"the price is {20 * 5} dollars"
print(txt)
