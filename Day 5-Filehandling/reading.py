import os 

file_path=input("Enter the File Path: ")
file_path=file_path.replace("\\","/")
print(file_path)

if os.path.exists(file_path):
    with open(file_path,"r") as file:
        content=file.read()
    print(content)
else:
    print("File doesn't Exists")
    