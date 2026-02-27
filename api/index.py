from flask import Flask
from mangum import Mangum

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on Vercel!"

handler = Mangum(app)
