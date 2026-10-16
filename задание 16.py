pin = input()

check_len = len(pin) == 4 and pin.isdigit()

check_unique = len(set(pin)) == 4
if pin.isdigit():
    year = int(pin)
    check_year = not (1900 <= year <= 2050)
else:
    check_year = False

if check_len and check_unique and check_year:
    print("OK")
else:
    print("ERROR")