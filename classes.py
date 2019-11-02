class MyClass:
    pass

oa = MyClass()
ob = MyClass()

print(oa)
print(ob)

# 

class Point:
    pass

    def myfunction(self,a: int):
        'this function prints a number that it takes as argument'
        print(a)

p1 = Point()
p1.x = 1
p1.y = 2
p1.myfunction(1)
print(p1.myfunction.__annotations__)
print(p1.myfunction.__doc__)


print(p1.x,p1.y)
