from read_file import *
from new_user import *


list_of_object_names = []
list_of_names = read_file('names.txt')
for name in list_of_names:
    list_of_object_names.append(NewUsers(name))

print(list_of_object_names[0].user_info())
