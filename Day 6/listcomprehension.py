a=[x for x in range(10) if x%2==0]
print(a)

matrix=[[1,2],
        [3,4],
        [5,6]]

flat=[x for row in matrix for num in row]

print(flat)