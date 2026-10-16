print("Собака короткошерстной породы?")
hair = input().lower()

if hair == "да":
    print("Рост собаки менее 50 см?")
    size_short = input().lower()
    if size_short == "да":
        print("такса")
    else:
        print("дог")

else:
    print("Рост собаки менее 50 см?")
    size_50 = input().lower()

    if size_50 == "да":
        print("шпиц")
    else:
        print("У собаки рост менее 70 см?")
        size_70 = input().lower()

        if size_70 == "да":
            print("У собаки длинные уши?")
            ears = input().lower()

            if ears == "да":
                print("сеттер")
            else:
                print("колли")
        else:
            print("сенбернар")