import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from faker import Faker
import random

from app import app, db
from models import Customer, Book, Transaction

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def add_3_users():
    fake = Faker("pt_BR")
    for x in range(3):
        customer_name = fake.name()
        customer=Customer(
            name = customer_name,
            email = fake.email(),
            address = fake.street_address(),
            phone =  fake.phone_number(),
            city = fake.city(),
            state = fake.estado_sigla(),
            zipcode = fake.postcode()
        )
        print("Customer "+customer_name+" created.")
        db.session.add(customer)
    db.session.commit()
    return "3 users added."

@manager.command
def add_5_books():
    fake = Faker("pt_BR")
    for x in range(5):
        book_name = fake.catch_phrase()
        book=Book(
            book_name = book_name,
            author_name = fake.name(),
            publisher = fake.domain_word(),
            customer_review =  random.randint(0, 5)
        )
        print("Book "+book_name+" created.")
        db.session.add(book)
    db.session.commit()
    return "5 books added."

@manager.command
def add_3_transactions():
    fake = Faker("pt_BR")
    customers=Customer.query.all()
    books=Book.query.all()
    for x in range(1,4):
        books_list = books
        transaction=Transaction(
            customer_id = random.choice(customers).id,
            status = "completed",
        )
        if(x == 1 and len(books) > 0):
            transaction.books.append(random.choice(books_list))
        elif(x == 2 and len(books) > 1):
            random_book = random.choice(books_list)
            transaction.books.append(random_book)
            books_list.remove(random_book)
            random_book = random.choice(books_list)
            transaction.books.append(random_book)
            transaction.status = "in progress"
        elif(x == 3 and len(books) > 2):
            random_book = random.choice(books_list)
            transaction.books.append(random_book)
            books_list.remove(random_book)
            random_book = random.choice(books_list)
            transaction.books.append(random_book)
            books_list.remove(random_book)
            random_book = random.choice(books_list)
            transaction.books.append(random_book)
            transaction.status = "cancelled"
        else:
            return str(len(books))
        db.session.add(transaction)
    db.session.commit()
    return "3 transactions added."


if __name__ == '__main__':
    manager.run()