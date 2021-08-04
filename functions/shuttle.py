
from flask import request, session, jsonify
from pymongo import MongoClient
import datetime
import random
from bson import ObjectId

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

        # check log in 
        if 'logged_in' not in session:
            return jsonify({"error": "not logged in"}), 400

        item = request.form['items_give']
        # check empty
        if item == "":
            return jsonify({"error": "empty string"}), 400

        name = session['user']['name']
        userID = session['user']['userID']

        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')

        new_items = {
            'name': name,
            'item': item,
            'userID': userID
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

        player = set()
        
        for i in info :
            player.add(i.get('name'))
            # print(data[0]['content'][i]) <- 이게 뭔 뻘짓

        # 리스트 중복 제거 (한 사람이 여러 개 넣어도 당첨 확률은 다른이들과 동일함)
        # new_list = []
        # for v in player:
        #     if v not in new_list:
        #         new_list.append(v)
        # print(player)
        # print(new_list)

        # 두 명 추출
        winner = random.sample(player, 2)
        print(winner)
        
        db.shuttles.update_one({"date": date}, {"$set": {"winner": winner}})




    def delete_item(self):
        id = ObjectId(request.form.get('_id'))
        posted_date = request.form.get('date')

        # check if user did log in
        if 'logged_in' not in session:
            return jsonify({"error": "not logged in"}), 400

        user_id = ObjectId(session['user']['_id'])
        # check user matches the posting
        userdata = db.users.find_one({"_id": user_id})
        if id not in userdata['postings']:
            return jsonify({"error": "others postings"}), 400

        # delete the postings @ items, shuttles, users collection
        cond1 = db.items.delete_one({"_id": id})
        cond2 = db.users.update_one({"_id": user_id}, {"$pull": {"postings":{"$in":[id]}}})

        content = db.shuttles.find_one({"date": posted_date})['content']
        for idx, posting in enumerate(content):
            if posting['_id'] == id:
                target = idx
                break
        del content[idx]
        # re update to mongoDB
        cond3 = db.shuttles.update_one({"date": posted_date}, {"$set": {"content": content}})
        if cond1 and cond2 and cond3:
            return jsonify({"success": "deleted successfully"}), 200

        return jsonify({"error": "deleting failed"}), 400


