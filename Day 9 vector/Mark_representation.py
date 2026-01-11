import numpy as np 

stduent1=np.array([12,54,67,78,12])
student2=np.array([34,56,78,98,34])

print(sum(stduent1*student2))

dot=np.dot(stduent1,student2)

print(dot)

mag_A=np.linalg.norm(stduent1)
mag_B=np.linalg.norm(student2)

print(f"{mag_A:.2f},{mag_B:.2f}")

cosine_similarity = dot / (mag_A * mag_B)

print(f"{cosine_similarity:.2f}")