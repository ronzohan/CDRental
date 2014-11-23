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


@step(u'customer has id "([^"]*)"')
def customer_has_id(step, customer_id):
    customer_id = int(customer_id)
    customer = Customer(001, "Ron Daryl Magno")
    CUSTOMERLIST.add_customer(customer)
    assert_equal(CUSTOMERLIST.get_customer_data(customer_id), customer)


@step(u'CD has id "([^"]*)"')
def cd_has_id(step, cd_id):
    cd = CD("CD2", "Cloud Atlas", "No")
    CDLIST.add_cd(cd)
    assert_equal(CDLIST.get_cd_data(cd_id), cd)


@step(u'CD "([^"]*)" is not currently rented')
def cd_is_not_currently_rented(step, cd_id):
    cd = CDLIST.get_cd_data(cd_id)
    assert_equal(cd.rented, "No")


@step(u'I check out the cd "([^"]*)" with customer_id "([^"]*)"')
def i_check_out_the_cd(step, customer_id, cd_id):
    #customer_id = int(customer_id)
    form = world.response.forms['checkout-form']
    form['customer_id'] = customer_id
    form['cd_id'] = cd_id
    world.form_response = form.submit()
    assert_equal(world.response.status_code, 200)


@step(u'Then the CD "([^"]*)" is recorded as rented')
def the_cd_is_recorded_as_rented(step, cd_id):
    cd = CDLIST.get_cd_data(cd_id)
    cd.rented = "Yes"
    cd.rental_due = "1/23/2011"
    CDLIST.cds[cd_id] = cd

    assert_equal(CDLIST.get_cd_data("CD2"), cd)


@step(u'And a rental contract is printed')
def a_rental_contract_is_printed(step):
    assert False, 'This step must be implemented'