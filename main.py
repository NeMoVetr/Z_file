from logger import input_contact, print_contact, find_contact, delete_contact, contacts_replace


def menu():
    text = '' \
           "Главное меню:\n" \
           "1 - Запись контакта\n" \
           "2 - Вывод всех контактов\n" \
           "3 - Поиск по фамилии\n" \
           "4 - Удаление контакта\n"\
            "5 - Изменить контакт\n"
    print(text)
    while True:
        comand = int(input('Введите команду: '))
        if comand == 1:
            input_contact()
        if comand == 2:
            print_contact()
        if comand == 3:
            find_contact()
        if comand == 4:
            delete_contact()
        if comand == 5:
            contacts_replace()
        if comand == 0:
            break
        print('_' * 30)


if __name__ == '__main__':
    menu()
