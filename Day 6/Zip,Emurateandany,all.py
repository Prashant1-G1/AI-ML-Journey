#zip
#zip() pairs elements from multiple iterables.

fruit=["Apple","Mango","Banana"]

price=[98,107,67]

result=zip(fruit,price)

value=list(result)

print(value)

#convert into dictionary
subject=["Math","English","Science"]
marks=[98,98,56]

dic=dict(zip(subject,marks))

print(dic)

for x , y in dic.items():
    print(f"{x}:{y}")

#Important rule

test=list(zip([1,2,3], [10,20]))  # stops at 2

print(test)


# 4. enumerate()
# Why enumerate()?

# To get index + value together.
# list only

for i, x in enumerate(["a", "b", "c"],start=1):
    print(f"{i}:{x}")


# any() and all()
# any()

# Returns True if at least ONE element is True

marks = [30, 40, 90]
print(any(m >= 40 for m in marks))

# all()

# Returns True only if ALL elements are True
marks = [70, 80, 90]
print(all(m >= 40 for m in marks))

#very very important Pattern 
data=[12,13,14,-8]
if all(x>0 for x in data):
    print("All value are positive")
else:
    print("All values are not positive")

