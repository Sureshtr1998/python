# By default init will be called whenever we create Comp object
# Self will be by default sent when we are creating any method in class
class Comp:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        print("In Init")

    def config(self):
        print("Config is: ", self.cpu, self.ram)

comp1 = Comp('i5',16)
comp2 = Comp('i7', 32)

comp1.config()
comp2.config()


# Comparing two object properties


class Person:
    def __init__(self):
        self.name="Suresh"
        self.age= 26
    def compare(self,other):
        return self.age == other.age


p1 = Person()
p2 = Person()

p1.age = 27
print("P1 : ",p1.name, p1.age)
print("P2 : ",p2.name, p2.age)

print(p1.compare(p2))

# Instance variables and class variables

class Car:
    # This block is class variables
    wheels = 4

    def __init__(self):
        # Below is instance variable
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()
# To change instance variable we can target c1 or c2, to change class variable we have to target class which affects globally
Car.wheels = 3
# c1.wheels = 5 this is also valid, we can change for specific objects as well
c1.mil = 7
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

# There are 3 different variables instance , class and static variables


class Student:
    schoolName = "HVP"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    # Below is an instance method which works with instance variable
    def get_m1(self):
        return self.m1

    # Below is an class method which works with class variable, we have to use decorator
    @classmethod
    def getSchool(cls):
        return cls.schoolName

    # Below is an static method, we have to use decorator
    @staticmethod
    def info():
        print("This is a static method, if something is completely general like factorial then we can use this")

s1 = Student(12,34,64)
s2 = Student(19,14,89)
print(s1.m1)
# We will pass Class over here as it does not depend on the arguments or object
print(Student.getSchool())
Student.info()

# Inner class

class Stud:
    def __init__(self,name, roll):
        self.roll = roll
        self.name = name
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.ram = 16
        def show(self):
            print(self.brand, self.ram)


s1 = Stud('Sur', 1)
s2 = Stud('Suresh', 2)

s1.show()
s2.show()

print(s2.lap.brand)

# Inheritance

# There are three types of imheritance multiple, single and multi level


class A:
    def __init__(self):
        print("IN A Init")
    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")

class B:
    def __init__(self):
        print("IN B Init")

    def feature1(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")

# If there are same method names in the inheritance class it would work on priority first prioity is it will check whether method name is present in the same class
# Second priority is based on how we inherit if it is B,A then B is prioritized, which is called Method Resolution Order (MRO)
# class C(A) Single level inheritance

# Multiple Inheritance
# If class B inherits class A and class C inherits class B we call Class C as multi level inheritance
class C(B, A):
    def __init__(self):
        # Here we use super to call the init if we need, here if both classes have init, it goes for MRO, based on order left one would be given priority
        super().__init__()
        print("IN C Init")

    def feature5(self):
        print("Feature 5")


a1 = A()
c1 = C()
a1.feature1()
c1.feature1()

