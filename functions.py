"""
============= FUNCTIONS ==============
"""

def printOkay():
    print('-----------')
    print(' OKAY ')
    print('-----------')

#with parameter
def printText(param = ''):
    print('-----------')
    print(param)
    print('-----------')

#number calculation
def count(a, b):
    print('Sum from a and b is', a+b)

#printOkay()
#printText('This is text')
#count(3,2)

"""
Return on Functions
"""

def sum(a,b):
    return a + b

#print("calculation result", sum(9,5))

"""
*Args, **Kwargs
"""

def printData(*args):
    print(args)

def printData2(**kwargs):
    for key, value in kwargs.items():
        print(key + " - " + value)

printData('steve','joe')
printData2(name = 'Jhon', age = '21', hobby = 'jogging')
