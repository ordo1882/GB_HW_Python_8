phone_book = {}
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        contacts = file.readlines()
        for i, contact in enumerate(contacts, 1):
            phone_book[i] = contact.strip().split(';')

def save_file():
    data = []
    for contact in phone_book.values():
        contact = ';'.join(contact)
        data.append(contact)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def show_contacts(pb: dict):
        print()
        for i, contact in pb.items():
            print(f'{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
        print()

def new_contact():
    name = input('Введите имя контакта: ')
    try:
        phone = input('Введите телефон: ')
        assert phone.isdigit() == True # Проверка на ввод цифр.
    except:
        return print(f'\n\033[91mНомер телефона может содержать только цифры.\033[0m\n')
    comment = input('Введите комментарий: ')
    if len(phone_book) == 0: # Проверка на случай, если все контакты удалены.
        u_id = 1
    else:
        u_id = max(phone_book.keys()) + 1
    phone_book[u_id] = [name, phone, comment]
    return name

def find_contact():
    result = {}
    word = input('Введите слово для поиска: ').lower()
    for i, contact in phone_book.items():
        if word in ''.join(contact).lower():
            result[i] = contact
    return result

def edit_contact():
    result = find_contact()
    show_contacts(result)
    u_id = int(input('Введите ID контакта для изменения: '))
    c_name, c_phone, c_comment = phone_book[u_id]
    name = input('Введите новое имя контакта: ')
    try:
        phone = input('Введите новый телефон: ')
        assert phone.isdigit() == True # Проверка на ввод цифр.
    except:
        return print(f'\n\033[91mНомер телефона может содержать только цифры.\033[0m\n')
    comment = input('Введите новый комментарий: ')
    phone_book[u_id] = [name if name else c_name, phone if phone else c_phone, comment if comment else c_comment]
    return name if name else c_name

def del_contact():
    result = find_contact()
    show_contacts(result)
    u_id = int(input('Введите ID контакта для удаления: '))
    name = phone_book.pop(u_id)
    return name

menu = '''\33[92mГлавное меню\033[0m\33[93m
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Очистить весь список контактов\033[0m\33[91m
    9. Выход\033[0m'''

while True:
    print(menu)
    choice = input("Выберите пункт меню: ")
    match choice:
        case '1':
            open_file()
            print('\nТелефонная книга успешно загружена!\n')
        case '2':
            save_file()
            print('\nТелефонная книга успешно сохранена!\n')
        case '3':
            show_contacts(phone_book)
        case '4': 
            name = new_contact()
            if name:
                print(f'\nКонтакт {name} создан\n')
        case '5':
            result = find_contact()
            show_contacts(result)
        case '6':
            name = edit_contact()
            print(f'Контак {name} изменен!')
        case '7':
            name = del_contact()
            print(f'Контак {name} удален!')
        case '8':
            phone_book.clear()
            print(f'\nТелефонная книга очищена!\n') # Добавил кейс удаления всех контактов.
        case '9':
            print("До свидания!")
            break
        case _:
            print("Ошибка ввода.")