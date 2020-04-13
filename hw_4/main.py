# main.py file from homework #3
from logger import file_path_decor

class Contact:
    def __init__(self, name, surname, phone_number, favorite=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite = favorite
        self.notes = args
        self.additional = kwargs

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.phone_number}\n'
        if self.favorite:
            output += 'В избранных: да\n'
        else:
            output += 'В избранных: нет\n'
        for item in self.additional.items():
            output += f'    {item[0]}: {item[1]}\n'
        for note in self.notes:
            output += f'- {note}\n'
        return output


class PhoneBook:
    def __init__(self, title):
        self.contacts = {}
        self.title = title
        self.interface()

    def interface(self):
        interface_text = '''Телефонная книга.
        Выберите действие:
        1 - Просмотреть контакты
        2 - Добавить новый контакт
        3 - Удалить контакт
        4 - Вывести избранные контакты
        5 - Найти контакт
        6 - Завершить работу
        Введите команду: '''
        print('\n' * 50)
        key = input(interface_text)
        print()
        if key == '1':
            self.print_contacts()
        elif key == '2':
            self.add_contact()
        elif key == '3':
            self.delete_contact()
        elif key == '4':
            self.find_favorites()
        elif key == '5':
            self.find_contact()
        elif key == '6':
            return
        else:
            self.interface()

    @file_path_decor('log.txt')
    def print_contacts(self):
        if len(self.contacts) == 0:
            print('На данный момент телефонная книга пуста.')
        else:
            for id, contact in self.contacts.items():
                print(contact)
        input('Нажмите Enter для продолжения...')
        self.interface()

    @file_path_decor('log.txt')
    def add_contact(self):
        contact_id = 'entry_' + str(len(self.contacts))
        for i, item in enumerate(self.contacts.items()):
            alias = 'entry_' + str(i)
            if alias not in self.contacts.keys():
                contact_id = alias

        print(contact_id)
        contact_info = input('Введите имя, фамилию и номер контакта через пробел: ').split(' ')
        contact_name = contact_info[0]
        contact_surname = contact_info[1]
        contact_number = contact_info[2]
        fav_check = input('Добавить контакт в избранные? [Y/N]: ').capitalize()
        if fav_check == 'Y':
            contact_fav = True
        else:
            contact_fav = False
        self.contacts[contact_id] = Contact(contact_name, contact_surname, contact_number, contact_fav)
        input('Нажмите Enter для продолжения...')
        self.interface()

    @file_path_decor('log.txt')
    def delete_contact(self):
        if len(self.contacts) == 0:
            print('На данный момент телефонная книга пуста.')
        else:
            contact_number = input('Введите номер контакта, подлежащего удалению: ')
            key = ''
            for id, contact in self.contacts.items():
                if contact_number == contact.phone_number:
                    key = id
            if key == '':
                    print('Контакт не найден.')
            else:
                print(f'Контакт для удаления:\n{self.contacts[key]}')
                del self.contacts[key]
        input('Нажмите Enter для продолжения...')
        self.interface()

    @file_path_decor('log.txt')
    def find_favorites(self):
        if len(self.contacts) == 0:
            print('На данный момент телефонная книга пуста.')
        else:
            for id, contact in self.contacts.items():
                if contact.favorite:
                    print(contact)
        input('Нажмите Enter для продолжения...')
        self.interface()

    @file_path_decor('log.txt')
    def find_contact(self):
        if len(self.contacts) == 0:
            print('На данный момент телефонная книга пуста.')
        else:
            key = ''
            contact_info = input('Введите имя и фамилию контакта через пробел: ').split(' ')
            contact_name = contact_info[0]
            contact_surname = contact_info[1]
            for id, contact in self.contacts.items():
                if (contact_name == contact.name and contact_surname == contact.surname):
                    print(contact)
                    key = '1'
            if key != '1':
                print('Контакт не найден.')
        input('Нажмите Enter для продолжения...')
        self.interface()


if __name__ == '__main__':
    phonebook = PhoneBook('Book')
#     person = Contact('Umberto', 'Robina', '+999012345678', True,'Характер скверный, не женат',\
#                      origin='mexican', cojones='huge')
#     print(person)