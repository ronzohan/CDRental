from flask import Flask, render_template, request
from models import Customer, CD, CDRentals, db
import datetime


app = Flask(__name__)


@app.route('/')
def index():
    cd_id = request.args.get('cd_id')
    customer_id = request.args.get('customer_id')

    if customer_id != "":
        try:
            customer_id = int(customer_id)
        except:
            pass

    cd = CD.query.filter(CD.id == cd_id).first()
    customer = Customer.query.filter(Customer.id == customer_id).first()

    if customer is None:
        return render_template('index.html', 
                               rental_contract={'Error': 'Customer Not Found'})
    elif cd is None or cd.rented == "Yes":
        return render_template('index.html', 
                               rental_contract={'Error': 'CD is not found or rented'})
    else:
        cdrental = CDRentals(cd_id, customer_id)
        return render_template('index.html', 
                               rental_contract=cdrental.print_contract())


if __name__ == "__main__":
    app.run(debug=True)
