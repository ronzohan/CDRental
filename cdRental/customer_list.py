class CustomerList(object):
    def __init__(self):
        self.list = {}

    def add_customer(self, customer):
        self.list[customer.id] = customer

    def get_customer_data(self, id):
        return self.list.get(id)
