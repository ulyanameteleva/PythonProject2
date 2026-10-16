score = input()
score1, score2 = map(int, score.split(":"))

if score1 > score2:
    print(1)
elif score2 > score1:
    print(2)
else:
    print(0)