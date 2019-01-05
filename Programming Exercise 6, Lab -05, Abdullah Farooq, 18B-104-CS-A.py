print('Programming Exercise 6')

print('Enter the initial velocity, acceleration and time respectively with eqmotion1()')
def eqmotion1(iniVel, accel, time):
    finVel = (iniVel+(accel*time))
    print(finVel,'m/s')
print('Enter the initial velocity, acceleration and time respectively with eqmotion2()')

def eqmotion2(iniVel, accel, time):
    distance = (iniVel + (0.5*(accel*time**2)))
    print(distance, 'm')
print('Enter the initial velocity, acceleration and distance respectively with eqmotion3()')

def eqmotion3(iniVel, accel, distance):
    finVel = ((iniVel**2)+(2*accel*distance))**0.5
    print(finVel,'m/s')
