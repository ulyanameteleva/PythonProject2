num = int(input())

d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

if d1 == d4 and d2 == d3:
    print("Настоящее")
else:
    print("Кривое")