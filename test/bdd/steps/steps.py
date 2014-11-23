from lettuce import step, world
from cdRental.cd_rental_app import CDLIST, CUSTOMERLIST, app
from cdRental.customer import Customer
from cdRental.cd import CD
from nose.tools import assert_equal
from webtest import TestApp

