from lettuce import step
from cdRental.cd_rental_app import CDStock, CUSTOMERLIST
from cdRental.customer import Customer
from cdRental.cd import CD
from nose.tools import assert_equal

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
    cd = CDStock.get_cd_data("CD2")
    assert_equal(cd.rented,"No")


@step(u'I check out the cd')
def i_check_out_the_cd(step):
    assert False, 'Implement in the web'


@step(u'Then the CD is recorded as rented')
def then_the_cd_is_recorded_as_rented(step):
    assert False, 'This step must be implemented'


@step(u'And a rental contract is printed')
def and_a_rental_contract_is_printed(step):
    assert False, 'This step must be implemented'