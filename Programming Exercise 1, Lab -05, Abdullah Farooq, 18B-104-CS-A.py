print('Abdullah Farooq')
print('18B-104-CS-A')
print('Lab-05, 24-11-2018')
print('Programming Exercise 1')

def area():
    import math
    print('Area of the cylinder')
    radius1 = eval(input('Enter the radius of the cylinder: '))
    height1 = eval(input('Enter the height of the cylinder: '))
    area1 = (2* math.pi * radius1 * height1) + (2* math.pi *radius1**2)
    print("The area of the cylinder is {0:.{1}f}cm\u00b2".format(area1, 4))
area()
def volume():
    import math
    print('Volume of the cylinder')
    radius2= eval(input('Enter the radius of the cylinder: '))
    height2 = eval(input('Enter the radius of the cylinder: '))
    volume1 = (math.pi * (radius2**2) * height2)
    print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume1, 4))
volume()
