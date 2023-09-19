import os
import functools

def divide_by2(item):
    return item/2

def increment_by1(item,item2):
    return item+item2

def filter_mod(item):
    if (item < 4):
        return True
    else:
        return False
    

print (os.environ['ORIGINAL_XDG_CURRENT_DESKTOP'])
print ("test")



my_ints_list=[1,2,3,4,5,6,7,8]

print (list(map (divide_by2,my_ints_list)))
print(functools.reduce(increment_by1,my_ints_list))
print(list(filter(filter_mod,my_ints_list)))
