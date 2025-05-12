#A program that computes thee body mass index of the user
#author: helyanny perozo
#september 2024

#setting variables for weight and height
weight = float(input('what is your weight (kg)?'))
height = float(input('and what is your height (m)?'))

#computing the BMI
BMI = weight/height**2

#displaying result of user's bmi
print('your body mass index is:', BMI)