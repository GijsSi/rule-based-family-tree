# Familieboom Programma

## Overzicht
In dit programma maak ik gebruik van Python en de Experta-library om een eenvoudige familieboom te creëren. Ik definieer relaties zoals vader, moeder, broer, zus, oom en tante, en toon hoe deze familieleden aan elkaar gerelateerd zijn. Ik heb dit programma moeten maken voor een practicum van het vak Intelligent Systems bij de Hogeschool van Amsterdam

## Belangrijk
Het is essentieel om Python 3.7 te gebruiken voor dit programma vanwege compatibiliteitsredenen met de Experta-bibliotheek.

## Installatie
Voordat je begint, zorg ervoor dat Python 3.7 geïnstalleerd is op je computer. De Experta-bibliotheek is vereist en kan geïnstalleerd worden met pip:

```bash
pip install experta
```

## Opdracht

Maak een voorbeeld systeem met (bijvoorbeeld!) je eigen "familieboom" als data en regels over vader, moeder, oom, neef/nicht (cousin en nephew) en laat het systeem vragen beantwoorden als "wie zijn (klein-)zonen". Beschrijf/test de werking. Let op dat je geen feiten toevoegt die het systeem zelf af kan leiden dus hou de initiële kennisbank zo klein mogelijk.
### Sub-opdrachten
1. Beschrijf ook hoe je dit systeem 'futureproof' maakt voor eenoudergezinnen.
Het systeem kan eenoudergezinnen aan maar met een paar haken en ogen, dit komt omdat we een `ParentOf`-fact hebben, dit systeem kan het aan dat we een van de ouders in vullen, bijvoorbeeld een moeder of een vader. Maar bij de oom of tante relatie is het nodig dat beide ouders zijn ingevuld om goed te werken. Het kan dus zijn dat het relaties tussen ooms en tantes mist. 

2. Het huidige systeem kan nu niet geslachtsveranderingen of genderneutraliteit aan. Dit komt omdat de `Person`-class nu een verplichte `gender`-veld heeft. Dit kan M of F zijn. 
Om er voor te zorgen dat dit systeem genderneutraliteit en geslachtsverandering aan kan moet er een bredere scala aan gendervariabele zijn voor het systeem. Of een functie die het `gender`-veld aanpast als een geslacht veranderd. Ook zou het `gender`-veld optioneel kunnen worden of een speciaal veld voor genderneutrale mensen. 

3. Het huidige systeem is gefocused op een huwelijk tussen 2 mensen en op relaties tussen ouder, kind en de schoonfamilie. Als dit model dat wel zou moeten kunnend dan zou er een extra `Fact`-type bij kunnen komen die huwelijken of relaties beschrijft. 

4. Laat zien hoe/of het systeem Forward chaining en Backwards chaining toepast en of nieuwe afgeleiden feiten afgeleide feiten permanent of tijdelijk worden oppgeslagen. Zoek ook of de gebruikte inference engine of expert systeem shell in gebruik is (geweest) in de praktijk

Bij forward chaining start het systeem met een aantal facts en past de regels toe op deze facts om nieuwe informatie te krijgen. Elke keer dat er een nieuwe regel wordt toegepast, kunnen er ook nieuwe regels worden toegepast. In dit systeem worden de initiele facts zoals `Persoon` of `ParentOf`, deze worden elke keer getriggerd als hun if condition klopt. Als voorbeeld wanneer de `ParentsOf` fact is gedefineerd worden gelijk de `GrandParentOf` en `UncleAuntOf` getest. 
Backward chaining wordt hier niet gebruikt, dit komt omdat experta geen feature is van de experta module. Bij experta blijven de facts in de knowledge base tot dat het systeem wordt gereset of dat de facts worden "verwijderd". 


## Gebruik
Volg deze stappen om het programma te gebruiken:

1. **Start het Programma**: Open het Python-bestand waarin de familieboom code staat.
2. **Voeg Familieleden Toe**: Het programma staat ingesteld met een voorbeeldfamilie. Deze informatie kan aangepast worden door de `declare`-functies te wijzigen.
3. **Voer het Programma uit**: Draai het script. Het programma toont dan de familierelaties op basis van de ingevoerde gegevens.

## Reflectie
Het was leuk om dit programma te maken en uit te vogelen hoe het werkend te krijgen. Ik heb er in het begin wat problemen mee gehad om PyKnow aan de praat te krijgen, na een aantal keer proberen heb ik het opgegeven om PyKnow werkend te gebruiken en heb ik een oudere versie geinstalleerd van Python (python3.7) en de experta library gebruikt. Ik ben begonnen met het onderzoeken van hoe expert systemen werken door de slides te bestuderen en wat YouTube filmpjes te bekijken. Er waren best weinig voorbeelden voor Python op YouTube, vandaar dat ik Java filmpjes heb opgezocht en toen de Java logica heb omgeschreven in Python aangezien ik dit de fijnste taal vindt om in te werken. Toen ik eenmaal begreep hoe het systeem werkt was het vrij snel klaar ik denk dat ik met studie en programmeren er 4 uur mee bezig ben geweest.


