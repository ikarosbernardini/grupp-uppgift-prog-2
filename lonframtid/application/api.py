from flask import Flask, request, render_template
import pandas as pd
import requests
import json
from application import func

app = Flask(__name__)

@app.route("/skatteverket", methods=["GET"])
def skatteverk():
    content = requests.get("https://skatteverket.entryscape.net/rowstore/dataset/1cad9af9-6c1e-4518-a610-c16302dd3b72/json?gruppering=Bransch&_limit=500&_offset=0")
    data = content.json()["results"][0]
    

    df = pd.DataFrame.from_dict(data, orient='index').reset_index()
    df.columns = ['Bransch'] + list(df.columns[1:])
    data = df.to_dict(orient='records')

    print(data)
    return render_template('index.html', data=data)
@app.route("/arbetsformedlingen", methods=["GET"])
def arbetsformedlingen():
    data_url = "https://historical.api.jobtechdev.se/ad/8430129"
    response = requests.get(data_url)
    data = response.json()
    return render_template('index.html', data=data)

