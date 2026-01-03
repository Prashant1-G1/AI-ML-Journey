# function is defined by def and it is used so be don't have write the same code in multiple places

def sum_of_two_num(a, b):
    sum=a+b
    return sum

print(sum_of_two_num(4,5))


# there are many inbuild python functions for example string function


a="apple"

print(a.upper())

print(a.lower())

print(a.capitalize())

print(a.center(10))

print(a.isalpha())

print(a.count("p"))

b=("1","2","3")

re="-".join(b)

print(re)

c="    ball   "
print(c.strip()) 

d="www.google.con"

d=d.replace("www.","")
d2=d.split(".")

print(d2)



