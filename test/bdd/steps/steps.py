from lettuce import step, world
from cdRental.cd_rental_app import CDLIST, CUSTOMERLIST, app
from cdRental.customer import Customer
from cdRental.cd import CD
from nose.tools import assert_equal
from webtest import TestApp


@step(u'Customer "([^"]*)" with ID "([^"]*)"')
def given_customer_group1_with_id_group2(self, customer_name, customer_id):
    customer = Customer(customer_id, customer_name)
    CUSTOMERLIST.add_customer(customer)

    assert_equal(CUSTOMERLIST.get_customer_data(customer_id), customer)


@step(u'CD with ID "([^"]*)", title "([^"]*)", has a rental period of "([^"]*)" days and isnot currently rented')
def cd_with_id_group1_title_group2_has_a_rental_period_of_group3_days_and_isnot_currently_rented(step, 
    cd_id, cd_title, cd_rental_period):

    cd = CD(cd_id, cd_title, "No", rental_period=cd_rental_period)
    CDLIST.add_cd(cd)

    assert_equal(CDLIST.get_cd_data(cd_id), cd)


@step(u'the clerk checks out the CD with ID "([^"]*)" to customer with ID "([^"]*)" on "([^"]*)"')
def the_clerk_checks_out_the_cd_with_id_group1_to_customer_with_id_group2_on_group3(step, 
    cd_id, customer_id, date):

    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')

    assert_equal(world.response.status_code, 200)

    form = world.response.forms['checkout-form']
    form['cd_id'] = cd_id
    form['customer_id'] = customer_id
    world.form_response = form.submit()

    assert_equal(world.form_response.status_code, 200)


@step(u'CD with ID "([^"]*)" is recorded as rented')
def cd_with_id_group1_is_recorded_as_rented(step, cd_id):
    cd = CDLIST.get_cd_data(cd_id)
    cd.set_rent()
    CDLIST.cds[cd_id] = cd

    assert_equal(CDLIST.get_cd_data(cd_id), cd)
    assert_equal(CDLIST.get_cd_data(cd_id).rental_due, cd.rental_due)


@step(u'And rental contract printed with customer ID "([^"]*)", customer name "([^"]*)", CD ID "([^"]*)", CD title "([^"]*)", and rental due on "([^"]*)"')
def and_rental_contract_printed_with_customer_id_group1_customer_name_group2_cd_id_group3_cd_title_group4_and_rental_due_on_group5(step, 
    customer_id, customer_name, cd_id, cd_title, cd_rental_due):

    customer = CUSTOMERLIST.get_customer_data(customer_id)
    cd = CDLIST.get_cd_data(cd_id)
    