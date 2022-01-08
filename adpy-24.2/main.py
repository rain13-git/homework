from pprint import pprint
import csv
import re

def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

# ваш код
def up_number(contacts_list):
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                         r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                         r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_list_up = list()
    for inf in contacts_list:
        inf_string = ','.join(inf)
        formatted_inf = re.sub(number_pattern_raw, number_pattern_new, inf_string)
        inf_string = formatted_inf.split(',')
        contacts_list_up.append(inf_string)
    return contacts_list_up

def up_full_name(contacts_list):
    name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'
    contacts_list_up = list()
    for inf in contacts_list:
        inf_string = ','.join(inf)
        formatted_card = re.sub(name_pattern_raw, name_pattern_new, inf_string)
        inf_list = formatted_card.split(',')
        contacts_list_up.append(inf_list)
    return contacts_list_up

def join_duplicates(contacts_list):
    for inf in contacts_list:
        for part in contacts_list:
            if inf[0] == part[0] and inf[1] == part[1] and inf is not part:
                if inf[2] == '':
                    inf[2] = part[2]
                if inf[3] == '':
                    inf[3] = part[3]
                if inf[4] == '':
                    inf[4] = part[4]
                if inf[5] == '':
                    inf[5] = part[5]
                if inf[6] == '':
                    inf[6] = part[6]
    contacts_list_updated = list()
    for info in contacts_list:
        if info not in contacts_list_updated:
            contacts_list_updated.append(info)
    return contacts_list_updated


def new_file(contacts_list_up):
    with open("phonebook.csv", 'w',encoding='windows-1251') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(contacts_list_up)

if __name__ == "__main__":
    book = read_file('phonebook_raw.csv')
    book = up_number(book)
    book = up_full_name(book)
    book = join_duplicates(book)
    new_file(book)
