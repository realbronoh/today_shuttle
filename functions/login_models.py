###########################################
# login User Class

from flask import jsonify, request, session, redirect, render_template
from passlib.hash import pbkdf2_sha256
import pymongo
import datetime

# Database
client = pymongo.MongoClient('3.35.205.48', 27017)
db = client.today_shuttle

class User:

    # 원본
    def render_homepage(self):
        data = sorted(db.shuttles.find({}), key=lambda x: x['date'], reverse=True)
        ##############################
        ## Suttle().post_additem() 내 형식이랑 같아야 함
        now = datetime.datetime.now()
        today = sorted(db.shuttles.find({}), key=lambda x: x['date'], reverse=True)[0]['date']
        return render_template('index.html', session=session, data=data, today=today)




    def start_session(self, user):
        # delete before store user data in session
        del user['password']
        try:
            del user['postings']  ## 수정 부분
        except:
            pass
        session['logged_in'] = True
        session['user'] = user

        # change ObjectId to str
        user['_id'] = str(user['_id'])

        return jsonify(user), 200

    def signup(self):
        # Encrypt password
        password = pbkdf2_sha256.encrypt(request.form.get('password'))

        user = {
            "userID": request.form.get('userID'),
            "name": request.form.get('name'),
            "password": password
        }

        # Check for existing name
        if db.users.find_one({"userID": user['userID']}):
            return jsonify({"error": "user ID already in use"}), 400

        # insert user doc to mongoDB and start session
        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):
        user = db.users.find_one({
            "userID": request.form.get('userID')
        })
        # check whether user exist and password matches
        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)
        return jsonify({"error": "Invalid login credentials"}), 401

    def change_pw(self):
        user = db.users.find_one({
            "userID": request.form.get('userID')
        })
        # check existing user and matches pw
        if user and pbkdf2_sha256.verify(request.form.get('oldPassword'), user['password']):
            # Encrypt password
            new_password = pbkdf2_sha256.encrypt(request.form.get('newPassword'))
            db.users.update_one({"name": user['name']}, {"$set": {"password": new_password}})
            return self.start_session(user)
        return jsonify({"error": "password updated failed: not existing ID or not matcing password"}), 400