from cdRental.cd import CD
from cdRental.customer import Customer


class CheckoutCD(object):
    def checkout(self, customer, cd):
        if type(customer) == Customer and type(cd) == CD:
            self.customer = customer
            self.cd = cd

            self.cd.set_rent(customer)
        else:
            raise TypeError("Customer must be of {} and cd must of be".format\
                            (type(customer), type(cd)))
