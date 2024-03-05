#Matthew Howe
#3/5/24
#P2LAB1
#Creating a Circle an using variable expressions

import math
radius = float(input("What is the radius of the circle? "))
print()
diameter = 2 * radius
print(f'The diameter of the circle is {diameter:.1f}')
print()
circumference = 2*3.14*radius
print(f'The circumference of the circle is {circumference:,.2f}')
print()
area = 3.14*math.pow(radius,2)
print('The area of the circle is',format(area,'.3f'))
