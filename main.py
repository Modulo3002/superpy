# Imports
from argparse import *
from csv import *
from datetime import date
from argparse import ArgumentParser
from functions import *
from csv_data_functions import *

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
parser = ArgumentParser(description="SuperPy, a command-line inventory system.")
subparser = parser.add_subparsers(dest="command")

#report inventory
report_parser = subparser.add_parser("report_inventory", help="Generate a report with 'report_inventory now' or 'report_inventory yesterday'.")
report_parser.add_argument("report_time", choices=["now", "yesterday"], help="Choose a report time. Choice are 'now' or 'yesterday'")
    

# report revenue
report_parser = subparser.add_parser("report_revenue", help="Generate a revenue report for today with 'report_revenue today', yesterday with 'report_revenue yesterday' or a custom date in format YYYY-MM-DD. Example: 'report_revenue 2024-11-09'")
report_parser.add_argument("report_time", choices=["today", "yesterday"], help="Choose a revenue report time. Choices are 'today'or 'yesterday'")
report_parser.add_argument("date", help="Put in the date of choice in format YYYY-MM-DD please")

#report profit
report_parser = subparser.add_parser("report_profit", help="Generate a profit report for today with 'report_profit today' or yesterday with 'report_profit yesterday'")
report_parser.add_argument("report_time", choices=["today", "yesterday"], help="Choose a profit report time. Choices are 'today' or 'yesterday'")

#Which items does the supermarket sell
report_parser = subparser.add_parser("supermarket_products", help="Generate a list of items sold at the supermarket.")

#Which items have been bought (including expiration date) by the supermarket
report_parser = subparser.add_parser("bought_items", help="Generate a list of items bought at the supermarket including expiration date.")

#Which product was sold or expired on this day(TODAY!).
report_parser = subparser.add_parser("sold_or_expired", help="Generate a list of items sold or expired at the supermarket.")


#Buy parser product for which price and what is the expiration data exp 2020-01-01  
report_parser = subparser.add_parser("buy", help="Buys a product. Format is: buy product_name price quatity expiration_date")
report_parser.add_argument("product_name", help="Name of the product to buy.")
report_parser.add_argument("price", type=float, help="Price of the product.")
report_parser.add_argument("quantity", help="How many of the product did you buy.")
report_parser.add_argument("expiration_date", help="Expiration date of the product (YYYY-MM-DD).")

#Sell parser which product for what price
report_parser = subparser.add_parser("sell", help="Sell a product. Format is: sell product_name sell_price quatity")
report_parser.add_argument("product_name", help="Name of the product to sell.") 
report_parser.add_argument("sell_price", type=float, help="Price of the product.")
report_parser.add_argument("quantity", help="How many of the product to sell")

#advance time by day's
advance_time_parser = subparser.add_parser("advance_time", help="Set a new date by adding days to current date. Example: advance_time 1 (advances time by 1 day)")
advance_time_parser.add_argument("days", type=int, help="Number of days to advance the date.")

#set date to today
set_date_parser = subparser.add_parser("set_date", help="Set ttoday as date.")

#show report of revenue comparerd to yesterday
report_parser = subparser.add_parser("compare_to_yesterday", help="Show report of todays revenue compared to yesterday")



def main():
    args = parser.parse_args()
#report inventory
    if args.command == "report_inventory":
        if args.report_time == "now":
            report_current_inventory()

        if args.report_time == "yesterday":
            report_yesterday_inventory()
   
    #report revenue
    if args.command == "report_revenue":
        if args.report_time == "today":
            report_today_revenue()

        if args.report_time == "yesterday":
            report_yesterday_revenue()

        if args.report_time == "date":
            report_for_date(args.date)

    #report profit
    if args.command == "report_profit":
        if args.report_time == "today":
            report_today_profit()

        if args.report_time == "yesterday":
            report_yesterday_profit()

    #Which items does the supermarket sell
    if args.command == "supermarket_products":
        supermarket_products()

    #Which items have been bought (including expiration date) by the supermarket
    if args.command == "bought_items":
        bought_items()

    #Which product was sold or expired on this day(TODAY!).
    if args.command == "sold_or_expired":
        sold_or_expired()

    #Buy product for which price and what is the expiration data exp 2020-01-01
    if args.command == "buy":
        buy(args.product_name, args.price, args.quantity, args.expiration_date)

    #Sell product for which price
    if args.command == "sell":
        sell(args.product_name, args.sell_price, args.quantity,)

    #advance time by day's
    if args.command == "advance_time":
        advance_time(args.days)

    #set date to today's date
    #deze functie is ready!
    if args.command == "set_date":
        set_date_to_today()

    #show graph of revnue today compared to yesterday
    if args.command == "compare_to_yesterday":
        report_yesterday_and_reset()

if __name__ == "__main__":
    main()
