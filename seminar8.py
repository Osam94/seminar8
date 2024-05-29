def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = input('Введите новые данные (Фамилия,Имя,Телефон,Описание): ')
            add_user(phone_book, user_data)
        elif choice == 5:
            write_txt('phonebook.txt', phone_book)
        elif choice == 6:
             source_file = input('Введите имя исходного файла: ') 
             dest_file = input('Введите имя файла назначения: ')
             line_number = int(input('Введите номер строки для копирования: ')) 
             copy_user(source_file, dest_file, line_number) 
        choice = show_menu()
       

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6.копировать с одного файла в другом\n"
          "7. Закончить работу")
    choice = int(input("Введите номер действия: "))
    return choice

def read_txt(filename):
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            values = line.strip().split(',')
            if len(values) == len(fields):
                record = dict(zip(fields, values))
                phone_book.append(record)
            else:
                print(f"Ошибка в строке: {line.strip()}")
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ",".join(record.values())
            phout.write(f"{s}\n")

def print_result(phone_book):
    for record in phone_book:
        print(record)

def find_by_lastname(phone_book, last_name):
    result = [record for record in phone_book if record.get("Фамилия") == last_name]
    return result if result else "Абонент не найден"

def find_by_number(phone_book, number):
    result = [record for record in phone_book if record.get("Телефон") == number]
    return result if result else "Номер не найден"

def add_user(phone_book, user_data):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    values = user_data.split(',')
    if len(values) == len(fields):
        record = dict(zip(fields, values))
        phone_book.append(record)
        print("Абонент добавлен")
    else:
        print("Ошибка: Неправильный формат данных")

def copy_user(source_file, dest_file, line_number): 
    with open(source_file, 'r', encoding='utf-8') as src: 
        lines = src.readlines()
        if line_number <= 0 or line_number > len(lines):
            print("Ошибка: Некорректный номер строки")
            return
        line_to_copy = lines[line_number - 1].strip() 
        with open(dest_file, 'a', encoding='utf-8') as dst: 
            dst.write(line_to_copy + '\n')
        print("Запись скопирована")

work_with_phonebook()