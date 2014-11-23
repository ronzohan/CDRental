from flask import Flask, render_template
from cd_list import CDList
from customer_list import CustomerList


app = Flask(__name__)
CDLIST = CDList()
CUSTOMERLIST = CustomerList()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
