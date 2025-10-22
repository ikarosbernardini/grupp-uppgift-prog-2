
















Instruktioner


----------


Gruppuppgift
I denna uppgift skall ni bygga en lite mer detaljerad app. Ni skall använda minst ett externt API, men
gärna flera i kombination med varandra el. där resultatet av den ena ger information nödvändig för att
hämta den andra.
Applikationen skall ha ett front-end (webb-gränssnitt) och arbeta med en lite större datamängd, så
som statistisk data, eller annan form av register. Nedan är föreslaget Gutendex, vilken innehåller
information om alla böcker i Project Gutenberg (se nedan).
Bygg ett formulär för att kunna påverka sökresultatet på uppslagningen. Det finns 9 st olika parametrar
att påverka. Visa data i strukturerad form, gärna i tabellform med Pandas och kanske skicka någon
Pandas-kolumn till Plotly för att illustrera antal böcker eller annat som kan beräknas i ett diagram.
Visa informationen ni hämtat ur några olika perspektiv, t.ex lista per författare på en sida, medan ni
listar efter boktitlar på en annan. Pandas lämpar sig mycket bra till detta, dvs att ändra ordning på
data.
Applikationen skall spara en Cookie när ni sökt med ert formulär (skickat en request). Innehållet i
denna är lite information (key-value) om den senaste sökningen. När ni sedan öppnar sidan med
formuläret igen läser ni denna cookie och fyller i några av sökfälten med hjälpa av jinja.
Anteckna under tiden ni bygger applikationen med saker ni upptäcker, t.ex problem som uppstått och
hur ni löst dem. Dessa anteckningar kan ni senare använda när ni skall presentera ert projekt under
vecka 45 som en inledning innan ni demonstrerar er applikation. Vi kan alla lära av varandras
erfarenheter, så detta kan bli en lärdom för andra även under presentationerna.
Fundera över test case under tiden ni pratar om lösningar och skriv tester för de funktioner ni
skapar i appen. Tänk därför på att alla funktioner måste returnera något som går att testa 