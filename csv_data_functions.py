import csv
import datetime as dt
from date import date_of_yesterday

#read bought.csv file
#dit is al report inventory
def report_current_inventory():
    with open ('bought.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def report_yesterday_inventory():
    date_of_yesterday()
    with open('time.txt', 'r') as f:
            yesterday_date = f.readline().strip()
    with open ('bought.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] == yesterday_date:
                print(row)

def report_today_revenue():
      



# Eerste versie functie
# def report_yesterday_inventory():
#     with open('time.txt', 'r') as f:
#         current_date = f.readline()

#     with open ('bought.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
             
#             print(row)

# #read sold.csv file 
# with open ('sold.csv', 'r') as file:
#     reader = reader(file)
#     for row in reader:
#         print(row)

# #write to bought.csv file
# with open ('bought.csv', 'w', newline='') as file:
#     writer = writer(file)
#     writer.writerow(['id', 'product_name', 'buy_price', 'expiration_date'])
#     writer.writerow(['1', 'Apples', '$2', '2023-05-01'])