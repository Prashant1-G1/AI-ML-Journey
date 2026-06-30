# Basically python doesn't support method overloading Directly but we can achieve it through various methods mentioned below.

# Method overloading is an object-oriented programming (OOP) feature that 
# allows a class to have multiple methods with the same name but different parameter lists.
# python only selects the latest method so we can achieve it through defult argument, args.

# Method overloading - compilationtime polymorphism
# class Demo():
#     def add (self, a,b,c=0):
#         return a+b+c

# d=Demo()
# print(d.add(1,2))
# print(d.add(1,2,3))

# class Demo2():
#     def add (self, *args):
#         sum=0
#         for i in args:
#             sum=i+sum
        
#         return sum

# d2=Demo2()
# print(d2.add(1,2))
# print(d2.add(1,2,3))

# Method overriding - runtime polymorphism
class father():
    def sleep(self):
        print("He sleeps from 10PM to 5AM")
    def eat(self):
        print("He is eating")

class Son(father):
    def sleep(self):
        print("He sleeps from 12PM to 7AM")

f=father()
s=Son()

f.sleep()
f.eat()
print()
s.sleep()
s.eat()
