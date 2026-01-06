Student={}
while True:
    name=input("Enter the student name: ")
    subject=input("Enter the subject name: ")
    marks=int(input("Enter the marks obtained: "))
    exit=input("do you want to exit?(y/n): ").lower()
    Student[name]={"Makrs":{subject:marks}}
    if exit=="y":
        for x in Student.keys():
            print(f"Name={x}")
            for key , Value in Student[name]["Makrs"].items():
                print(f"{key}:{Value}")          
                
        False