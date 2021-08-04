from flask import Flask, render_template
from functions.shuttle import Shuttle
from functions.login_models import User

app = Flask(__name__)
app.secret_key = b'Q^\xb5Z\n\xed\x9d\xcf\n\xfem\x0c\xc2l\x96\\'
# 'os.urandom(16)'

#import cron
from functions.cron import *


################################################
# Routes

@app.route('/')
def home():
    return User().render_homepage()

@app.route('/addtodayshuttle', methods=['GET'])
def add_today():
    return Shuttle().new_today_shuttle()

@app.route('/additem', methods=['POST'])
def post_additem():
    return Shuttle().post_additem()

@app.route('/deleteitem', methods=['POST'])
def delete_item():
    return Shuttle().delete_item()

@app.route('/login/')
def login_window():
    return render_template('login.html')

@app.route('/user/signup', methods=['GET', 'POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
    return User().login()

@app.route('/user/change_pw', methods=['POST'])
def change_pw():
    return User().change_pw()

@app.route('/test')
def test():
    return "TEST"


if __name__ == '__main__':  
    app.run('0.0.0.0', port=5000, debug=True, use_reloader=False)