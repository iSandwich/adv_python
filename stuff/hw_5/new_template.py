import json
import os

# documents = []
# directories = {}


def program_start():
    current_path = str(os.path.dirname(os.path.abspath(__file__)))
    f_directories = os.path.join(current_path, 'directories.json')
    f_documents = os.path.join(current_path, 'documents.json')
    with open(f_documents, encoding='utf-8') as docs_file:
        docs = json.load(docs_file)
    with open(f_directories, encoding='utf-8') as dirs_file:
        dirs = json.load(dirs_file)
    return docs, dirs


# def program_end():
#     with open('documents.json', 'w', encoding='utf-8') as docs_file:
#         json.dump(documents, docs_file, ensure_ascii=False, indent=2)
#     with open('directories.json', 'w', encoding='utf-8') as dirs_file:
#         json.dump(directories, dirs_file, ensure_ascii=False, indent=2)


def interface():
    # global documents, directories
    # documents, directories = program_start()

    print('Список доступных команд:')
    print('p - Вывести имя по номеру документа')
    print('l - Вывести список документов')
    print('s - Вывести номер полки по номеру документа')
    print('a - Добавить новый документ')
    print('d - Удалить выбранный документ')
    print('m - Переместить выбранный документ на другую полку')
    print('as - Создать новую полку')
    print('q - Завершить работу программы')

    while True:
        key = input('\nВведите ключ нужной команды: ')
        if key == 'p':
            print_name()
        elif key == 'l':
            docs_list()
        elif key == 's':
            get_shelf_no()
        elif key == 'a':
            add_doc()
        elif key == 'd':
            delete_doc()
        elif key == 'm':
            move_doc()
        elif key == 'as':
            add_shelf()
        elif key == 'q':
            # program_end()
            break
        elif key == 'c':
            contents()
        else:
            print('Ошибка: недопустимый ключ команды. Попробуйте повторить ввод.')
    print('\nРабота программы завершена.')


def print_name():
    owner_name = 'error'
    doc_no = input('Введите номер документа: ')
    for document in documents:
        if doc_no == document['number']:
            owner_name = document['name']
            print(f'Имя владельца: {owner_name}')
    if owner_name == 'error':
        print('Ошибка: в каталоге отсутствует документ с таким номером!')


def docs_list():
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


def get_shelf_no():
    shelf_no = 'error'
    doc_no = input('Введите номер документа: ')
    for directory in directories:
        if doc_no in directories[directory]:
            shelf_no = directory
            print(f'Номер полки: {shelf_no}')
    if shelf_no == 'error':
        print('Ошибка: в каталоге отсутствует документ с таким номером!')


def add_doc():
    doc_check = 'clear'
    doc_no = input('Введите номер документа: ')
    for directory in directories:
        if doc_no in directories[directory]:
            doc_check = 'error'

    if doc_check == 'clear':
        doc_type = input('Введите тип документа: ')
        owner_name = input('Введите имя владельца: ')
        shelf_no = input('Введите номер полки: ')
        new_line = {"type": doc_type, "number": doc_no, "name": owner_name}
        documents.append(new_line)
        directories.setdefault(shelf_no, [])
        directories[shelf_no].append(doc_no)
        print('Запись успешно добавлена')
    else:
        print('Ошибка: добавляемый документ уже существует в каталоге!')


def delete_doc():
    shelf_no = 'nope'
    doc_no = input('Введите номер документа: ')
    for directory in directories:
        if doc_no in directories[directory]:
            shelf_no = directory

    if shelf_no == 'nope':
        print('Ошибка: в каталоге отсутствует документ с таким номером!')
    else:
        for document in documents:
            if doc_no in document['number']:
                documents.remove(document)
        directories[shelf_no].remove(doc_no)
        print(f'Документ №{doc_no} усппешно удалён из каталога')


def move_doc():
    shelf_no = 'nope'
    doc_no = input('Введите номер документа: ')
    for directory in directories:
        if doc_no in directories[directory]:
            shelf_no = directory

    if shelf_no == 'nope':
        print('Ошибка: в каталоге отсутствует документ с таким номером!')
    else:
        print(f'Выбранный документ находится на полке № {shelf_no}')
        new_shelf_no = input(f'Введите номер новой полки: ')
        if new_shelf_no == shelf_no:
            print(f'Документ № {doc_no} взяли, стряхнули с него пыль и вернули на полку № {shelf_no}')
        else:
            if new_shelf_no not in directories.keys():
                directories.setdefault(new_shelf_no, [])
            directories[shelf_no].remove(doc_no)
            directories[new_shelf_no].append(doc_no)
            print(f'Документ № {doc_no} был успешно перемещён на полку № {new_shelf_no}')


def add_shelf():
    shelf_no = input('Введите номер полки: ')
    if shelf_no in directories:
        print('Ошибка: полка с таким номером уже существует в каталоге!')
    else:
        directories.setdefault(shelf_no, [])
        print(f'Полка № {shelf_no} успешно создана')


def contents():
    print('Documents:')
    for document in documents:
        print(document)
    print('\nDirectories:')
    for directory in directories:
        print(directory, ':', directories[directory])


if __name__ == '__main__':
    documents, directories = program_start()
    interface()
