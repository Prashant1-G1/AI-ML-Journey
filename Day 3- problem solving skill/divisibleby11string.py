odd_sum=0
even_sum=0
s=input("enter the number: ")

for i in range(len(s)):
    digit=int(s[i])
    if i%2==0:
        even_sum+=digit
    else:
        odd_sum+=digit

print("True" if (odd_sum-even_sum)%11==0 else "False")

