### Basic Programming.
# Ques1: Write a program which will find all such numbers which are divisible by 7 but are not 
#        multiple of 5, between 2000 and 3200 (Both included.), the numbers obtained should be 
#        printed in a comma-seperated sequence on a single line.

list1 = []
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        list1.append(str(i))
#print(list1)

print(','.join(list1)) ## To print the o/p in comma seperated sequence in a single line.# convert i in str

# ------------------------------------------------------------------------------------------------##

# Ques2: Write a python program to accept user's first and last name and getting them printed in 
#        reverse order with a space between first name and last name.

first_name = input("Enter your first name:")

last_name = input("Enter your last name:")

print(last_name + " " + first_name)

# ------------------------------------------------------------------------------------------------#

# ques3: Write a Python program to find the volume of a sphere with diameter 12 cm.
#        Formula: V=4/3 * π * r 3

pi = 3.14
r = 12
v = 4.0/3.0 * pi * r**3
print(v) ## Manually

## Defining function for diameter of sphere
def dia_sphere(r):
    pi = 3.14
    v = 4.0/3.0 * pi * r**3
    return v

dia_sphere(4)    

## Printing diameter of sphere by input.
diameter_sphere = int(input("Enter the rad:"))
print("Diameter of sphere: ",dia_sphere(diameter_sphere))