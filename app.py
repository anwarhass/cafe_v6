from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = "C:/Users/19467/PycharmProjects/flaskProject/coffee_db"
#this is a test comment
app = Flask(__name__)

def create_connection(db_file):
    """
    Create a connection with the database
    parameter: name of the database file
    returns: a connection to the file
    """
    try:
        connection = sqlite3.Connection(db_file)
        return connection
    except Error as e:
        print(e)
    return None


@app.route('/')
def render_home_page():
    return render_template('home.html')


@app.route('/menu')
def render_menu_page():
    con = create_connection(DATABASE)
    query = "SELECT name, description, volume, image, price FROM products"
    cur = con.cursor()
    cur.execute(query)
    product_list = cur.fetchall()
    con.close()
    print(product_list)
    return render_template('menu.html', products=product_list)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
#app.run(host='0.0.0.0', debug=True)
