f1=open("C:/Users/Hp/OneDrive/Desktop/AI-Ml-Journey/Day 5-Filehandling/lotm.jpg",'rb') 

print(f1.read())

f2=open("C:/Users/Hp/OneDrive/Desktop/AI-Ml-Journey/Day 5-Filehandling/lotm2.jpg","wb") 

for i in f1:
    f2.write(i)