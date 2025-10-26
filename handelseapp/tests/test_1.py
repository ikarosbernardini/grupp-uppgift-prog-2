from flask import Flask, render_template, redirect, url_for   
from application import func

app = Flask(__name__)


@app.route("/map/test")
def test_map():

    events = [
        {"title": "Här är faktiskt vår skola", "description": "Nackademin", "lat": 59.34527896351938, "lon": 18.023387442913386},
        {"title": "Hemma hos mej", "description": "Vega", "lat": 59.17901498967768, "lon": 18.1283693503939926},
    ]
    return render_template("map.html", events=events) # renderar mallen med händelserna