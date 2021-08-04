# cron
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from flask import redirect
from functions.shuttle import Shuttle
from functions.login_models import User



def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

def at_lunch_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

def do_cron_job():
    print("##############################\n#############################\n###########################")
    Shuttle().get_winner()
    Shuttle().new_today_shuttle()

scheduler = BackgroundScheduler()
do_cron_job()
scheduler.add_job(func=do_cron_job, trigger="interval", seconds=60)
scheduler.add_job(at_lunch_time, 'cron', hour='9', minute='19')
scheduler.start()



# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())