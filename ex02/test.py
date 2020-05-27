from vector import Vector

v1 = Vector([0.0, 1.0, 2.0, 3.0])
print(v1)
v3 = Vector(5)
print(v3)
v1 = Vector((10,15))
print(v1)
print("------ v1 + 5 ------")
v2 = v1 + "bonjour"
print(v2)
print("------ 5 + v1 ------")
v2 = 5 + v1
print(v2)
print("------ 5 - v1 ------")
v2 = 5 - v1
print(v2)
print("------ v1 - 5 ------")
v2 = v1 - 5
print(v2)
print("------ v1 / 5 ------")
v2 = v1 / 5
print(v2)
print("------ 5 / v1 ------")
v2 = 5/v1
print(v2)
print("------ v1 * 5 ------")
v2 = v1 * 5
print(v2)
print("------ 5 * v1 ------")
v2 = 5*v1
print(v2)

print("------ v1 + v3 ------")
v2 = v1 + v3
print(v2)
print("------ v1 - v3 ------")
v2 = v1 + v3
print(v2)
print("------ v1 / v3 ------")
v2 = v1/v3
print(v2)
print("------ v1 * v3 ------")
v2 = v1*v3
print(v2)
