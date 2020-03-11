try:
    with open('names.txt', 'r') as file_to_write:
        names = file_to_write.readlines()
except FileNotFoundError as err:
    print('File not found')
    print(err)


print(names)
