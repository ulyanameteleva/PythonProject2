n = int(input())

if 11 <= n <= 14:
    print(n, "попугаев")
else:
    # 2. Если не исключение, смотрим на самую последнюю цифру числа
    last_digit = n % 10

    if last_digit == 1:
        print(n, "попугай")
    elif 2 <= last_digit <= 4:
        print(n, "попугая")
    else:
        # Для цифр 5, 6, 7, 8, 9 и 0
        print(n, "попугаев")