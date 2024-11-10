from date import *
import csv
from rich.console import Console
import matplotlib.pyplot as plt
import datetime as dt

console = Console()

#report revenue today
def report_today_revenue():
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
    return console.print(f"[magenta]This is the total revenue of today:[/] [green]{total_revenue:.2f}[/] [magenta]euro[/]")

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
            return console.print(f"[magenta]This is the total revenue of yesterday:[/] [green]{total_revenue:.2f}[/] [magenta]euro[/]")

#report profit
def report_today_profit():
    today = dt.datetime.today()
    to_datetime = today.strftime('%Y-%m-%d')
    
    total_profit = 0.0
    
    with open('sold.csv', 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            if row[3] == to_datetime:
                    bought_price = float(row[4].strip())
                    sell_price = float(row[5].strip())
                    quantity = int(row[6].strip())
                    profit = (sell_price - bought_price) * quantity
                    total_profit += profit

    return console.print(f"[magenta]This is today's total profit:[/] [green]{total_profit:.2f}[/] [magenta]euro[/]")

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
    console.print(f"[magenta]This is yesterday's total profit:[/] [green]{total_profit:.2f}[/] [magenta]euro[/]")


#Which items does the supermarket sell
def supermarket_products():
    console.print(f"[green]Supermarket Products List:[/]")
    with open('bought.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            product_id = row[0].strip()
            product_name = row[1].strip()
            stock = row[2].strip()
            buy_date = row[3].strip()
            buy_price = row[4].strip()
            expiration_date = row[5].strip()

            console.print(f"[magenta]ID:[/] [green]{product_id}[/], [magenta]Name:[/] [green]{product_name}[/], [magenta]Stock:[/] [green]{stock}[/], "
              f"[magenta]Buy Date:[/] [green]{buy_date}[/], [magenta]Buy Price:[/] [green]{buy_price}[/] [magenta]euro[/], "
              f"[magenta]Expiration Date:[/] [green]{expiration_date}[/]")

#Which items have been bought (including expiration date)
def bought_items():
    console.print(f"[green]List of bought items incl. expiration dates:[/]")
    with open('bought.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            product_name = row[1].strip()
            buy_date = row[3].strip()            
            expiration_date = row[5].strip()
            console.print(f"[magenta]Product:[/] [green]{product_name}[/], [magenta]Buy date:[/] [green]{buy_date}[/], [magenta]Expiration Date:[/] [green]{expiration_date}[/]")


#Which product was sold or expired on today.
def sold_or_expired():
    today = dt.datetime.today().strftime('%Y-%m-%d')
    console.print(f"[green]These Items are sold or[/] [red]expired[/] [green]today[/]")
    
    #Items sold today
    with open('sold.csv', 'r') as sold_file:
        reader = csv.reader(sold_file)
        for row in reader:
            sell_date = row[3].strip()
            if sell_date == today:
                product_name = row[2].strip()
                console.print(f"[magenta]Sold Today:[/] [green]{product_name}[/]")

    #Items expired
    with open('bought.csv', 'r') as bought_file:
        reader = csv.reader(bought_file)
        for row in reader:
            product_name = row[1].strip()
            expiration_date = row[5].strip()
            if expiration_date == today:
                console.print(f"[magenta]Expired Today:[/] [green]{product_name}[/]")

#Buy product for which price and what is the expiration data exp 2020-01-01
def buy(product_name, price, quantity, expiration_date):
    buy_date = dt.datetime.today().strftime('%Y-%m-%d')
        
    with open('bought.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        max_id = 0
        for row in reader:
            current_id = int(row[0])  
            if current_id > max_id:
                max_id = current_id 
        purchase_id = max_id + 1  

    with open('bought.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([purchase_id, product_name, quantity, buy_date, price, expiration_date])
        
    console.print(f"[magenta]Recorded purchase of[/] [green]{quantity} {product_name}(s)[/] [magenta]at[/] [green]{price:.2f}[/] [magenta]euro each on[/] [green]{buy_date}[/] [magenta]with expiration date[/] [green]{expiration_date}[/]")

# buy("apple", 1.20, 50, "2024-11-30")


# Function to record a product sale with an auto-incrementing ID and update stock
def sell(product_name, sell_price, quantity, sell_date=None):
    sell_date = sell_date or dt.datetime.today().strftime('%Y-%m-%d')
    
    updated_rows = []
    bought_id = None
    stock_available = 0
    bought_price = None

    with open('bought.csv', 'r') as bought_file:
        reader = csv.reader(bought_file)
        header = next(reader) 
        for row in reader:
            if row[1].strip() == product_name:
                stock_available = int(row[2]) 
                if stock_available >= quantity:
                    bought_id = row[0] 
                    bought_price = float(row[4])  
                    row[2] = str(stock_available - quantity)
                else:
                    console.print(f"[red]Error:[/] Not enough stock available for {product_name}. Available: {stock_available}, requested: {quantity}.")
                    return
                updated_rows.append(row)

    if not bought_id or bought_price is None:
       console.print(f"[red]Error:[/] Product '{product_name}' not found or insufficient stock in 'bought.csv'.")
       return

    # Write the updated stock back to bought.csv
    with open('bought.csv', 'w', newline='') as bought_file:
        writer = csv.writer(bought_file)
        writer.writerow(header)  # Write the header
        writer.writerows(updated_rows)  # Write updated rows


    # Determine the next ID for the new sale record
    with open('sold.csv', 'r') as sold_file:
        reader = csv.reader(sold_file)
        rows = list(reader)
        if rows:
            next_id = len(rows)  # Next ID is the number of rows (excluding header)
        else:
            next_id = 1  # If the file is empty, start from ID 1

    # Write the new sale record to the CSV file
    with open('sold.csv', 'a', newline='') as sold_file:
        writer = csv.writer(sold_file)
        # If the file is empty (first entry), add the header row
        if next_id == 1:
            writer.writerow(['id', 'bought_id', 'product_name', 'sell_date', 'bought_price', 'sell_price', 'quantity'])
        writer.writerow([next_id, bought_id, product_name, sell_date, bought_price, sell_price, quantity])
    console.print(f"[magenta]Recorded sale of[/] [green]{quantity} {product_name}(s)[/] [magenta]at[/] [green]{sell_price:.2f}[/] [magenta]euro each on[/] [green]{sell_date}[/]")


# -------------------------------------------------------
# report revenue of a custom date
def report_for_date(target_date):
    # Format date to string
    to_datetime = target_date.strftime('%Y-%m-%d')
    
    with open('time.txt', 'w') as f:
        f.write(to_datetime)
        
    total_revenue = 0.0
    
    with open('sold.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] == to_datetime:
                sell_price = float(row[5].strip())
                quantity = int(row[6].strip())
                total_revenue += sell_price * quantity
    
    console.print(f"[green]This is the total revenue for {to_datetime}:[/] [magenta]{total_revenue:.2f}[/] [green]euro[/]")
    return total_revenue


#yesterday revenue and reset the date to today
def report_yesterday_and_reset():
    # yesterday date
    yesterday = dt.datetime.today() - dt.timedelta(days=1)
    yesterday_revenue = report_for_date(yesterday)
    
    # date today
    today = dt.datetime.today()
    today_revenue = report_for_date(today)
    
    # Plot the revenue comparison
    show_report_revenue([yesterday_revenue, today_revenue])
    # Reset to today
    set_date_to_today()
    
    console.print(f"[yellow]Date has been reset to today.[/]")

    

# Function to report plot revenue comparison
def show_report_revenue(revenues):
    # Dates for the plot (yesterday and today)
    dates = ['Yesterday', 'Today']
    
    # Show report plot revenue
    plt.figure(figsize=(8, 6))
    plt.bar(dates, revenues, color=['magenta', 'green'])
    
    # Title and labels
    plt.title(f'Revenue difference between yesterday and today')
    plt.xlabel("Date")
    plt.ylabel("Revenue (€)")
    
    # Add the value labels above the bars
    for i, revenue in enumerate(revenues):
        plt.text(i, revenue + 10, f'€{revenue:.2f}', ha='center', va='bottom')
    
    plt.show()

