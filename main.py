#1-misol
students = {
    "Ali": 85,
    "Vali": 90,
    "Hasan": 78,
    "Husan": 92
}
print(students)

max_ball = max(students.values())

for v, k in enumerate(students):
    if max_ball == students[k]:
        print(k)
        break

#2-misol
sales = {
    "apples": 50,
    "oranges": 75,
    "bananas": 30,
    "pears": 45
}
print(sales)

summa = sum(sales.values())
print(summa)

#3-misol
grades = {
    "Math": 80,
    "Physics": 75,
    "Chemistry": 85,
    "Biology": 90
}

for subject, grade in grades.items():
    if grade > 75:
        print(subject, grade)


#4-misol
inventory = {
    "pen": 10,
    "pencil": 20,
    "notebook": 15,
    "eraser": 5
}
print(inventory)

for key, value in inventory.items():
    if  value < 10:
        print(key, value)

#5-misol
products = {
    "A": 100,
    "B": 200,
    "C": 150,
    "D": 250
}
print(products)

summa = sum(products.values())
print(summa)

x = summa / len(products)
print(x)

#1-misol
d = dict()

d["x"] = 10
d["y"] = 20
d["z"] = 30

print(d)

#2-misol
d = {
    "a": 5,
    "b": 10
}
print(d)

d["c"] = 15
d["d"] = 20
print(d)

#3-misol
d = dict(name="Ali", age=20)
print(d)
d['age'] = 25
print(d)

#4-misol
d = {}

for i in range(3):
    key = input(f"{i+1}-kalitni kiriting: ")
    value = input(f"{i+1}-qiymatni kiriting: ")
    d[key] = value

print("Natijaviy dictionary:", d)

#5-misol
d1 = {"x": 1, "y": 2}
d2 = {"y": 3, "z": 4}

d1.update(d2)

print(d1)

#1-misol
grades = {
"Math": 80,
"Physics": 90,
"Chemistry": 85
}
print(grades.keys())


#2-misol
grades = {
    "Math": 80,
    "Physics": 90,
    "Chemistry": 85
}
print(grades.values())
print(sum(grades.values()))


#3-misol
grades = {
    "Math": 80,
    "Physics": 90,
    "Chemistry": 85
}
for key, ball in grades.items():
    if  ball > 85:
        print("Excellent")
        print(ball)


#4-misol
inventory = {
    "pen": 10,
    "pencil": 20,
    "notebook": 15
}
print(inventory)
eraser_count = inventory.get("eraser", 0)
print(eraser_count)

#5-misol
scores = {"Ali": 85, "Vali": 90, "Hasan": 78}

for name, score in scores.items():
    print("{} scored {} points".format(name, score))

#1-misol
students = {"Ali": [85, 90], "Vali": [78, 88], "Hasan": [92, 95]}

averages = {}

for name, scores in students.items():
    averages[name] = sum(scores) / len(scores)

print(averages)

#2-misol
inventory = {
    "pens": [10, 15],
    "pencils": [5, 10],
    "notebooks": [20, 25]}

total_inventory = {}
for item, counts in inventory.items():
    total_inventory[item] = sum(counts)

print(total_inventory)

#3-misol
grades = {
    "Math": [80, 85, 90],
    "Physics": [70, 75, 80]
}
print(grades)
for subject in grades:
    print(subject, "bo‘yicha eng yuqori ball:", max(grades[subject]))

#4-misol
students = {
    "Ali": [85, 90, 95],
    "Vali": [70, 75, 80]
}

for name, scores in students.items():
    total = sum(scores)
    if total > 250:
        print(f"{name}: Passed")
    else:
        print(f"{name}: Failed")


#5-misol
scores = {
    "Ali": [10, 20], 
    "Vali": [5, 15], 
    "Hasan": [20, 25]
}

for student, marks in scores.items():
    average = sum(marks) / len(marks) 
    if average > 15:
        grade = "A"
    else:
        grade = "B"
    print(f"{student}: {grade}")










