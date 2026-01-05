with open("C:/Users/Hp/OneDrive/Desktop/AI-Ml-Journey/Day 5-Filehandling/data.txt", "r") as file:
    content=file.read()
    print(content)

with open("C:/Users/Hp/OneDrive/Desktop/AI-Ml-Journey/Day 5-Filehandling/data.txt", "w") as file:
    file.write("\n hello world22222")

with open("C:/Users/Hp/OneDrive/Desktop/AI-Ml-Journey/Day 5-Filehandling/data.txt", "a") as file:
    file.write("\nhello 234")

a="my name is prashant."

word=a.split(" ")

print(len(word))