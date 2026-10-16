import math

xc = float(input())
yc = float(input())
r = float(input())

x = float(input())
y = float(input())

distance = math.sqrt((x - xc)**2 + (y - yc)**2)

if distance < r:
    print("Точка находится внутри окружности")
elif distance == r:
    print("Точка лежит на окружности")
else:
    print("Точка располагается за ее пределами")