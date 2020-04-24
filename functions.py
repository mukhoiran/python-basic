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

print("calculation result", sum(9,5))
