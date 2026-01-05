a="aaabbb"
total={}
if " " in a:
    text=a.split(" ")
    for x in text:
        total[x]=text.count(x)
else:
    for x in a:
        total[x]=a.count(x)

print(total) 