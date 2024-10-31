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
report_parser = subparser.add_parser("report_inventory", help="Generate a report.")
report_parser.add_argument("report_time", choices=["now", "yesterday"], help="Choose a report time.")
# report_parser.add_argument("--now", action="store_true", help="Report current inventory.")
# report_parser.add_argument("--yesterday", action="store_true", help="Report yesterday's inventory.")    

# report revenue
report_parser = subparser.add_parser("report_revenue", help="Generate a revenue report.")
report_parser.add_argument("report_time", choices=["today", "yesterday"], help="Choose a revenue report time.")
# report_parser.add_argument("today", action="store_true", help="Report today's revenue.")
# report_parser.add_argument("yesterday", action="store_true", help="Report yesterday's revenue.")

#report profit
report_parser = subparser.add_parser("report_profit", help="Generate a profit report.")
report_parser.add_argument("report_time", choices=["today", "yesterday"], help="Choose a profit report time.")
# report_parser.add_argument("--today", action="store_true", help="Report today's profit.")
# report_parser.add_argument("--yesterday", action="store_true", help="Report yesterday's profit.")

#Which items does the supermarket sell
report_parser = subparser.add_parser("supermarket_products", help="Generate a list of items sold at the supermarket.")

#Which items have been bought (including expiration date) by the supermarket
report_parser = subparser.add_parser("bought_items", help="Generate a list of items bought at the supermarket including expiration date.")

#Which product was sold or expired on this day(TODAY!).
report_parser = subparser.add_parser("sold_or_expired", help="Generate a list of items sold or expired at the supermarket.")


#Buy parser product for which price and what is the expiration data exp 2020-01-01  
report_parser = subparser.add_parser("buy", help="Buy a product.")
report_parser.add_argument("product_name", help="Name of the product to buy.")
report_parser.add_argument("price", type=float, help="Price of the product.")
report_parser.add_argument("expiration_date", help="Expiration date of the product (YYYY-MM-DD).")

#Sell parser which product for what price
report_parser = subparser.add_parser("sell", help="Sell a product.")
report_parser.add_argument("product_name", help="Name of the product to sell.") 
report_parser.add_argument("price", type=float, help="Price of the product.")


#advance time by day's
advance_time_parser = subparser.add_parser("advance_time", help="Set a new date by adding days to current date.")
report_parser.add_argument("days", type=int, help="Number of days to advance the date.")

#set date
set_date_parser = subparser.add_parser("set_date", help="Set the current date.")



def main():
    args = parser.parse_args()
#report inventory
#deze functies is ready!
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
        buy(args.product_name, args.price, args.expiration_date)

    #Sell product for which price
    if args.command == "sell":
        sell(args.product_name, args.price)

    #advance time by day's
    if args.command == "advance_time":
        advance_time(args.days)

    #set date to today's date
    #deze functie is ready!
    if args.command == "set_date":
        set_date()



if __name__ == "__main__":
    main()
