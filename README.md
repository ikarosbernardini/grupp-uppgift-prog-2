*Grupp uppgift*

**Händelse App**

En webbapplikation byggd i Flask som hämtar aktuella händelser från polisens RSS-flöde, geokodar adresser och visar dem på en interaktiv karta med Leaflet. Projektet började som en löneprognos-app men omstrukturerades till att fokusera på polishändelser.


***Instruktioner***

För att köra projektet lokalt behöver du först klona repot och gå in i projektmappen:

git clone <repo-url> 

cd handelseapp


Skapa sedan en virtuell miljö och aktivera den:

python3 -m venv venv 

source venv/bin/activate # Linux/Mac venv\Scripts\activate # Windows


Installera alla beroenden från `requirements.txt`:

pip install -r requirements.txt



Gå därefter in i `application`-mappen och starta appen:

cd application 

flask --app app run


Öppna sedan i webbläsaren:

http://127.0.0.1:5000



***Funktioner***

- Hämtar händelser från polisens RSS
- Geokodar adresser med Nominatim
- Visar händelser på karta och i tabell
- Testläge med hårdkodade exempel


***Källor och API:er***

- Kart api : https://leafletjs.com/ och https://nominatim.openstreetmap.org/ui/search.html  
- Polisens händelse api : https://polisen.se/aktuellt/rss/stockholms-lan/handelser-rss---stockholms-lan/  
- Geolocation HTML : https://www.w3schools.com/html/html5_geolocation.asp  
- HTML strukturering : https://getbootstrap.com/  
- Jinja strukturering : https://jinja.palletsprojects.com/en/stable/templates/  
- Flask quickstart : https://flask.palletsprojects.com/en/stable/quickstart/  

För renskrivning och små förbättringsförslag etc har vi använt oss utav följande AI-modeller :  
- Copilot  
- ChatGPT  
- Ollamas - qwen3-coder:480b-cloud, qwen3-coder:30b  

Vi har även använt oss av Google Maps för att få exakta koordinater på latitud och longitud.



***Logg-bok***

- 2025-10-20(Lektion 6):
Vi skapade ett github repo och satte upp miljön så vi kan börja arbeta.
sedan bestämde vi oss för vad vi skulle skapa för projekt.

Vi valde ett projekt där vi skulle förutspå löne-ökningarna på specfika arbeten med hjälp av skatteverkets löne API och arbetsförmedlingens jobbannons API


- 2025-10-21:


Vi mötes upp och fixa miljöerna för gruppmedlemmarna och började jobba på varsin github "branch"


- 2025-10-22:

Projektet var lite stillastående.


- 2025-10-23(Lektion 7): 


Vi fick ihop en del HTML för visuallisering och började få upp tabeller.


- 2025-10-24 - 2025-10-26:

Vi valde att omstrukturera hela projektet och byta API:er helt och hållet till att istället använda oss utav polisens rss fil med aktuella händelser och sedan nyttja ett kart API som heter Leafletjs som ger oss möjlighet att ha en interaktiv karta som vi tänkt "pin pointa" de olika händelserna från polisens data.

Vi valde även att göra om de mesta och ändå kommit en bit på projektet och fått fram test varianter på vårat projekt.  

Vi har även listat vilka olika funktioner vi vill lägga till och vad vi behöver vidareutveckla, samt fördelat de olika uppgifterna i gruppen. 



- 2025-10-27(Lektion 8)
Vi började stukturera flask appen så att vi äntligen kunde få något visuellt men var fortfarande inte riktigt där, då vi fortfarande inte kunde få kartnålarna att gå i sync med riktiga live händelser.


- 2025-10-29(Lektion 9)

Efter himla många om och om med lite tricks och knep från Dennis lyckades Ikaros och han få  live händelserna gå i sync med kartnålarna och vi hade en bra grund på de hela. Vi byggde även vidare på hemsidan för utseendemässiga aspekter.


- 2025-10-31(Inlämningsdag)

Vi ordna en bra design på hemsidan mycket hjälp av bootstrap och våran kompis "Bengan" som vi kallar han och andra kanske referar till AI. 
Sedan implemnterade vi in en sök funktion och en "tillbaka funktion", vi löste även cookie lösning som sparar dina senaste sökningar upp till ett dygn. 

Vi gjorde 5 olika test cases varav 2 var för att testa cookie funktionen och 2 var för att testa om sidan var online samt om erorr handlern 404 fungerade som tänkt, sista var för att säkerställa att .json filen öppnades och gick att öppna från alla datorer oavsett filsökvägar.

Ikaros redigerande även Polis logan så de blev transparent och passade snyggt in på hemsidan samt själva "faviconen", vi började sedan dokumentera koden så gott de gick och vad tiden erbjöd.

Testade koden med pytest på de test vi gjort och lyckades bli godkända!

pushade upp all koden och städade undan lite i filerna för att skapa en snygg filstruktur och enkel att navigera sig runt på våran GitHub reposeratory.

Fixade denna README.md fil med alla loggar för vårat arbete samt la till en "Instruktion" flik så man vet hur man ska köra själva skripetet.









