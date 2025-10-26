from urllib import request
import ssl
import json
import pandas as pd
import requests
import time


_cache = {} # cache för att slippa upprepade geokodningsförfrågningar


def json_url_to_html_table(url, columns=None): 
    """
    Hämtar JSON format och returnerar en HTML-tabell (via Pandas).
    """
    try:
        raw = request.urlopen(url, context=ssl._create_unverified_context()).read() # Hämta rådata från URL:en
        data = json.loads(raw) # Ladda JSON-datan
        df = pd.DataFrame(data) # Gör om till DataFrame
        return df.to_html(columns=columns, classes="table p-5", justify="left") # Gör om till HTML-tabell
    except Exception as e:
        print("Fel vid hämtning av JSON formatet:", e) # Felhantering
        return "<p>Kunde inte hämta datan korrekt.</p>"

def xml_url_to_dataframe(data_url, xpath="//item"):
    """
    Hämtar XML-data och gör om till en DataFrame med hjälp av Pandas.
    """
    try: 
        raw = request.urlopen(data_url, context=ssl._create_unverified_context()).read() # Hämta rådata från URL:en
        return pd.read_xml(raw, xpath=xpath) # Gör om till DataFrame
    except Exception as e:
        print("Fel vid hämtning/parsing av XML:", e) # Felhantering
        return pd.DataFrame()
    
def geocode_dataframe(df, columns="description"):
    """
    Geokodar en DataFrame med hjälp av Nonimatim (OpenStreetMap) API:n.
    """
    lat_list, lon_list = [], [] # listor för latitud och longitud
    for address in df[columns]: # går igenom varje adress i den angivna kolumnen
        if pd.isna(address):
            lat_list.append(None); lon_list.append(None) 
            continue

        if address in _cache: # kolla om adressen finns i cache
            lat, lon = _cache[address] # hämta lat/lon från cache
        else: 
            try:
                url = "https://nominatim.openstreetmap.org/search" # Nominatim API-endpointen
                query = {"q": address, "format": "json", "limit": 1} # parametrar för förfrågan, alltså vad vi söker efter i API:n
                r = requests.get(url, params=query, headers={"User-Agent": "FlaskApp"}) # skickar en GET-förfrågan
                data = r.json() # hämtar JSON-svaret
                if data: # om data finns
                    lat = float(data[0]["lat"])
                    lon = float(data[0]["lon"])
                    _cache[address] = (lat, lon) # spara i cache
                else:
                    lat, lon = None, None # om ingen data hittas så sätts lat/lon till None
            except Exception: # Felhantering
                lat, lon = None, None
                time.sleep(1)  # Vänta en sekund vid fel för att undvika överbelastning av API:n

        lat_list.append(lat) # lägg till latitud i listan
        lon_list.append(lon) # lägg till longitud i listan

        df["latitude"] = lat_list # lägg till latitud-kolumn i DataFrame
        df["longitude"] = lon_list # lägg till longitud-kolumn i DataFrame
    return df # returnera den uppdaterade DataFrame:n
            