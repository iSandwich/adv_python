import re
import csv
# from pprint import pprint


def main():
    contacts_list = read_file()
    new_data = data_cleaner(contacts_list)
    doubles_finder(new_data)
    write_file(new_data)


def read_file():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


def write_file(new_data):
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_data)


def data_cleaner(contacts_list):
    search_phone_pattern = re.compile(
        '(8|\+7)\s?\(?([0-9]+)\)?[\s|\-]?([0-9]{3})[\-]?([0-9]{2})[\-]?([0-9]{2})[\s\(]*(доб. [0-9]+)?')
    new_phone_pattern = r'+7(\2)\3-\4-\5 \6'
    new_data = []

    for entry in contacts_list:
        new_entry = []

        fio = f'{entry[0]} {entry[1]} {entry[2]}'.split()
        phone_num = search_phone_pattern.sub(new_phone_pattern, entry[5]).strip()

        new_entry.append(fio[0])
        new_entry.append(fio[1])
        if len(fio) == 3:
            new_entry.append(fio[2])
        else:
            new_entry.append('')
        new_entry.append(entry[3])
        new_entry.append(entry[4])
        new_entry.append(phone_num)
        new_entry.append(entry[6])
        new_data.append(new_entry)
    return new_data


def doubles_finder(new_data):
    double_index_pool = {}
    mod_list = []

    for i, entry in enumerate(new_data):
        counter = 0
        for j, double in enumerate(new_data):
            if str(i) not in double_index_pool.keys() and i != j:
                if entry[0] == double[0] and entry[1] == double[1]:
                    double_index_pool[str(j)] = double
                    mod_list.append(doubles_remover(entry, double))
                    counter += 1
        if counter > 0:
            double_index_pool[str(i)] = entry

    for i, item in double_index_pool.items():
        new_data.remove(item)

    for item in mod_list:
        new_data.append(item)

    for item in new_data:
        print(item)
    return


def doubles_remover(list_1, list_2):
    modded_list = []
    for i in range(len(list_1)):
        if len(list_1[i]) >= len(list_2[i]):
            modded_list.append(list_1[i])
        else:
            modded_list.append(list_2[i])
    return modded_list


if __name__ == '__main__':
    main()
