from app import db


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    zipcode = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id' : self.id, 
            'name' : self.name,
            'email' : self.email,
            'address' : self.address,
            'phone' : self.phone,
            'city' : self.city,
            'state' : self.state,
            'zipcode' : self.zipcode
        }

book_transaction = db.Table('BookTransaction',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), nullable=False),
    db.Column('transaction_id', db.Integer, db.ForeignKey('transactions.id'), nullable=False))

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(), nullable=False)
    author_name = db.Column(db.String(), nullable=False)
    publisher = db.Column(db.String(), nullable=False)
    customer_review = db.Column(db.Integer, nullable=False)
    transactions = db.relationship('Transaction', secondary=book_transaction)

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id' : self.id, 
            'book_name' : self.book_name,
            'author_name' : self.author_name,
            'publisher' : self.publisher,
            'customer_review' : self.customer_review,
        }

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    status = db.Column(db.String(), nullable=False, default="in progress")
    books = db.relationship('Book', secondary=book_transaction)

    def __repr__(self):
        return '<id {}>'.format(self.id)

