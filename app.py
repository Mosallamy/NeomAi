from flask import Flask, render_template, jsonify,url_for
from datetime import datetime
import pandas as pd
import os
import csv

app = Flask(__name__)

@app.template_filter("date")
def date(dateInSecodns):
    dateInSecodns = int(dateInSecodns)
    return datetime.utcfromtimestamp(dateInSecodns).strftime('%Y-%m-%d %H:%M:%S')

@app.route("/")
def train():
    predictions = list()
    with open("Predections.csv", "r") as file:
        reader = csv.DictReader(file)
        predictions = list(reader)

    return render_template("index.html", predictions = predictions[:10])

if __name__ == "__main__":
    app.run(debug=True)
