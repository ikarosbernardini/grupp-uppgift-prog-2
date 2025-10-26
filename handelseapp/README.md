###Grupp uppgift

###Händelse App###

En webbapplikation byggd i Flask som hämtar aktuella händelser från polisens RSS-flöde, geokodar adresser och visar dem på en interaktiv karta med Leaflet. Projektet började som en löneprognos-app men omstrukturerades till att fokusera på polishändelser.


###Funktioner

- Hämtar händelser från polisens RSS
- Geokodar adresser med Nominatim
- Visar händelser på karta och i tabell
- Testläge med hårdkodade exempel




***Källor och API:er***

kart api : https://leafletjs.com/ och https://nominatim.openstreetmap.org/ui/search.html
polisens händelse api : https://polisen.se/aktuellt/rss/stockholms-lan/handelser-rss---stockholms-lan/

HTML strukturering : https://getbootstrap.com/
Jinja strukturering : https://jinja.palletsprojects.com/en/stable/templates/
Flask quickstart : https://flask.palletsprojects.com/en/stable/quickstart/

Vi har även använt oss av Google Maps för att få exakta koordinater på latitud och longitud.






***Logg-bok***

- 2025-10-20(Lektion 6):
Vi skapade ett github repo och satte upp miljön så vi kan börja arbeta.
sedan bestämde vi oss för vad vi skulle skapa för projekt.

Vi valde ett projekt där vi skulle förutspå löne-ökningarna på specfika arbeten med hjälp av skatteverkets löne API och arbetsförmedlingens jobbannons API


- 2025-10-21:


Vi mötes upp och fixa miljöerna för gruppmedlemmarna och började jobba på varsin github "branch"


- 2025-10-22:

Projektet vart lite stilla stående.


- 2025-10-23(Lektion 7): 


Vi fick ihop en del HTML för visuallisering och började få upp tabeller.


- 2025-10-24 - 2025-10-26:

Vi valde att omstrukturera hela projektet och byta API:er helt och hållet till att istället använda oss utav polisens rss fil med aktuella händelser och sedan nyttja ett kart API som heter Leafletjs som ger oss möjlighet att ha en interaktiv karta som vi tänkt "pin pointa" de olika händelserna från polisens data.

Vi valde även att göra om de mesta och ändå kommit en bit på projektet och fått fram test varianter på vårat projekt.  

Vi har även listat vilka olika funktioner vi vill lägga till och vad vi behöver vidareutveckla, samt fördelat de olika uppgifterna i gruppen. 



- 2025-10-27(Lektion 8)










