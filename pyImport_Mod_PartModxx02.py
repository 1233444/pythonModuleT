import pyImport_Mod_PartModxx01
import sys
import os



#print location of the standard library
print(os.__file__)

#Added path to the pythonpath envirnoment
sys.path.append('')
# import pyImport_Mod_PartModxx01 as mmxx
# from pyImport_Mod_PartModxx01 import find_index, test
# from pyImport_Mod_PartModxx01 import find_index as fixx, test as txx

course = ['History','Math', 'Physics', 'CompSci']

index = pyImport_Mod_PartModxx01.find_index(course, 'CompSci')

# index = mmxx.find_index(course, 'Math')

# index = fixx(course, 'CompSci')


print(index)
# print(index)


print(dir(pyImport_Mod_PartModxx01.__name__))

print(sys.path)
print()
print(dir(os.path))

#Using data in module depend on how you import from module
#Case $1 if not specify on import statment
# print(mmxx.test)
#case $2 if already specify on import statement then can use it directly
# print(test)
# print(txx)