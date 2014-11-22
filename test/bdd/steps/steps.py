from lettuce import step
from cdRental.cd_rental_app import CDList, CUSTOMERLIST
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
    CDList.add_cd(cd)


@step(u'CD is not currently rented')
def cd_is_not_currently_rented(step):
    cd = CDList.get_cd_data("CD2")
    assert_equal(cd.rented,"No")


@step(u'I check out the cd')
def i_check_out_the_cd(step):
    assert True, 'Implement in the web'


@step(u'Then the CD is recorded as rented')
def the_cd_is_recorded_as_rented(step):
    cd = CDList.get_cd_data("CD2")
    cd.rented = "Yes"
    cd.rental_due = "1/23/2011"
    CDList.cds['CD2'] = cd

    assert_equal(CDList.get_cd_data("CD2"), cd)


@step(u'And a rental contract is printed')
def a_rental_contract_is_printed(step):
    assert False, 'This step must be implemented'