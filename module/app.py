#import all script from data.py
import data as x

print(x.person)

#import specifiec script from data.py
from data import printName

print(printName('Alex'))
