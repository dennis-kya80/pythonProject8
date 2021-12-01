from array import *
my_array = array("i",[1,2,3,4,5])
for i in my_array:
    print(i)
my_array = array("i",[1,2,3,4,5])
my_array.append(6)
print(my_array)

my_array = array("i",[1,2,3,4,5])
my_extnd_array = array("i",[7,8,9,10])
my_array.extend(my_extnd_array)
print(my_array)

