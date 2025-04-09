# color=["red","yellow","green"]

# color.append("blue")
# print(color)
# color.insert(3, "gray")
# print(color)
# color.pop()
# print(color)
# color.remove("yellow")
# print(color)
# print(color[1]
# print(color[-1])

student={
    "name":"sanjana",
    "age":"20",
    "class":"bca"
}
print(student)
print(student.get("grade","not defined"))
print(student["name"])
print(student.get('age'))

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)