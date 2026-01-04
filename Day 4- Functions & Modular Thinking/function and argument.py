# name=input("Enter the name of the person: ")
# def birthday(name):
#     print(f"Happy birthday {name}")
#     print("Achieve everything in life")
#     print("Don't give-up and keep grinding/")

# birthday(name)


# def birthday(*args):
#     for arg in args:
#         print(arg)

# birthday(" Happy birthday Prashant", "you are 19 years old")

def birthday2(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}={value}")

birthday2(name="prashant", age=19 )

