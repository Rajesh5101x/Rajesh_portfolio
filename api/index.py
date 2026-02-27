from flask import Flask, request, render_template, flash
import sqlite3
from mangum import Mangum

app = Flask(__name__)
app.secret_key = 'secret_key'

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

    return "Flask running on Vercel"

# THIS LINE IS CRITICAL
handler = Mangum(app)
