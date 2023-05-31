from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


import mysql.connector

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    #password='password'
)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Execute the raw SQL command to create a database
database_name = 'deals'
create_database_command = f'CREATE DATABASE {database_name}'
try:
    cursor.execute(create_database_command)
except:
    print('Database ALready Exists')
# Close the cursor and the connection
cursor.close()
connection.close()

# Establish a connection to the MySQL server again
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    #password='password',
    database='deals'  # Specify the database you created
)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Execute the raw SQL command to create the "deal" table
create_table_command = """
CREATE TABLE deal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price VARCHAR(20) NOT NULL,
    discount VARCHAR(20) NOT NULL
)
"""
try:
    cursor.execute(create_table_command)
    connection.commit()
except:
    print('error while creating table, table exists or other problem [Line 53 Config.py]')

cursor.close()
connection.close()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/deals?unix_socket=C:/xampp/mysql/mysql.sock'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your models here, if needed
# from models import ...

# Register blueprints and configure routes here, if needed
# ...

if __name__ == '__main__':
    app.run()

