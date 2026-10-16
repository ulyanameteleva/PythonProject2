r1, r2, r3 = map(int, input().split())

best = r1
if r2 > best:
    best = r2
if r3 > best:
    best = r3

print(best)

