
def add(x,y) :
    c = x+y
    d = x-y
    if __name__ == "__main__":
        print("Main " + __name__)
    else:
        print("Child " + __name__)

    # return c
    return c,d


res1, res2 = add(5,4)
print(res1, res2)

# Pass By value and pass by reference
def update(x) :
    x= 8
    print(x)

a= 10
# We are just passing value, so a and x are completely different, there is no pass by value or pass by reference in python, by default it is value
update(a)
print(a)

def updatelist(ae) :
    ae[1] = 25
    print(a)

lst= [10,20,30]
# In the list case both would be modified a and lst, unlike previous example as lst still referring to same id, we can use copy to avoid
updatelist(lst)
# updatelist(lst.copy()`
print(lst)

# ARGUMENTS
# Using keywords while passing argument and default argument

def person(name, age=18) :
    print(name+": "+str(age+1))

person("Suresh", 25)
person(age=26, name="SUSHA")
person( name="SURI")

# Variable lengths argument (dynamic args)
# Here b is tuple, we can get rid of a also
def allSum(a,*b):
    c = a
    for i in b:
        c=c+i
    print(c)

allSum(3, 4,6,7,8,9)

# To accept key value data we use **, key word variable length
def personData(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)


personData("Suresh", age=27, city="Blr", num=9761511)

# Scope ==> Local variable and global variable


l = 10

def vars() :
    # If we don't use this then global is seperate and local is seperate
    # global l
    # Here it modifies the local variable, it won't affect the global variable, to change global variable we have to use global key word
    l = 15

    # if we want both local and global to be present then use globals
    globals()['l'] = 20
    print(l)

vars()
print(l)


def count(lst) :
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even = even+1
        else:
            odd+=1
    return even,odd



lst = [2,3,56,8,1,9,4,7]

even, odd = count(lst)
print(even,odd)
print("Another example of string Even:{}, odd: {}, {}".format(even, odd,10))

# FIBONACCI

# 0,1,1,2,3,5,8,13

def fibbo(len):
    lst = [0,1]
    for i in range(len -2):
        lst.append(lst[i]+lst[i+1])
    return lst

print(fibbo(10))

# FACTORIAL

def fact(f):
    l=1
    for i in range(1,f+1):
        l = l*i
    return l



print(fact(5))

# Recurssion
import sys
# By default we can call same loop 1000 time to change it we can use set recursion
# sys.setrecursionlimit(1000)
# print(sys.getrecursionlimit())

def factRec(f):
    if f <= 1:
        return f
    else:
       return f * factRec(f-1)


print(factRec(4))

# Lambda function

f = lambda a: a*a

print(f(5))

# Map Filter Reduce

def is_even(n):
    return n%2==0

nums = [3,2,1,4,7,8,9]

evens = list(filter(is_even, nums))

# Using lambda
odds = list(filter(lambda n: n%2 !=0 , nums))


print(evens)
print(odds)

# doubles using map

doubles = list(map(lambda n: n*2,nums))
print(doubles)

#Reduce
from functools import reduce

addingAll = int(reduce(lambda a,b: a+b, doubles))

print(addingAll)

# Decorators

def div(a,b):
    return a/b

def smart_dif(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div = smart_dif(div)
# They both give same values, we are passing function through div and modifying it this is called as decorator
print(div(2,4))
print(div(4,2))


