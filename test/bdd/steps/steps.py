from lettuce import step, world
from nose.tools import assert_equal,assert_in
from webtest import TestApp
from cdRental.models import db, CD, Customer, CDRentals
from cdRental.cd_rental_app import app
import datetime
from flask.globals import session


def setupDB():
    db.drop_all()
    db.create_all()
    customer1 = Customer('Ron Magno')
    cd = CD('Beatles Greatest Hits', rental_period=2)

    db.session.add(cd)
    db.session.add(customer1)
    db.session.commit()

@step(u'Customer "([^"]*)" with ID "([^"]*)"')
def given_customer_group1_with_id_group2(self, customer_name, customer_id):
    setupDB()

    cust = Customer.query.filter(Customer.name=="Ron Magno").first()
    customer_id = int(customer_id)

    assert_equal(cust.name, customer_name)
    assert_equal(cust.id, customer_id)

@step(u'CD with ID "([^"]*)", title "([^"]*)", has a rental period of "([^"]*)" days and is not currently rented')
def cd_with_id_group1_title_group2_has_a_rental_period_of_group3_days_and_isnot_currently_rented(step,
        cd_id, cd_title, cd_rental_period):

    cd = CD.query.filter(CD.id == cd_id, CD.title == cd_title, \
        CD.rental_period == cd_rental_period, CD.rented == "No").first()


    assert_equal(cd.title, cd_title)
    assert_equal(cd.id, int(cd_id))


@step(u'the clerk checks out the CD with ID "([^"]*)" to customer with ID "([^"]*)" on "([^"]*)"')
def the_clerk_checks_out_the_cd_with_id_group1_to_customer_with_id_group2_on_group3(step, 
    cd_id, customer_id, date):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    form = world.response.forms['checkout-form']

    form['cd_id'] = cd_id
    form['customer_id'] = customer_id
    world.form_response = form.submit()

    assert_equal(world.form_response.status_code, 200)


@step(u'CD with ID "([^"]*)" is recorded as rented with customer ID "([^"]*)"')
def cd_with_id_group1_is_recorded_as_rented_with_customer_idd_group2(step,
                                                                     cd_id, customer_id):
    results = (db.session.query(CD.id, CD.title, CD.rented, CDRentals.customer_id,
                                CDRentals.rental_due).join(CD.cdrental)).first()

    assert_equal(results.id, int(cd_id))
    assert_equal(results.rented, 'Yes')
    assert_equal(results.customer_id, int(customer_id))

@step(u'rental contract printed with customer ID "([^"]*)", customer name "([^"]*)", CD ID "([^"]*)", CD title "([^"]*)", and rental due on "([^"]*)"')
def and_rental_contract_printed_with_customer_id_group1_customer_name_group2_cd_id_group3_cd_title_group4_and_rental_due_on_group5(step, 
    customer_id, customer_name, cd_id, cd_title, rental_due):

    rental_contract = generate_rental_contract(cd_id)

    assert_equal(rental_contract['CustomerID'], customer_id)
    assert_equal(rental_contract['CustomerName'], customer_name)
    rental_due = datetime.date.today() + \
        datetime.timedelta(days=2)
    rental_due = rental_due.strftime("%m/%d/%Y")

    assert_equal(rental_contract['RentalDue'], rental_due)