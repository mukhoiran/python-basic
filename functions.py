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

printOkay()
printText('This is text')
count(3,2)
