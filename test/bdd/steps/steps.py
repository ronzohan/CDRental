from lettuce import step, world
from cdRental.cd_rental_app import CDLIST, CUSTOMERLIST, app
from cdRental.customer import Customer
from cdRental.cd import CD
from nose.tools import assert_equal
from webtest import TestApp


@step(u'I visit the homepage')
def i_visit_the_homepage(step):
    world.browser = TestApp(app)
    world.response = world.browser.get("http://localhost:5000")
    assert_equal(world.response.status_code, 200)


@step(u'customer has id')
def customer_has_id(step):
    customer = Customer(001, "Ron Daryl Magno")
    CUSTOMERLIST.add_customer(customer) 


@step(u'CD has id')
def cd_has_id(step):
    cd = CD("CD2", "Cloud Atlas", "No")
    CDLIST.add_cd(cd)


@step(u'CD is not currently rented')
def cd_is_not_currently_rented(step):
    cd = CDLIST.get_cd_data("CD2")
    assert_equal(cd.rented,"No")


@step(u'I check out the cd')
def i_check_out_the_cd(step):
    assert True, 'Implement in the web'


@step(u'Then the CD is recorded as rented')
def the_cd_is_recorded_as_rented(step):
    cd = CDLIST.get_cd_data("CD2")
    cd.rented = "Yes"
    cd.rental_due = "1/23/2011"
    CDLIST.cds['CD2'] = cd

    assert_equal(CDLIST.get_cd_data("CD2"), cd)


@step(u'And a rental contract is printed')
def a_rental_contract_is_printed(step):
    assert False, 'This step must be implemented'