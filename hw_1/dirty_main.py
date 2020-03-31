from datetime import datetime
from application.salary import *
from application.people import *

def menu():
    startup_text = '''\n"Бухгалтерия 1.0"
    1 - запросить список активных сотрудников
    2 - рассчитать объём выплат за текущий период
    3 - Завершить работу программы
    Выберите действие: '''

    while True:
        command = input(startup_text)
        if command == '1':
            print(f'\nТекущая дата: {datetime.now().year}.{datetime.now().month}.{datetime.now().day}')
            get_employees()
        elif command == '2':
            print(f'\nТекущая дата: {datetime.now().year}.{datetime.now().month}.{datetime.now().day}')
            calculate_salary()
        elif command == '3':
            print('\nЗавершение работы...')
            break
        else:
            print('Команда не распознана. Пожалуйста, повторите ввод.')
        input('Для продолжения нажмите Enter...')
        print("\n" * 50)

if __name__ == '__main__':
    menu()