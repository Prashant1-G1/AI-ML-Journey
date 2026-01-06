company = {
    "IT": {
        "employees": 25,
        "budget": 500000
    },
    "HR": {
        "employees": 10,
        "budget": 150000
    }
}

print(company["IT"]["employees"])

company["HR"]["budget"]+=50000



company["Sales"]={"employees":15,
                  "budget":300000}

print(company)

#2
names = ["Ram", "Sita", "Hari"]
scores = [85, 92, 78]

dic=dict(zip(names,scores))

passed={x:y for x ,y in dic.items() if y>80}

print(passed)

#3
students = {
    "Ram": {"math": 80, "science": 70, "english": 60},
    "Sita": {"math": 90, "science": 95, "english": 88},
    "Hari": {"math": 35, "science": 40, "english": 45}
}

names=[x for x , y in students.items() if all(m>40 for m in y.values() ) ]
print(names)