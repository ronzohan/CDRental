import datetime


class CD(object):
    def __init__(self, id, title, rented, customer_id=None, rental_period=None, rental_due=None):
        self.id = id
        self.title = title
        self.rented = rented
        self.customer_id = customer_id
        self.rental_period = int(rental_period)
        self.rental_due = rental_due

    def set_rent(self):
        self.rented = "Yes"
        self.rental_due = datetime.date.today() + \
            datetime.timedelta(days=self.rental_period)
        self.rental_due = self.rental_due.strftime("%m/%d/%Y")