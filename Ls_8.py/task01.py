


def main():
    read_file ('directory.txt')
    print('Введите 1 если хотите найти пользователя: ')
    print('Введите 2 если хотите найти номер телефона: ')
    print('Введите 3 если хотите найти адресс пользователя: ')
    txt = input('')
    if txt == '1':
        Find_user_name()
    elif txt == '2':
        Find_user_number()
    elif txt == '3':
        Find_user_address()

def Find_user_name():
    print('Введите имя, фамилию или отчество пользователя: ')
    n = input('')
    return n

def Find_user_number():
    print('Чей номер хотите найти?: ')
    n = input('')
    return n

def Find_user_address():
    print('Чей адрес вас интересует?: ')
    n = input('')
    return n

def read_file(file_name):
    with open (file_name, 'r' , encoding = 'UTF-8') as file:
        lines = file.readlines()
        headers = ['Name1', 'Name2', 'Name3', 'Number', 'City']
        contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    print(contact_list)
    return contact_list



if __name__ == "__main__":
    main()


# with open('directory.txt', 'w', encoding='UTF-8') as data:
#     data.write('Иванов Иван Иванович 89299219 Москва\n')
#     data.write('Сидоров Петр Сергеевич 812712878 Казань\n')
#     data.write('Петров Петр Петрович 7218281798 Ростов\n')



