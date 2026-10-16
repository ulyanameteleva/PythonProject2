x1, y1, x2, y2 = map(int, input().split())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("YES")
else:
    print("NO")