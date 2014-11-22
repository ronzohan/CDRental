from flask import Flask, render_template
from cdRental.cd_stock import CDStock

app = Flask(__name__)
CDStock = CDStock()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)