
"""
This is for documentation part alone
"""

# Iterator
nums = [3,5,8,2,4,7,9]

it = iter(nums)
# They both are same, it gives one value at a time
print(it.__next__())
print(next(it))


# Generators
# It gives iterators through generators so we can work one data at a time

def topTen():
    i = 1
    while i<=10:
        # Yield is kind of return but it wont terminate, and it is used to create iterator
        yield i*i
        i+=1

values = topTen()

# print(values.__next__())
for i in values:
    print(i)

# Exception Handling

a = 5
b = 1

try:
    print("Resource opened")
    print(a/b)
    # k = int(input("ENter a  number"))
    # print(k)
except ZeroDivisionError as e:
    print("It is an zero divison",e)
except ValueError as e:
    print("It is an value error",e)
except Exception as e:
    print("It is an exception",e)
finally:
    print("Resource close")

print("Bye")

# Multi threading

from time import sleep
from threading import *

# Need to extend thread class to implemnet threading

class Hello(Thread):
    # run is a keyword which executes by default when we call start method in threading
    def run(self):
        for i in range(5):
            print("Hello")
            # sleep(1)

class Hi(Thread):
    # run is a keyword which executes by default when we call start method in threading
    def run(self):
        for i in range(5):
            print("Hi")
            # sleep(1)

t1 = Hello()
t2= Hi()
# By default start would execute run
t1.start()
# sleep(0.2) #To avoid collision
t2.start()

t1.join()
t2.join()
# Basically bye would be executed immediately by main thread to wait for t1 and t2 threads to complete we use join
print("Bye")

# File Handling

# rb is for read bindary like image
f = open("FileReader/MyData", 'r')

# print(f.read()) It will read all the data inside a file
# print(f.readline(), end="#")
# print(f.readline(), end="#")

# w  won't append it would just rewrite, a is for append, we use wb for binary like image
# f1 = open("abc", 'w')
f1 = open("FileReader/abc", 'w')
# f1.write("This is first line")
# f1.write("This is second line")

# It will  copy Mydata to abc file
for i in f:
    f1.write(i)



# PYthon is both compiled and interpreted language

# ZIP
names= ("2024", "2023", "2022")
comps = ("SAI", "Broadridge", "Stepchange")

zipped = zip(names, comps)
zippedDict = dict(zip(names, comps))
# zipped = set(zip(names, comps))
# zipped = list(zip(names, comps))
for (a,b) in zipped:
    print(a,b)

print(zippedDict)