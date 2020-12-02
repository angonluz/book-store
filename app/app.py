from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Customer

@app.route('/')
def hello():
    return "Welcome to Eldorado's book store"

@app.route("/customers/",methods=['GET'])
def get_all_customers():
    try:
        customers=Customer.query.all()
        return  jsonify([e.serialize() for e in customers])
    except Exception as e:
	    return(str(e))

@app.route("/customers/",methods=['POST'])
def add_customer():
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    phone = request.form.get('phone')
    phone = request.form.get('phone')
    city = request.form.get('city')
    state = request.form.get('state')
    zipcode = request.form.get('zipcode')
    try:
        customer=Customer(
            name = name,
            email = email,
            address = address,
            phone = phone,
            city = city,
            state = state,
            zipcode = zipcode
        )
        db.session.add(customer)
        db.session.commit()
        return "Customer added. customer id={}".format(customer.id)
    except Exception as e:
	    return(str(e))

@app.route("/customers/<id_>/")
def get_by_id(id_):
    try:
        customer=Customer.query.filter_by(id=id_).first()
        return jsonify(customer.serialize())
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run()