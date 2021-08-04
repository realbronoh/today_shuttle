
from flask import request, session, jsonify
from pymongo import MongoClient
import datetime
# from bson.json_util import dumps

import random

import pymongo

##########################
# DB
client = MongoClient('3.35.205.48', 27017)
db = client.today_shuttle

class Shuttle():

    def new_today_shuttle(self):
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d %H:%M')

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

    def get_winner(self):
        # now = datetime.datetime.now()
        # nowDate = now.strftime('%Y-%m-%d')

        # failed to get latest
        # latest = db.shuttles.find().sort({'_id', 1}).limit(1)
        # latest = list(db.shuttles.find_one(sort=[( '_id', pymongo.DESCENDING )]))
        # latest = db.collection.find().limit(1).sort({'$natural':-1})
        # latest = db.shuttles.find().sort({'_id': -1}).limit(1)

        data = sorted(db.shuttles.find({}), key=lambda x: x['date'], reverse=True)
        # get latest shuttle
        info = data[0]['content']
        date = data[0]['date']

        player = []
        
        for i in info :
            player.append(i.get('name'))
            # print(data[0]['content'][i]) <- 이게 뭔 뻘짓

        # 리스트 중복 제거 (한 사람이 여러 개 넣어도 당첨 확률은 다른이들과 동일함)
        new_list = []
        for v in player:
            if v not in new_list:
                new_list.append(v)
        print(player)
        print(new_list)

        # 두 명 추출
        winner = random.sample(new_list, 2)
        print(winner)
        
        db.shuttles.update_one({"date": date}, {"$set": {"winner": winner}})






