A = float(input())
B = float(input())

C = float(input())
D = float(input())
E = float(input())

if (C <= A and D <= B) or (D <= A and C <= B):
    print("YES")

elif (C <= A and E <= B) or (E <= A and C <= B):
    print("YES")

elif (D <= A and E <= B) or (E <= A and D <= B):
    print("YES")
else:
    print("NO")