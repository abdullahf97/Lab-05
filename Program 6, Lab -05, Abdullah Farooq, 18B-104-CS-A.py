print('Abdullah Farooq')
print('18B-104-CS-A')
print('Lab-05, 24-11-2018')
print('Program 6')

def CubeValues():
    lst=list()
    for i in range(1, 31):
        lst.append(i**3)
    print(lst[:6])
    print(lst[-6:])
CubeValues()
