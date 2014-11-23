class Customer(object):
    def __init__(self, id, name):
        if type(id) == str:
            id = int(id)

        self.id = id
        self.name = name
