def read_sprav():
    sprav = []
    path = 'tel_sprav.txt'
    tel_sprav = open(path, 'r', encoding='utf-8')

    # content = tel_sprav.read()   # Вариант-2
    # print(content)
    # print(type(content))
    for line in tel_sprav:
        n = line.split()
        # print (n)
        dict_ = {
            "last_name": n[0],
            "second_name": n[2],
            "first_name": n[1],
            "tel": n[3],
        }
        # print(dict)
        sprav.append(dict_)
        # print(sprav)

    """Альтернативный вариант"""
    # headers = ['last_name', 'first_name', 'second_name', 'tel']
    # for line in tel_sprav:
    #     line = line.strip().split()
    #     sprav.append(dict(zip(headers, line)))

    tel_sprav.close()
    return sprav


def print_sprav(tel_sprav):
    for item in tel_sprav:
        # print(*(f"{k}: {v}" for k, v in item.items()))
        print(*(f"обычный текст до {v} и после" for v in item.values()))
        # print(item['last_name'], item['first_name'], item['second_name'], item['tel'])

    return None


def add_contact():
    tel_sprav = open('tel_sprav.txt', 'a', encoding='utf-8')
    s = input("Введите ФИО, тел, резделенные пробелами")

    # tel_sprav.writelines( \n, 's')
    tel_sprav.close()


def main():
    # переменная = open ('название файла', 'режим работы', encoding='кодировка')
    while True:
        print("Что хотите сделать?")
        print("1: Вывести данные")
        print("2: Записать новый контакт")
        print("3: Найти контакт")
        print("0: Выйти")

        x = input()
        tel_sprav = read_sprav()
        if x == "1":
            print_sprav(tel_sprav)
        elif x == "2":
            add_contact()
        elif x == "0":
            break
        else:
            print("неверная команда")


if __name__ == "__main__":
    main()