from os.path import exists
from scv_creating import creating
from interface import show_main_menu


valid = exists('Phonebook.csv')
if not valid:
    creating()

show_main_menu()