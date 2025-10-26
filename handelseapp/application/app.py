from flask import Flask, render_template, redirect, url_for
from application import func

app = Flask(__name__)

@app.route("/")
def index():
    """ Omdirigerar till kartvyn."""
    return redirect(url_for("map_view")) 

@app.route("/map")
def map_view():
    """ Visar en karta med händelser."""
    data_url = "https://polisen.se/aktuellt/rss/stockholms-lan/handelser-rss---stockholms-lan/"
    df = func.xml_url_to_dataframe(data_url, xpath="//item") # här hämtar jag datan från RSS-flödet och gör om den till en DataFrame

    if "description" in df.columns: # om description finns i kolumnerna
        df = func.geocode_dataframe(df, location_column="description") # använder description för geokodning
    elif "title" in df.columns: # om title finns i kolumnerna
        df = func.geocode_dataframe(df, location_column="title") # använder title som fallback
    else:
        return "Ingen platsinformation hittades", 500 # felhantering om ingen platsinfo finns

    events = df.to_dict(orient="records") # här gör jag om DataFrame till en lista av ordböcker
    return render_template("map.html", events=events)

@app.route("/table")
def table_view():
    """ Visar en tabell med händelser."""
    data_url = "https://polisen.se/aktuellt/rss/stockholms-lan/handelser-rss---stockholms-lan/" # här definierar jag URL:en till RSS-flödet
    df = func.xml_url_to_dataframe(data_url, xpath="//item") # här hämtar jag datan från RSS-flödet och gör om den till en DataFrame
    table_html = df.to_html(classes="table table-striped", justify="left") # här gör jag om tabellen till HTML
    return f"<h1>Aktuella händelser i Stockholm</h1>{table_html}"  # returnerar HTML-sidan med tabellen

@app.route("/map/test")
def test_map():
    """ Testvy för kartan med hårdkodade händelser
        där jag använder mig utav "title" och "description" som platsinformation,
        och kan enkelt välja ut vilka latitud och longitud värden jag vill använda mig av för att visa på kartan."""
    events = [
        {"title": "Här är faktiskt vår skola", "description": "Nackademin", "lat": 59.34527896351938, "lon": 18.023387442913386},
        {"title": "Hemma hos mej", "description": "Vega", "lat": 59.17901498967768, "lon": 18.1283693503939926},
    ]
    return render_template("map.html", events=events) # renderar mallen med händelserna

if __name__ == "__main__": # kör appen om detta är huvudmodulen
    app.run(debug=True)

