
def read_file(file):
    try:
        with open(file, 'r') as file_to_read:
            names = file_to_read.readlines()
            return names
    except FileNotFoundError as err:
        print('File not found')
        print(err)
