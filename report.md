# Rapport: Drie Belangrijke Technische Aspecten van de Implementatie

## 1. Gebruik van argparse voor een supermarkt CLI-Tool  
In dit project wordt gebruik gemaakt van de `argparse` library om command-line inputs te verwerken. Dit biedt veel flexibiliteit wanneer de app wordt uitgevoerd, waardoor de gebruiker eenvoudig verschillende acties kan kiezen. Het genereren van reports, het kopen of verkopen van producten, of het aanpassen van de tijd. Met voorbeelden van deze commando's zijn `report_inventory`, `buy` en `sell`. Hiermee kan de gebruiker precies aangeven wat hij wil doen. Het --help argument zorgt ervoor dat de gebruiker altijd weet welke opties beschikbaar zijn (bijvoorbeeld kiezes voor "today", "yesterday" of een specifieke datum).

## 2. Werken met CSV-bestanden voor inventory en reporting  
Het gebruik maken van CSV-bestanden om inventory en selldata op te slaan. De files `bought.csv` en `sold.csv` worden gebruikt om koop- en verkoopacties bij te houden. Het programma leest deze bestanden om reports te genereren over de verkopen. Door deze CSV-files te gebruiken, is het mogelijk om gemakellijk data op te slaan en te manipuleren zonder een complex database op te zetten. Dit zorgt voor een simpel en effectieve CLI-tool.

## 3. Timecontrol met de datetime Module  
Timecontrol is een ander deel van het programma. De reports zijn meestal afhankelijk van de data van vandaag of gisteren, de `datetime` module wordt gebruikt om de tijd op te roepen of aan te passen. Hierdoor kan automatisch de datum van vandaag of gisteren opgehaald worden om de reports te genereren. 
