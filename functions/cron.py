# cron
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

#shuttle import
from functions.shuttle import Shuttle




def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

def at_lunch_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

def do_cron_job():
    Shuttle().get_winner()
    Shuttle().new_today_shuttle()


scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", seconds=100)
scheduler.add_job(at_lunch_time, 'cron', hour='9', minute='19')
scheduler.start()



# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())