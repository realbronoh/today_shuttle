from flask import Flask, jsonify, request, session
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('3.35.205.48', 27017)
db = client.today_shuttle

import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
 # 실행할 함수

# import threading
# import multiprocessing

def cronwork():
    def exec_cron():
        print('1분 마다 exec cron 크론이 실행되었습니다.')

    def exec_cron2():
        print('지정된 시간에 exec cron 크론이 실행되었습니다.')

    sched = BlockingScheduler()

    # 예약방식 interval로 설정, 10초마다 한번 실행
    # sched.add_job(exec_cron, 'interval', seconds=10)

    # 예약방식 cron으로 설정, 각 5배수 분의 10, 30초마다 실행
    # ex) (5분 10, 30초), (10분 10, 30초), (15분 10, 30초)
    sched.add_job(exec_cron, 'cron', minute='*/5', second='10, 30')

    sched.add_job(exec_cron, 'cron', minute='*/1', second='10')

    sched.add_job(exec_cron2, 'cron', hour='14', minute='25', second='10')

    sched.start() # 스케줄링 시작


@app.route('/')
def home():
   return 'This is Home!'

# main data 불러오기
@app.route('/allshuttles', methods=['GET'])
def allshuttles():
    allshuttle = list(db.shuttles.find({}, {'_id': 0}).sort({'date': -1}))
    # allshuttle = list(db.shuttles.find({}, {'_id': 0}).sort({'date': -1}))
    print(allshuttle)
    return jsonify({'result': 'success', 'allshuttle': allshuttle})

# 오늘 셔틀 추가
@app.route('/addtodayshuttle', methods=['GET'])
def add_today():
    return new_today_shuttle()

def new_today_shuttle():
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')

    today_shuttle = {
        'date': nowDate,
        'content': []
    }

    db.shuttles.insert_one(today_shuttle)
    return None

@app.route('/gettoday', methods=['GET'])
def get_today():
    today_shuttle = list(db.today.find({}, {'_id':0}))
    return jsonify({'result': 'success', 'today_shuttle': today_shuttle})

# item 추가
@app.route('/additem', methods=['GET'])
def get_additem():
    return;

@app.route('/additem', methods=['POST'])
def post_additem():
    item = request.form['items_give']
    
    userID = session['user']['userID']
    print(userID) #

    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')

    new_items = {
        'user': userID,
        'items': item
    }

    additem_result = db.items.insert_one(new_items)
    print(new_items)

    update_result = db.shuttles.update_one({'date': nowDate}, { '$push' : { 'content': new_items }})    
    # db.shuttles.update_one({'date': nowDate}, { '$push' : { 'content': new_items }})
    # db.shuttles.update_one({'data': nowDate}, new_items)
    return jsonify({'result': 'success'})

# 셔틀 만들기
@app.route('/makeshuttle', methods=['GET'])
def makeshuttles():

    new_shuttle = {
        'date': '2021-08-01',
        'winner': ['홍예지', '김갑수'],
        'content': [{'name': '김명민', 'item': '참치캔, 모니터'}, {'name' :'호날두', 'item':'콜라' }]
    }

    db.shuttles.insert_one(new_shuttle)
    return "muyaho"

# 물품 지우기
@app.route('/delete', methods=['POST'])
def deleteitem():
    return

if __name__ == '__main__':  
    app.run('0.0.0.0', port=5000, debug=True)
   