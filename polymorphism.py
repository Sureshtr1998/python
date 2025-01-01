# Duck Typing

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Laptop:
    # def __init__(self,ide):
    #     print(ide)
    def code(self,ide):
        ide.execute()

ide1 = PyCharm()

lap1 = Laptop()
# Basically we are saying arguments are dynamic when we are sending class all it cares is whther execute func is there or not
# lap1 = Laptop(ide1)
lap1.code(ide1)

# Operator Overloading

# Here we need to understand behind the scene concepts
# <=======================================>
a= 10
b = 12
# When we do a+b it calls int.__add__ function
print(a+b)
print(int.__add__(a,b))
# when we print an object or variable anything behind the scene it calls __str__ method
print(a)
print(a.__str__())

# <=======================================>
# We can give default as None
class Student:
    def __init__(self,m1=None,m2=None):
        self.m1 = m1
        self.m2 = m2
    # Here we are overriding the add
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    # Overriding greater
    def __gt__(self, other):
        return self.m1 + self.m2 > other.m1 + other.m2

    def __str__(self):
        return ('{} {}'.format(self.m1, self.m2))



st1 = Student(65,34)
st2 = Student(45,74)

s3 = st1 + st2
# The above is equivalent to Student.__add__(s1,s2)

if st1>st2:
    print("S1 wins")
else:
    print("S2 Wins")

print(s3.m1,s3.m2)


# when we print an object or variable anything behind the scene it calls __str__ method
#   By default without str overriding we would get the id
print(st1)
print(st1.__str__())
print(st2)





# Method Overloading

# If argument name is same and types or number of arguments are different
# IN PYTHON METHOD OVERLOADING DOESN"T WORK, WE HAVE TO GO WITH IF ELSE STATEMENTS TO MAKE IT TO WORK BUT IT IS NOT Overloading

class StudentA:
    def sum(self,a,b):
        return a + b
    # We can not have same name methods it would simply rewrites the last one
    def sum(self, a, b,c):
        return a + b + c

astd = StudentA()
s1 = astd.sum(10,11,15)
# s1 = astd.sum(10,11) This is invalid

print(s1)

# Method Overriding

# If argument types and number of arguments are same (in inheritance)

class A:
    def show(self):
        print("In A show")

# Basically if we have two methods with same name and arguments, first priority given to child, if not then only go for MRO based on order of extending

class B(A):
    def showA(self):
        print("In B Show")

a1 = B()

a1.show()


# Abstract class and abstract method,
# only when we have declaration, we can create object for abstract class

from abc import ABC, abstractmethod
# ABC => Abstract Base Classes
# We need to use ABC to make class as an abstract class, in abstract class we shpuld have atleast 1 abstract method
class Computer(ABC):
    @abstractmethod
    def process(self):
        print("Computer abstract")
    # Normal method also we can define, need to use decorator to make method as an abstract
    def process2(self):
        print("Computer normal method")
    #We will get error if we uncomment this as process1 is not defined in child
    # @abstractmethod
    # def process1(self):
    #     print("Computer1 abstract")

class Laptop(Computer):
    def ab(self):
        print("Ab method")
    #     If we comment below it throws error even process exists in abstract class, it is like interface
    # Whatever present in abstract class methods it should be present in child to access
    def process(self):
        print("Laptop process")

l1 = Laptop()
l1.process()
l1.process2()



