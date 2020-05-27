from matrix import Matrix
from vector import Vector


m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
             [0.0, 2.0, 4.0, 6.0]])
print(m1)
m2 = Matrix([[0.0, 1.0],
             [2.0, 3.0],
             [4.0, 5.0],
             [6.0, 7.0]])
print(m2)
v1 = Vector([0.0, 1.0, 2.0, 3.0])
v3 = Vector([0.0, 1.0, 2.0, 3.0])
v1 = Vector([0.0, 1.0, 2.0, 3.0])


print("------ m1 + m1 ------")
m3 = m1 + m1
print(m3)
print("------ m1 - m1 ------")
m3 = m1 - m1
print(m3)
print("------ m1 / 2 ------")
m3 = m1/2
print(m3)
print("------ 2 / m1 ------")
m3 = 2/m1
print(m3)
print("------ m1 / 0 ------")
m3 = m1/0
print(m3)
print("------ m1 * 5 ------")
m3 = m1 * 5
print(m3)
print("------ m1 * v1 ------")
m3 = m1*v1
print(m3)
print("------ m1 * m2 ------")
m3 = m1 * m2
print(m3)
print("------ v1 * m1 ------")
m3 = v1*m1
print(m3)
print("------ 5 * m1 ------")
m3 = 5*m1
print(m3)
