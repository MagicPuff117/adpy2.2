import re
import csv


def read_file():
  with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    return contacts_list



def format_numbers(contacts_list):
  raw_format = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
  new_format = r'+7(\4)\8-\11-\14\2\17\18\20'
  contacts_list_updated = list()
  for card in contacts_list:
    card_as_string = ','.join(card)
    # print(card_as_string)
    formatted_card = re.sub(raw_format, new_format, card_as_string)
    # print(formatted_card)
    card_as_list = formatted_card.split(',')
    contacts_list_updated.append(card_as_list)
  return contacts_list_updated


def format_names(contacts_list):
  raw_format = r'^([А-ЯЁа-яё]+)(\s?)(\,?)([А-ЯЁа-яЁ]+)(\s?)(\,?)([А-ЯЁа-яЁ]*)(\,?)'
  new_format = r'\1\8\4\8\7\8 '
  contacts_list_updated = list()
  for card in contacts_list:
    card_as_string = ','.join(card)
    # print(card_as_string)
    formatted_card = re.sub(raw_format, new_format, card_as_string)
    # print(formatted_card)
    card_as_list = formatted_card.split(',')
    contacts_list_updated.append(card_as_list)
  return contacts_list_updated



# def format_duplicates(contact_list):
#   for i in contact_list:
#     for j in contact_list:
#       if i[0] == j[0] and i[1] == j[1] and i != j:
#         if i[2] == '':
#           i[2] = j[2]
#         if i[3] == '':
#           i[3] = j[3]
#         if i[4] == '':
#           i[4] = j[4]
#         if i[5] == '':
#           i[5] = j[5]
#         if i[6] == '':
#           i[6] = j[6]
#   contact_list_updated = list()
#   for card in contact_list:
#     if card not in contact_list_updated:
#       contact_list_updated.append(card)
#   return contact_list_updated






def write_file(contacts_list):
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)



if __name__ == '__main__':
    contacts = read_file()
    contacts = format_numbers(contacts)
    contacts = format_names(contacts)
    # contacts = format_duplicates(contacts)
    write_file(contacts)