print("Welcome to the tip calculator!")
bill = float(input("What was the total of the bill? $"))
tip = float(input("How much would you like to tip? 10, 12, or 15? "))
if tip != 10 or tip != 12 or tip != 15:
    raise ValueError('That tip option is unavailable')
people = int(input("How many people to split the bill? "))
total = bill + bill * tip / 100
total_per_person = total / people
print("Each person will have to pay: $", round(total_per_person, 2))