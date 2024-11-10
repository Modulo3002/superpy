import csv
import datetime as dt
from date import date_of_yesterday


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