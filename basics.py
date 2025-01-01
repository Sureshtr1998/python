


# https://www.youtube.com/watch?v=QYUbLevwgDQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=42&ab_channel=Telusko


myname = "Suresh"
print(myname[0:4])
# <============================================>
# LIST
nums = [25, 12, 36, 95,"SA"]
print(nums[0])
values = ['suresh', 12,32,1.4]
mil = [nums, values]
print(mil)
nums.append(54)
# append at last insert in between
nums.insert(2,222)
nums.remove(95)
# If we provide index, it would return the exact index or else it would return last
nums.pop(2)
# Deletes multiple elements
del nums[2:]
print(nums)
# <============================================>
# TUPLES
# () for tuples [] for list, tuples are immutable and list are mutable, mutable allows change
tupNum = (21,9,343,23,"AA")
# tupNum[0] = 77 this is invalid as it doesn't allow to modify
nums[0] = 11 #This is valid
print(tupNum)
# <============================================>
# SET
# Curly brackets for set, it doesn't follow any sequenece, value be shown only once
s={22,14,57,21,67, 14,"DS"}
# We have set of actions such as update, add , remove so on
print(s)
# <============================================>
# Dictionary

data = {1:"Suresh" , 2:"TR", 3:"STG Labs"}
print(data.get(1))

key=["SAI", "Wipro", "StepChange"]
values=['SDE2', "Trainee", "SDE"]
mergeData = dict(zip(key,values))
# print(mergeData["SAI"])
mergeData['Broadridge'] = 'Contract'
del mergeData['Wipro']
print(mergeData)

# We can add list tuples, dictionary inside values
# <============================================>

# Operators
a = 8
b = 5
# We have not
print(a>7 and b<9)

print(a>10 or b<9)

# Number System conversion

print(bin(25)) # Decimal to binary
print(0b1011) #Automatically converts to decimal
print(oct(25)) #Octal
print(hex(25)) #Hexa
print(0x19)

# bit wise operator
#~ this symbol is bitwise compliment if it is 00011 it gives 11100 ,
# 12 & 13 & bitwise and operator
# 12 | 13  | bitwise or operator
# ^(xor) if odd numbers then it will be true 12 ^ 1
# 10 << 2 left shift operator
# 10 << 2 right shift operator


import math
# import math as m #This also works we can use m instead of math it is called alias
# from math import sqrt, pow # To import specific in the package


x = math.sqrt(25)

print(x)
print(math.pi)

# Swapping Variables
a = 10
b = 20
a,b = b,a
print(a,b)

# User Input

# x = int(input("Enter 1st Number"))
# y = int(input("Enter 2nd Number"))
# print(x+y)

# Accepting input from  cmd python basics.py 10 11
# import sys
#
# x = int(sys.argv[1])
# y = int(sys.argv[2])
# print(x+y)


# If else block
i = 10

if i>9:
    print("True")
    print("MULTIPLE STMNTS")
elif i==10:
    print("TRUE ELIF")
else:
    print("ELSE")

# While loop

i = 1
while i<=5:
    print("HELLo",i)
    i = i+1

# For loop
y = [23,54,"xsd"]

for i in y:
    print(i)

# For else loop, here else loop will be executed if none of the if stmnt is true, break is mandatory to make it work

nums = [12,34,76,25,43,21,151,4,7]

for num in nums:
    if num%5 == 0:
        print(num)
        break
else:
    print("Not found")

# Arrays
# The only difference between  array and list is that array should have same values
# Refer Notion for different types of values like 'i', 'f' , 'd' so on
# from array import *
import array as arr

# vals = array('i', [5,.5,2,6]) this is invalid as there is a float here
# There is append, remove, reverse so on in array
vals = arr.array('i', [5,8,2,6])

copyArr = arr.array(vals.typecode, (a for a in vals)) #To copy an array
# copyArr = arr.array(vals.typecode, (a*a for a in vals)) #To copy an array of square
print(vals)
for i in copyArr:
    print(i)

# User input dynamic arrays

# arr = arr.array('i', [])
# n = int(input("Enter the length of the array"))
#
# for i in range(n):
#     x= int(input("Enter the value"))
#     arr.append(x)
#
# print(arr)
# y = int(input("Enter the element you want to get index for"))
# print(arr.index(y))
# arr.remove(y)
# print(arr)



# <============================================================>

# NUMPY
# Multi dimension array we use numpy
# pip install numpy in cmd

from numpy import *
# This might be bit confusing the array which you are seeing below is from numpy not from array

arr = array([1,2,3])

print(arr)

# 6 ways to create an array
# 1) using array <===> this will accept all types and it'd automatically convert to higher type or we can specify the type also
arr = array([1,2,3,4.4,5,"A"])
# arr = array([1,2,3,4.4,5,"A"], int) this is invalid as A can not be type int
print(arr.dtype)

# 2) using linspace <===> this is bit weird so it asks for from and to, and it'd give the float data, if we don't mention the number of items we want we will end up with float vals
arr = linspace(0,20, 21)
# arr = linspace(0,20) We will get weird float vals here
print(arr)

# 3) using arange This is arange not arrange<==> Here last arguments mean steps not number of items we are expecting, it'd skip those steps
arr = arange(1,15,2)
print(arr)

# 4) using logspace <====> This provides logarthimic of data

arr = logspace(1,40,5)

print(arr)

# 5 and 6) zeros and ones <==> It creates zero and ones array

arr = zeros(5)
arrOne = ones(5,int)

print(arr)
print(arrOne)


arr1 = array([1,2,3,4,5])
# arr2 = array([4,6,9,1,3,12]) this is invalid we can not add as length should be same
arr2 = array([4,6,9,1,3])
print(arr1+arr2) # It adds both array
arr1 = arr1 + 5 # it adds 5 to each element
print(arr1)
print(sin(arr1)) # for sin calculation, we can do cos, log, sqrt, sum, min, max, sort, concatenate two arrays and so on
print(sort(arr2))

# Shallow copy and deep copy

# By default it would do shallow copy

arrA = array([1,3,67,84,2])
arrB =  arrA.copy()
arrA[2] = 9 # This would affect both the array elements if we don't use copy method
print(arrA)
print(arrB)


# Multi dimensional arrays
mArr = array([[1,2,3] , [4,2,9]])

print(mArr.ndim) # To get number of dimensions
print(mArr.shape) # To get row and cols, we have size also

# Converting 2d to 1d
arr2 = mArr.flatten()
print(arr2)

# Converting 2d to 3d
bArr = array([[1,2,3,4,5,6], [88,23,53,12,67,21]])
print(bArr.reshape(3,4)) #It converts to 3 x 4, it throws error if length is not proper or if some item is missing
print(bArr.reshape(2,2,3)) #It creates 2 2d array with 2 rows and 3 cols

# Matrices
arr4 = array([[1,2,3,4], [5,6,7,8]])
m = matrix(arr4)
print(m) # We can convert 2d to matrix

print(diagonal(m)) # To get diagonal elements from matrix
print(m.min()) # We have max as well

m1 = matrix('1 2 3; 3 5 4; 5 8 6')#It can convert string to matrix as well
m2 = matrix('4 5 9; 8 1 7; 2 8 1')#It can convert string to matrix as well
print(m1+m2)
print(m1 * m2) # TO do multiplication row and col should be same
