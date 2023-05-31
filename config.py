from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/deals?unix_socket=C:/xampp/mysql/mysql.sock'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your models here, if needed
# from models import ...


def create_database():
    try:
        # Create a database engine and session
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create the database using a transaction
        session.execute("CREATE DATABASE IF NOT EXISTS deals")
        session.commit()
        session.close()

    except OperationalError:
        print('Error occurred while creating the database.')


def create_table():
    try:
        # Create all tables using migrations
        with app.app_context():
            db.create_all()

    except OperationalError:
        print('Error occurred while creating the table.')


if __name__ == '__main__':
    create_database()
    create_table()
    app.run()
