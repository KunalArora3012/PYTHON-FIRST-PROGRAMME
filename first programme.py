name= "tony stark"
age =51
is_genius = True
print(name.upper())
print(name)
print(age)

old_age = input("enter your old age : ")


1
new_age = int(old_age) + 2
print(new_age)

first= input("enter your first number : ")
second = input("enter your second number : ")

sum = int(first) + int(second)

print( "your sum is : " + str(sum))

print(name.find("t"))
print(name.replace("tony stark" , "iron man"))
print("s" in name)

age= 0
if age >= 8:
    print("you are adult")
    print("u can vote now ")
print ("thank you")

first = input("enter your first number : ")
operator = input("enter your operator (+,-,/,*,%) :" )
second = input("enter your second number : ")

first = int(first)
second = int(second)

if operator == "+" :
    print(first + second)
elif operator == "-" :
    print(first -second)
elif operator == "/" :
    print(first / second)
elif operator == "*" :
    print(first * second)
elif operator == "%" :
    print(first % second)

else:
    print("invalid operations")

i=0

while i <=5 :
    print(i)
    i= i+1

i=5

while i >=0 :
    print(i)
    i= i-1

for i in range (5):
    print(i*"*")
    i= i+1

mark = (95,98,97)
print(mark)

for score in mark:
    print(score)
print (mark[2])
print(mark[0:2])
print(mark.count(95))

mark = [95,98,97]
mark.append(99)
print(mark)
mark.insert(0,100)
print(99 in mark)
print(len(mark))
i=0
while i <len(mark):
    print(mark[i])
    i=i+1
mark.clear()
print(mark)



students = ["ram", "shyam" ,"radha" , "radhika" "krishna"]
for students in students :
    if students == "radha" :
        break;
    print(students)
for students in students :
    if students == "shyam" :
        continue;
    print(students)


marks = {"physice" : 95,"chemistry" :98,"bio" :97}

for score in marks:
    print(score)
print(marks["chemistry"])
marks ["physice"] = 97
print(marks)



import math
print(dir(math))

from math import sqrt
print(sqrt(4) )

from math import *
print(sqrt(4) )

def print_sum(first , second):
    print(first + second)

print_sum(1,200)