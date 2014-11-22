class CD(object):
    def __init__(self, id, title, rented, customer_id = None, rental_due = None):
        self.id = id
        self.title = title
        self.rented = rented
        self.customer_id = customer_id
        self.rental_due = rental_due