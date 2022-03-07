import schedule
import time
import os
from dataclasses import dataclass, field


def job(a):
    print(a)
    os.system('date')

def consulta_db():
    # recupera intervalo de tempo que a loja esta configurada no postgres
    print("I'm getting variables...")

schedule.every(1).minutes.do(consulta_db)

lojas = {
    1558 : {
        'current_interval':1,
        'updated_interval':1,
        'last_run':'',
    }
}
def update_lojas():
    pass

schedule.every(3).seconds.do(job,a=23)
schedule.every(2).minutes.do(job)
schedule.every(3).weeks.do(job)

# Run job every minute at the 23rd second
schedule.every().minute.at(":23").do(job)

# Run job every hour at the 42rd minute
schedule.every().hour.at(":42").do(job)

# Run jobs every 5th hour, 20 minutes and 30 seconds in.
# If current time is 02:00, first execution is at 06:20:30
schedule.every(5).hours.at("20:30").do(job)

# Run job every day at specific HH:MM and next HH:MM:SS
schedule.every().day.at("10:30").do(job)
schedule.every().day.at("10:30:42").do(job)

# Run job on a specific day of the week
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

