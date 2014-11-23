from flask import Flask, render_template, request
from cd_list import CDList
from customer_list import CustomerList
from clerk import Clerk


app = Flask(__name__)
CDLIST = CDList()
CUSTOMERLIST = CustomerList()


@app.route('/')
def index():
    cd_id = request.args.get('cd_id')
    customer_id = request.args.get('customer_id')
    clerk = Clerk()
    clerk.record_cd_as_rented(cd_id, customer_id)
    rental_contract = clerk.generate_rental_contract(cd_id)

    return render_template('index.html', rental_contract)


if __name__ == "__main__":
    app.run(debug=True)
