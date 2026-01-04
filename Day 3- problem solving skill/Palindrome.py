def palindorme(x):
    c=x
    reverse=0
    while x>0:
        digit=x%10
        reverse=reverse*10+digit
        x=int(x//10)
    if reverse==c:
        return print(f"{c} is Palindrome")
    else:
        return print(f"{c} is not palindrome")

palindorme(121)


