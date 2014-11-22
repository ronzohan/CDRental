from lettuce import step
from cdRental.cd_rental_app import CDStock, CUSTOMERLIST
from cdRental.customer import Customer
from cdRental.cd import CD


@step(u'customer has id')
def customer_has_id(step):
    customer = Customer(001, "Ron Daryl Magno")
    CUSTOMERLIST.add_customer(customer)


@step(u'CD has id')
def cd_has_id(step):
    cd = CD("CD2", "Cloud Atlas", "No")
    CDStock.add_cd(cd)


@step(u'CD is not currently rented')
def cd_is_not_currently_rented(step):
    assert False, 'This step must be implemented'


@step(u'I check out the cd')
def i_check_out_the_cd(step):
    assert False, 'This step must be implemented'


@step(u'the CD is recorded as rented and a rental contract is printed')
def the_cd_is_recorded_as_rented_and_a_rental_contract_is_printed(step):
    assert False, 'This step must be implemented'
