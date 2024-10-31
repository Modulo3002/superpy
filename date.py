import datetime as dt   

# set date to today functio
def set_date_to_today():
    today = dt.datetime.today()
    to_datetime = today.strftime('%Y-%m-%d')
    with open ('time.txt', 'w') as f:
        f.write(to_datetime)

with open ('time.txt','r') as f:
    current_date = f.readline()

# Advance time in days
def advance_time(days: int):
    to_datetime = dt.datetime.strptime(current_date, '%Y-%m-%d')
    timedelta = dt.timedelta(days=days)
    new_date = to_datetime + timedelta

    with open ('time.txt', 'w') as f:
        f.write(new_date.strftime('%Y-%m-%d'))

# Sets date of yesterday
def date_of_yesterday():
    to_datetime = dt.datetime.strptime(current_date, '%Y-%m-%d')
    timedelta = dt.timedelta(days=1)
    new_date = to_datetime - timedelta

    with open ('time.txt', 'w') as f:
        f.write(new_date.strftime('%Y-%m-%d'))

# set date in days
def set_date():
    today=dt.datetime.today()
    # print(today.strftime('%Y-%m-%d'))
    with open ('time.txt', 'w') as f:
        f.write(today.strftime('%Y-%m-%d')) 

# Beiden implementeren in programma
#aanroep van de functie werkt
# date_of_yesterday()

#werkt ook
# advance_time(5)

