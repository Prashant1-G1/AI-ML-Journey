dic={name:len(name) for name in ["hari","Sita","gita"]}
print(dic)

#with if condition
scores={"math":98,"English":41,"Science":80}

passed={subject:marks for subject , marks in scores.items() if marks>=60}

print(passed)

#in nested dictionary

scores2={"Ram":{"Math":98,"Science":50},
        "Hari":{"Math":40,"Science":90}}

passed2={name:{s:m for s, m in marks.items() if m>80 } for name , marks in scores2.items()}

print(passed2)