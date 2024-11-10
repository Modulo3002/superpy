# Handleiding voor SuperPy

## Inleiding
SuperPy is een command-line applicatie waarmee je de inventaris, omzet en winst van een supermarkt kunt beheren. Met behulp van verschillende commando's kun je producten kopen, verkopen, en rapporten genereren over de huidige voorraad, omzet en winst.

## Installatie
1. Zorg ervoor dat Python 3 is geïnstalleerd op je computer.
2. Clone of download het SuperPy-project naar je lokale machine.
3. Installeer eventuele vereiste pakketten met `pip install -r requirements.txt`.

## Gebruik
SuperPy kan worden uitgevoerd via de command-line met verschillende commando's. Hieronder volgt een overzicht van de beschikbare commando's en hun gebruik.

### Commando's

### 1. Voorraadrapport
- **Beschrijving**: Genereert een rapport van de huidige of de voorraad van gisteren.
- **Gebruik**:
  ```bash
  python main.py report_inventory now
  python main.py report_inventory yesterday
  ```

### 2. Omzetrapport
- **Beschrijving**: Genereert een omzetrapport voor vandaag, gisteren of een specifieke datum.
- **Gebruik**:
  ```bash
  python main.py report_revenue today
  python main.py report_revenue yesterday
  python main.py report_revenue date 2024-11-09
  ```

### 3. Winstrapport
- **Beschrijving**: Genereert een winstrapport voor vandaag of gisteren.
- **Gebruik**:
  ```bash
  python main.py report_profit today
  python main.py report_profit yesterday
  ```

### 4. Verkrijgbare Producten
- **Beschrijving**: Toont een lijst van producten die door de supermarkt worden verkocht.
- **Gebruik**:
  ```bash
  python main.py supermarket_products
  ```

### 5. Gekochte Producten (inclusief houdbaarheidsdatum)
- **Beschrijving**: Geeft een overzicht van de gekochte producten en hun houdbaarheidsdatums.
- **Gebruik**:
  ```bash
  python main.py bought_items
  ```

### 6. Producten Verkocht of Verlopen (vandaag)
- **Beschrijving**: Geeft een lijst van producten die vandaag zijn verkocht of verlopen.
- **Gebruik**:
  ```bash
  python main.py sold_or_expired
  ```

### 7. Product Kopen
- **Beschrijving**: Registreert een aankoop van een product.
- **Gebruik**:
  ```bash
  python main.py buy <product_name> <price> <quantity> <expiration_date>
  ```

### 8. Product Verkopen
- **Beschrijving**: Registreert de verkoop van een product.
- **Gebruik**:
  ```bash
  python main.py sell <product_name> <sell_price> <quantity>
  ```

### 9. Tijd Vooruitzetten
- **Beschrijving**: Zet de datum vooruit met een opgegeven aantal dagen.
- **Gebruik**:
  ```bash
  python main.py advance_time <days>
  ```

### 10. Datum Instellen op Vandaag
- **Beschrijving**: Stelt de datum in op de huidige dag.
- **Gebruik**:
  ```bash
  python main.py set_date
  ```

### 11. Omzetvergelijking met Gisteren
- **Beschrijving**: Toont een vergelijking van de omzet van vandaag ten opzichte van gisteren.
- **Gebruik**:
  ```bash
  python main.py compare_to_yesterday
  ```

## Voorbeeldcommando's
Hieronder staan enkele voorbeeldcommando's om snel aan de slag te gaan:
- Registreer de aankoop van 10 appels voor €1,00 per stuk, met een houdbaarheidsdatum van 2024-12-01:
  ```bash
  python main.py buy apple 1.0 10 2024-12-01
  ```
- Verkoop 5 appels voor €1,50 per stuk:
  ```bash
  python main.py sell apple 1.5 5
  ```
------------------------------------------------------------------------------------------------------------------------












# Guide for SuperPy

## Introduction
SuperPy is a command-line application that allows you to manage the inventory, revenue, and profit of a supermarket. With various commands, you can buy and sell products, as well as generate reports on current stock, revenue, and profit.

## Installation
1. Ensure Python 3 is installed on your computer.
2. Clone or download the SuperPy project to your local machine.
3. Install any required packages using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
SuperPy can be run from the command line with different commands. Below is an overview of the available commands and their usage.

### Commands

### 1. Inventory Report
- **Description**: Generates a report of the current inventory or yesterday’s inventory.
- **Usage**:
  ```bash
  python main.py report_inventory now
  python main.py report_inventory yesterday
  ```

### 2. Revenue Report
- **Description**: Generates a revenue report for today, yesterday, or a specific date.
- **Usage**:
  ```bash
  python main.py report_revenue today
  python main.py report_revenue yesterday
  python main.py report_revenue date 2024-11-09
  ```

### 3. Profit Report
- **Description**: Generates a profit report for today or yesterday.
- **Usage**:
  ```bash
  python main.py report_profit today
  python main.py report_profit yesterday
  ```

### 4. Available Products
- **Description**: Shows a list of products sold by the supermarket.
- **Usage**:
  ```bash
  python main.py supermarket_products
  ```

### 5. Purchased Products (Including Expiration Date)
- **Description**: Provides an overview of purchased products and their expiration dates.
- **Usage**:
  ```bash
  python main.py bought_items
  ```

### 6. Sold or Expired Products (Today)
- **Description**: Lists products sold or expired today.
- **Usage**:
  ```bash
  python main.py sold_or_expired
  ```

### 7. Buy Product
- **Description**: Records the purchase of a product.
- **Usage**:
  ```bash
  python main.py buy <product_name> <price> <quantity> <expiration_date>
  ```

### 8. Sell Product
- **Description**: Records the sale of a product.
- **Usage**:
  ```bash
  python main.py sell <product_name> <sell_price> <quantity>
  ```

### 9. Advance Time
- **Description**: Advances the current date by a specified number of days.
- **Usage**:
  ```bash
  python main.py advance_time <days>
  ```

### 10. Set Date to Today
- **Description**: Sets the date to the current day.
- **Usage**:
  ```bash
  python main.py set_date
  ```

### 11. Compare Revenue with Yesterday
- **Description**: Shows a comparison of today’s revenue with yesterday’s revenue.
- **Usage**:
  ```bash
  python main.py compare_to_yesterday
  ```

## Example Commands
Here are some example commands to get started quickly:
- Record the purchase of 10 apples for €1.00 each, with an expiration date of 2024-12-01:
  ```bash
  python main.py buy apple 1.0 10 2024-12-01
  ```
- Sell 5 apples for €1.50 each:
  ```bash
  python main.py sell apple 1.5 5
  ``` 