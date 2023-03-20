from flask import Flask, render_template
import Sqlite3
from sqlite3 import Error

DATABASE = "C:\Users\19467\OneDrive - Wellington College\Flask\cafe_v5\coffee"
#this is a test comment
app = Flask(__name__)

def create_connection(db_file):
    """
    Create a connection with the database
    parameter: name of the database file
    returns: a connection to the file
    """
    try :
        connection = sqlite3.s=connection(db.file)
        return connection
    except Error as e:
        print(e)
    return none


@app.route('/')
def render_home_page():
    return render_template('home.html')


@app.route('/menu')
def render_menu_page():
    con = create_connection(DATABASE)
    query = "SELECT name, discription, volume, image, price FROM products"
    cur = con()
    cur.excecute(query)
    product_list = cur.fecthall()
    con.close()
    print(product_list)
    return render_template('menu.html', products=product_list)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
#app.run(host='0.0.0.0', debug=True)
