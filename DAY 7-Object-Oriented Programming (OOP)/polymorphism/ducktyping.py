class Duck:
    def speak(self):
        print("Quack")
    def swim(self):
        print("I am a duck i can Swim")

class Dog:
    def speak(self):
        print("Woof Woof")
    def swim(self):
        print("I am a dog i can swim")

def Display(obj):
    obj.swim()
    obj.speak()
    print("Information Displayed")


duck=Duck()
dog=Dog()


Display(duck)
print()
Display(dog)