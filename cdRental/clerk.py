from cdRental.cd_rental_app import CDLIST


class Clerk(object):
    def record_cd_as_rented(self, cd_id, customer_id):
        cd = CDLIST.get_cd_data(cd_id)
        cd.set_rent(customer_id)