class NewUsers():
    def __init__(self, name):
        self.name = name

    def user_info(self):
        with open(self.name + '.txt', 'a') as f:
            f.write(self.name)
