from flask import Flask
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('3.35.205.48', 27017)
db = client.today_shuttle

from apscheduler.schedulers.blocking import BlockingScheduler
 # 실행할 함수

# import threading
import multiprocessing

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
    allshuttle = db.shuttles.find({}, {'_id': 0})
    return;

# item 추가
@app.route('/additem', methods=['GET'])
def get_additem():
    return;

@app.route('/additem', methods=['POST'])
def post_additem():
    return

if __name__ == '__main__':  
    t = multiprocessing.Process(target=cronwork)
    t.start()
    t.join()
    print("무야호")
    app.run('0.0.0.0', port=5000, debug=True, threaded=True)
   