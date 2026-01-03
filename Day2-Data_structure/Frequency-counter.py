count={}

text=input("Enter a text: ")

text=text.split(" ")

for x in text:
    count[x]=text.count(x)

print(count)
