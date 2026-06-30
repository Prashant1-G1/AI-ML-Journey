class Authors():
    def __init__(self,name,book_name,pages):
        self.name=name
        self.book_name=book_name
        self.pages=pages
    
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"{self.book_name} BY {self.name}"
    
    def __del__(self): #to display the message when used the del method 
        print("Author obj has been deleted")
  

a=Authors("Prashant","Undefeated Villain",348)

print(str(a))
print(len(a))

del a  #deletes the obj a 

print(a)
