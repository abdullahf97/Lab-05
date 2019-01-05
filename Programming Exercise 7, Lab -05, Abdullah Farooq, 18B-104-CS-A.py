print('Programming Exercise 7')

def projMotion(iniVel, angle, gravity):
    import math
    height = ((iniVel**2)*math.sin(angle*2))/gravity
    print(height)
