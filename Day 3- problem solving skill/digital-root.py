def digital_root(x):
    while x>=10:
        root=0
        while x>0:
            digit=x%10
            root=root+digit
            x=x//10
        x=root
    return x

print(digital_root(9))
