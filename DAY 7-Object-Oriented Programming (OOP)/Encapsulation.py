class Students():
    def __init__(self,name,age,roll_no):
        self.name=name #Public instance variable
        self._age=age #Protected Instance Variable   can be acessed in both class and inherited class
        self.__roll_no=roll_no # prive Instance Variable    Can be accessed on in the class

    def __display(self):
        print(f"Your name is {self.name} and You are {self._age} years old and Your roll no is {self.__roll_no}")
    
    def displayPrivateData(self):
        self.__display()

class Branch(Students):
    def show(self):
        print(f"Your age is {self._age}")


s1=Students("prashant",19,21)

print(s1.name)
print(s1._age)
# print(s1.__roll_no)   will not work since we can't access private varialbe outside the class

print(s1._Students__roll_no)   # will work 

# s1.__display() won't work
# s1._Students__display()  will work


s1.displayPrivateData()