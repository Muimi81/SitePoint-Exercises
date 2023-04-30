#This is a test comment in python programming
print("Hello World")
#This prints some text
print("I'm Nzangi Muimi")

red_bucket = "Quantity Surveyor"
print (red_bucket) #this prints the variable name
print (type(red_bucket)) #prints out the class of the assingned variable

Thomas_Age = 3
Age_At_Nursery = 5

if Thomas_Age < Age_At_Nursery:
    print ("Thomas should be in pre-school")

elif Thomas_Age == Age_At_Nursery:
    print ("Enjoy kindergarten")

else:
    print ("Thomas should be in another class")

print ("Nzangi Muimi has a very great channel")

def print_nzangi():
    text = "Nzangi Muimi has a great channel"
    print (text)
    print (text)
    print (text)

print_nzangi ()
print_nzangi ()
print_nzangi ()

def print_james (text):
    print (text)
    print (text)
    print (text)

print_james ("James Muimi Nzangi is a Quantity Surveyor")

def school_age_calculator (age,name):
    if age < 5: 
        print ("Enjoy the time!" , name, "is only", age)
    
    elif age == 5:
        print ("Enjoy kindergarten," , name)

    else:
        print ("They grow up so fast!")

school_age_calculator(5, "Thomas")

def add_ten_to_age (age):
    new_age = age + 10
    return new_age

How_old_will_i_be = add_ten_to_age (7)

print (How_old_will_i_be)


#Python_Loops

#While_Loop_as_shown_below

x = 0
while (x<5):
    print (x)
    x = x + 1

#For Loop below

for x in range (5,10):
    print (x)


days = ("Mon", "Tue", "Wed", "Thur", "Fri")

for d in days:
    if d == ("Thur"): continue
    print (d)


#working with libraries

import math
print ("pi is", math.pi)