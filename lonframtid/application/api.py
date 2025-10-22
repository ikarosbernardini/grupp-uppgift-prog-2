from flask import Flask, request, render_template
import pandas as pd
import requests
import json
from application import func

app = Flask(__name__)

@app.route("/skatteverket", methods=["GET"])
def skatteverk():
    '''Denna funktion körs när man går till servern med  endpoint '/api/xml'. 
       Den tar endast emot trafik med alla HTTP methods.
       Den gör samma sak som funktionen ovan (api_post()) men med XML istället för JSON.'''

    # I det här exemplet har vi inga argument att lägga in i API:ets URL, så vi använder en vanlig sträng.
    # XPath är ett sätt att navigera i XML. Raden nedan väljer ut alla taggar med namn <item>
    data_url = "https://skatteverket.entryscape.net/rowstore/dataset/1cad9af9-6c1e-4518-a610-c16302dd3b72"
    data = func.xml_url_to_html_table(data_url, xpath="//item")

    # Skicka tillbaka resultatet till browsern med Jinja, dvs uppdatera mallen index.html med innehållet i variabeln data
    return render_template('index.html', data=data)
@app.route("/arbetsformedlingen", methods=["GET"])
def arbetsformedlingen():
    data_url = "https://historical.api.jobtechdev.se/ad/8430129"
    response = requests.get(data_url)
    data = response.json()
    return render_template('index.html', data=data)

