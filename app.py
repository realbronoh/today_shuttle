from flask import Flask
app = Flask(__name__)

from apscheduler.schedulers.blocking import BlockingScheduler
 # 실행할 함수

def exec_cron():
    print('exec cron 크론이 실행되었습니다.')

sched = BlockingScheduler()

# 예약방식 interval로 설정, 10초마다 한번 실행
# sched.add_job(exec_cron, 'interval', seconds=10)

# 예약방식 cron으로 설정, 각 5배수 분의 10, 30초마다 실행
# ex) (5분 10, 30초), (10분 10, 30초), (15분 10, 30초)
# sched.add_job(exec_cron, 'cron', minute='*/5', second='10, 30')

sched.add_job(exec_cron, 'cron', minute='*/5', second='10')

# 스케줄링 시작
sched.start()

# import time
# import schedule

# def printhello():
#     print("Hello")

# def printlunch():
#     print("점심시간입니다")

# schedule.every().day.at("13:10").do(printlunch) # 매일 12시에 실행
# schedule.every(2).minutes.do(printhello) # 3분마다 실행

# #스케줄 실행
# while True:
#     schedule.run_pending()
#     time.sleep(1) 



@app.route('/')
def home():
   return 'This is Home!'

# main data 불러오기
@app.route('/allshuttles', methods=['GET'])
def allshuttles():
    return;

# item 추가
@app.route('/additem', methods=['GET'])
def get_additem():
    return;

@app.route('/additem', methods=['POST'])
def post_additem():
    return

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)

