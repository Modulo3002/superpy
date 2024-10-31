from date import *
import csv


#report revenue today
def report_today_revenue():
    # today = '2024-07-04'
    # to_datetime = today
    today = dt.datetime.today()
    to_datetime = today.strftime('%Y-%m-%d')
    with open ('time.txt', 'w') as f:
        f.write(to_datetime)
    with open('time.txt', 'r') as f:
        date=f.readline().strip()
    total_revenue = 0.0
    if to_datetime == date:
        with open('sold.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3] == to_datetime:
                    sell_price = float(row[5].strip())
                    quantity = int(row[6].strip())
                    total_revenue+= sell_price * quantity
    return print(f"This is the total revenue of today: {total_revenue:.2f} euro")

#report revenue yesterday
def report_yesterday_revenue():
    date_of_yesterday()
    total_revenue = 0.0
    with open('time.txt', 'r') as f:
            date=f.readline().strip()
    with open('sold.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3] == date:
                    sell_price = float(row[5].strip())
                    quantity = int(row[6].strip())
                    total_revenue+= sell_price * quantity
    return print(f"This is the total revenue of yesterday: {total_revenue:.2f} euro")

#report profit
def report_today_profit():
    today = dt.datetime.today()
    to_datetime = today.strftime('%Y-%m-%d')
    
    total_profit = 0.0
    
    # Open and read the sold.csv file to calculate profit for today's date
    with open('sold.csv', 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            # Check if sell_date (row[3]) matches today's date
            if row[3] == to_datetime:
                    bought_price = float(row[4].strip())
                    sell_price = float(row[5].strip())
                    quantity = int(row[6].strip())
                    profit = (sell_price - bought_price) * quantity
                    total_profit += profit

    return print(f"This is today's total profit: ${total_profit:.2f}")

def report_yesterday_profit():
    yesterday = dt.datetime.today() - dt.timedelta(days=1)
    to_datetime = yesterday.strftime('%Y-%m-%d')
    
    total_profit = 0.0
    
     # Open and read the sold.csv file to calculate profit for yesterday's date
    with open('sold.csv', 'r') as file:
        reader = csv.reader(file)        
        for row in reader:
            if row[3] == to_datetime:
                    bought_price = float(row[4].strip())
                    sell_price = float(row[5].strip())
                    quantity = int(row[6].strip())
                    
                    # Calculate profit for this row and add it to total profit
                    profit = (sell_price - bought_price) * quantity
                    total_profit += profit    
    # Print the total profit for yesterday
    print(f"This is yesterday's total profit: ${total_profit:.2f}")


#Which items does the supermarket sell
def supermarket_products():
    print("Supermarket Products List:")
    with open('bought.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            product_id = row[0].strip()
            product_name = row[1].strip()
            stock = row[2].strip()
            buy_date = row[3].strip()
            buy_price = row[4].strip()
            expiration_date = row[5].strip()
            print(f"ID: {product_id}, Name: {product_name}, Stock: {stock}, Buy Date: {buy_date}, "
                  f"Buy Price: ${buy_price}, Expiration Date: {expiration_date}")

#Which items have been bought (including expiration date) by the supermarket
def bought_items():
    print("List of bought items incl. expiration dates:")
    with open('bought.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            product_name = row[1].strip()
            buy_date = row[3].strip()            
            expiration_date = row[5].strip()
            print(f"Product: {product_name}, Buy date: {buy_date}, Expiration Date: {expiration_date}")
bought_items()


#Which product was sold or expired on today.
def sold_or_expired():
    today = dt.datetime.today().strftime('%Y-%m-%d')
    print("These Items are sold or expired today")
    
    #Items sold today
    with open('sold.csv', 'r') as sold_file:
        reader = csv.reader(sold_file)
        for row in reader:
            sell_date = row[3].strip()
            if sell_date == today:
                product_name = row[2].strip()
                print(f"Sold Today: {product_name}")
    
    #Items expired
    with open('bought.csv', 'r') as bought_file:
        reader = csv.reader(bought_file)
        for row in reader:
            product_name = row[1].strip()
            expiration_date = row[5].strip()
            if expiration_date == today:
                print(f"Expired Today: {product_name}")

#Buy product for which price and what is the expiration data exp 2020-01-01
def buy(product_name, price, expiration_date):
    return print(f"Buying {product_name} for ${price} with expiration date {expiration_date}")

#Sell parser which product for what price
def sell(product_name, price):
    return print(f"Selling {product_name} for ${price}")

#advance time by day's
# advance_time(2)
