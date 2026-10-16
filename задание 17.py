A = float(input())
B = float(input())

diagonal_squared = A**2 + B**2

if diagonal_squared <= 169:
    print("YES")
else:
    print("NO")