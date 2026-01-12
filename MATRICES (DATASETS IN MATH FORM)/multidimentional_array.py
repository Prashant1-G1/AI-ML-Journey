import numpy as np
array=np.array(['A','B','C'])


array2=np.array([["A","B","C"],
                ["D","E","F"],
                ["G","H","I"]])

array3=np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
                 [["J","K","L"],["M","N","O"],["P","Q","R"]],
                 [["S","T","U"],["V","W","X"],["Y","Z"," "]]])

print(array3[0][0][0]) #chain indexing
print(array3[0,0,0])#mutidimentional indexing
print(array2[0,0])

word=array3[0,1,0]+array3[1,1,2]+array3[0,2,0]
print(word)