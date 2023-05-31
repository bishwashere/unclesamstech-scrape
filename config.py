#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost:3306/deals'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your models here, if needed
# from models import ...

# Register blueprints and configure routes here, if needed
# ...

if __name__ == '__main__':
    app.run()
