print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
   
  
  

#import ImportMod as mm
from ImportMod import find_index, test
#from ImportMod import *
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')

#print(index)
#print(test)
print(sys.path)
