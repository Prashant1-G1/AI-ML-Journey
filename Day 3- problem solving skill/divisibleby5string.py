
number=input("Enter a number: ")

last_digit=int(number[-2::])

print("True" if last_digit%4==0 else "False")