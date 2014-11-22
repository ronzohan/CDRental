class CustomerList(object):
    def __init__(self):
        self.customer_list = {}
        
    def add_customer(self, customer):
        self.customer_list[customer.id] = customer