import os


def input_contact():
    if not os.path.isfile('data.txt'):
        f = open('data.txt', 'w')
        f.close()
    with open('data.txt', 'a', encoding='utf-8') as f:
        user = input('Введите имя, фамилию, телефон: ').strip().split()
        f.write(';'.join(user) + '\n')


def print_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    for contact in contacts:
        print(*contact.strip().split(';'))


def find_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('По каким параметрам ищем контакт?:\n1. Имя\n2. Фамилия\n3. Телефон')
        command_index = int(input('Команда: '))
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break
    data = input('Введите данные: ')
    print('Найденные контакты: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data == full_contact[command_index - 1]:
            print(' '.join(full_contact))


def delete_contact():
    temp = []
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = [line.strip() for line in f]
    while True:
        print('По каким параметрам найти контакт для его удаления:\n1. Имя\n2. Фамилия\n')
        command_index = int(input('Команда: '))
        if str(command_index) not in '12':
            print('Неверная команда')
        else:
            break
    del_contact = input('Введите данные контакта: ')
    for contact in contacts:
        if del_contact not in contact:
            temp.append(contact)
    if len(temp) < len(contacts):
        print('Контакт удалён')
    else:
        print('Контакт не найден')

    with open('data.txt', 'w', encoding='utf-8') as f_rep:
        for contact in temp:
            f_rep.write(contact + '\n')


def contacts_replace():
    temp = []
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = [line.strip() for line in f]
    while True:
        print('По каким параметрам найти контакт для его изменения:\n1. Имя\n2. Фамилия\n')
        command_index = int(input('Команда: '))
        if str(command_index) not in '12':
            print('Неверная команда')
        else:
            break
    replace_contact_data = input('Введите данные контакта: ')
    for contact in contacts:
        if replace_contact_data == contact.split(';')[command_index - 1]:
            contact = contact.split(';')
            contact[command_index - 1] = input('Введите новые данные: ')
            print('Данные контакта успешно изменены')
            contact = ';'.join(contact)
        temp.append(contact)

    with open('data.txt', 'w', encoding='utf-8') as f_rep:
        for contact in temp:
            f_rep.write(contact + '\n')
