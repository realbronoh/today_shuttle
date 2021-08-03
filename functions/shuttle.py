
from flask import request, session, jsonify
from pymongo import MongoClient
import datetime

##########################
# DB
client = MongoClient('3.35.205.48', 27017)
db = client.today_shuttle

class Shuttle():

    def new_today_shuttle(self):
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')

        today_shuttle = {
            'date': nowDate,
            'content': []
        }

        db.shuttles.insert_one(today_shuttle)
        return None

    def post_additem(self):
        item = request.form['items_give']
        
        userID = session['user']['userID']

        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')

        new_items = {
            'name': userID,
            'item': item
        }

        additem_result = db.items.insert_one(new_items)
        print(new_items)

        if db.shuttles.update_one({'date': nowDate}, { '$push' : { 'content': new_items }}):

            db.users.update_one({"userID": userID}, {'$push': {'postings': new_items['_id']}})
            return jsonify({'result': 'success'}), 200

        return jsonify({"error": "post item failed"}), 400

        # db.shuttles.update_one({'date': nowDate}, { '$push' : { 'content': new_items }})
        # db.shuttles.update_one({'data': nowDate}, new_items)


