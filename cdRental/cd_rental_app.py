from flask import Flask, render_template
from cdRental.cd_list import CDList
from cdRental.customer_list import CustomerList


app = Flask(__name__)
CDList = CDList()
CUSTOMERLIST = CustomerList()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
