N, K, M = map(int, input().split())

dist1 = abs(K - M) - 1

dist2 = N - abs(K - M) - 1

if dist1 < dist2:
    print(dist1)
else:
    print(dist2)