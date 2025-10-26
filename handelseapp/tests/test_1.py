from flask import Flask, render_template, redirect, url_for   
from application import func

app = Flask(__name__)


@app.route("/map/test")
def test_map():
    events = [
        {"title": "TestHändelse 1", "description": "Nackademin", "lat": 59.3496, "lon": 18.0069},
        {"title": "TestHändelse 2", "description": "Vega", "lat": 59.193054, "lon": 18.339186},
    ]
    return render_template("map.html", events=events)