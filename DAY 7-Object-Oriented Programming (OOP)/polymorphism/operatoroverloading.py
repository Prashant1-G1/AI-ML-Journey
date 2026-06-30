class Complex_number():
    def __init__(self,r, i):
        self.real=r
        self.img=i
    
    def __add__(self, other):
        return f"{self.real+other.real} + {self.img+other.img}i"
    

c1=Complex_number(3,4)
c2=Complex_number(3,5)

print(c1+c2)


class person():
    def __init__(self,n,a):
        self.name=n
        self.age=a
    
    def __gt__(self, other):
        return self.age>other.age
    
p1=person("ram",45)
p2=person("hari",56)


if p1>p2:
    print(f"{p1.name} is going to pay the bill")
else:
    print(f"{p2.name} is going to pay the bill")




