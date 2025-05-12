#write program that solves ax2+bx+c = 0 and finds roots ox x (pos and neg)
# a,b,c are floats
# discriminant is (b)^2 - 4ac

import math
x= input('Choose a variable a:')
a = float(x)
y = input('Choose a variable b:')
b = float(y)
z = input('Choose a variable c:')
c = float(z)
discriminant = float(b**2 - 4*a*c)
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant))/(2*a)
    root2 = (-b - math.sqrt(discriminant))/(2*a)
    print('The roots are:', root1, 'and:', root2)
elif discriminant == 0:
    root = -b/(2*a)
    print('repeated real roots', root)
else:
    print('complex roots')
