from flask import Flask, request, render_template, url_for, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'  # You can use any random string


class ContactDB:
    def __init__(self, db_name='contact.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    category TEXT NOT NULL,
                    message TEXT NOT NULL
                )
            ''')

    def save_message(self, name, email, category, message):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''
                INSERT INTO messages (name, email, category, message)
                VALUES (?, ?, ?, ?)
            ''', (name, email, category, message))

db = ContactDB()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        category = request.form['category']
        message = request.form['message']

        db.save_message(name, email, category, message)
        flash('Your message has been sent!')

    return render_template('index.html', title='Home')




if __name__ == '__main__':
    app.run(debug=True)