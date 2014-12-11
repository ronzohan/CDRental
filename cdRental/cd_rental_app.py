from flask import Flask, render_template, request
from cd import CD
from customer import Customer
from cd_list import CDList
from customer_list import CustomerList


app = Flask(__name__)
CDLIST = CDList()
CUSTOMERLIST = CustomerList()


@app.route('/')
def index():
    cd_id = request.args.get('cd_id')
    customer_id = request.args.get('customer_id')

    if customer_id != "":
        try:
            customer_id = int(customer_id)
        except:
            pass

    cd = CDLIST.get_cd_data(cd_id)
    customer = CUSTOMERLIST.get_customer_data(customer_id)

    if customer is None:
        return render_template('index.html', rental_contract={'Error': 'Customer Not Found'})
    elif cd is None or cd.rented == "Yes":
        return render_template('index.html', rental_contract={'Error': 'CD is not found or rented'})
    else:
        record_cd_as_rented(cd_id, customer_id)
        rental_contract = generate_rental_contract(cd_id)
        return render_template('index.html', rental_contract=rental_contract)


def record_cd_as_rented(cd_id, customer_id):
        cd = CDLIST.get_cd_data(cd_id)
        cd.set_rent(customer_id)


def generate_rental_contract(cd_id):
    cd = CDLIST.get_cd_data(cd_id)
    customer = CUSTOMERLIST.get_customer_data(cd.customer_id)
    rental_contract = {'CustomerID': customer.id,
                           'CustomerName': customer.name,
                           'CDID': cd.id,
                           'CDTitle': cd.title,
                           'RentalDue': cd.rental_due}
    return rental_contract

if __name__ == "__main__":
    cd = CD("CD2", "Cloud Atlas", "No", rental_period=2)
    CDLIST.add_cd(cd)
    customer = Customer("001", "Ron")
    CUSTOMERLIST.add_customer(customer)
    app.run(debug=True)
