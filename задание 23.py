pos = int(input())

if pos == 1:
    print(0)
else:
    pos = pos - 1

    if pos <= 9:
        print(pos)
    elif pos <= 9 + 180:
        pos = pos - 9
        number = 10 + (pos - 1) // 2

        digit_index = (pos - 1) % 2

        if digit_index == 0:
            print(number // 10)
        else:
            print(number % 10)

    else:
        pos = pos - 9 - 180
        number = 100 + (pos - 1) // 3
        digit_index = (pos - 1) % 3

        if digit_index == 0:
            print(number // 100)  # Первая цифра (сотни)
        elif digit_index == 1:
            print((number // 10) % 10)  # Вторая цифра (десятки)
        else:
            print(number % 10)  # Третья цифра (единицы)