import secrets
from flask import Flask, request, render_template
import MySQLdb
import os
from dotenv import load_dotenv

load_dotenv("secrets.env")

HOST = os.getenv("HOST")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

conn = MySQLdb.connect(HOST, USERNAME, PASSWORD, "warehouse")
cursor = conn.cursor()
app = Flask(__name__)

@app.route('/')
def main():
    cursor.execute("SELECT * from shipments")
    data = cursor.fetchall()
    return render_template('index.html', value=data)

