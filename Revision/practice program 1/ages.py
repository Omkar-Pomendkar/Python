# WAP to User will input (3ages).Find the oldest one

a = int(input("Enter the age 1"))
b = int(input("Enter the age 2"))
c = int(input("Enter the age 3"))


max = a

if max < b :
    max = b
if max < c:
    max = c
print(max)