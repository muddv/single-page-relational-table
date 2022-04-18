from crypt import methods
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

CRITERIA = [
    "shipment_date",
    "item",
    "amount",
    "shipment_distance"
]

#maybe this can be passed to another conditional and names can be made more human readable
CONDITIONS = [
    "=",
    ">",
    "<",
    "LIKE",
]

@app.route("/", methods=["GET", "POST"])
def main():
    column = request.form.get("column")
    condition = request.form.get("condition")
    query = request.form.get("query")
    cursor.execute("SELECT * FROM shipments") 
    if request.method == "POST":
        if column == None or condition == None or query == None:
            cursor.execute("SELECT * FROM shipments") 
        else:
            if isinstance(query, str):
                sql = f"SELECT * FROM shipments WHERE {column} {condition} '%{query}%'"
                cursor.execute(sql)
            else:
                sql = f"SELECT * FROM shipments WHERE {column} {condition} {query}"
                cursor.execute(sql)
            #cursor.execute("SELECT * FROM shipments WHERE %(column)s %(condition)s %(query)s", {'column': column, 'condition': condition, 'query': query});
    data = cursor.fetchall()
    return render_template('index.html', data = data, criteria = CRITERIA, conditions = CONDITIONS)

