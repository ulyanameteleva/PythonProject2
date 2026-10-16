N = int(input())
M = int(input())
K = int(input())

if K <= N * M and (K % N == 0 or K % M == 0):
    print("YES")
else:
    print("NO")