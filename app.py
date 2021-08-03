from flask import Flask
from functions.shuttle import Shuttle
app = Flask(__name__)

# 오늘 셔틀 추가
@app.route('/addtodayshuttle', methods=['GET'])
def add_today():
    return Shuttle().new_today_shuttle()


@app.route('/additem', methods=['POST'])
def post_additem():
    return Shuttle().post_additem()

if __name__ == '__main__':  
    app.run('0.0.0.0', port=5000, debug=True)



# # 셔틀 만들기( 테스트용 )
# @app.route('/makeshuttle', methods=['GET'])
# def makeshuttles():

#     new_shuttle = {
#         'date': '2021-08-01',
#         'winner': ['홍예지', '김갑수'],
#         'content': [{'name': '김명민', 'item': '참치캔, 모니터'}, {'name' :'호날두', 'item':'콜라' }]
#     }

#     db.shuttles.insert_one(new_shuttle)
#     return "muyaho"

# # 물품 지우기
# @app.route('/delete', methods=['POST'])
# def deleteitem():
#     return
