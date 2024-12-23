import math

lists = [2, 3, 5, 5, 6.9, 42, 2 / 4, 7 / 3, 53 / 55 / 6, 6 / 4.5 / 6, 6.64, 5, 6, 5, 4, 3, 2, 5, 5, 66, 6, 4, 3, 5, 3,
         3.54, 8, 5, 56, 4, 35, 4, 4, 8]

comp = [[i, j, k] for i in lists if int(i) % 2 == 0 for j in lists if int(j) % 3 == 0 for k in lists if int(k) % 5 == 0]
comp2 = [[i for i in lists if int(i) % 2 == 0], [k for k in lists if int(k) % 3 == 0],
         [k for k in lists if int(k) % 5 == 0]]
# print(comp)
print(comp2)

original = [[1, 2], [3, 4]]
shallow_copy = original.copy()

shallow_copy[0][0] = 999

print("Original:", original)  # [[999, 2], [3, 4]]
print("Shallow Copy:" * 2, shallow_copy * 2)  # [[999, 2], [3, 4]]

tup = (1, 2, 4, 5)
# print(tup.sort())
from math import *

pi = 3
print(math.pi)


class A:
    m = 5

    def __init__(self):
        pass

    def __new__(cls):
        print(cls)


# a=A()
# b=A()
# A.m=11
# print(a.m)
# print(b.m/)


class A:
    def process(self):
        print("A")


class B(A):
    def process(self):
        print("B")
        super().process()


class C(A):
    def process(self):
        print("C")
        super().process()


class D(B, C):
    def process(self):
        print(self)
        print("D")
        super().process()


obj = D()
obj.process()


class M:
    pass


m = M()
print(m)


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            print(cls)
        return cls._instance


obj1 = Singleton()
obj2 = Singleton()


class MyClass:
    count = 0  # A class-level variable

    @classmethod
    def increment_count(cls):
        cls.count += 1  # Modify the class variable
        print("CLS:",cls)
        print(f"Count is now {cls.count}")

    def increment(self):
        print("SELF:",self)
        self.count += 1  # Modify the class variable
        print(f"Count is now {self.count}")

MyClass.increment_count()  # Output: Count is now 1
MyClass.increment_count()  # Output: Count is now 2
# MyClass.increment()
