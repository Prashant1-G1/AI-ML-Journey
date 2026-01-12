import numpy as np
ages=np.array([[3,45,6,23,78,12,21],
               [67,55,43,20,16,45,17]])
teenagers=ages[ages<=16] 
print(teenagers)
adult=ages[(ages>=30) & (ages<=65)]
print(adult)
senior=ages[ages>=65]
print(senior)

even= ages[ages%2==0]
print(even)

adult2=np.where(ages>=16,ages,0)#to keep the same shape of array
print(adult2)