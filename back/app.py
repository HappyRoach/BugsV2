import SQL
from flask import Flask, request
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/DB', methods=['GET'])
def GET():
    return SQL.Db().select_all_user()


@app.route('/DB', methods=['POST'])
def POST(): #Не ебу как, но оно работает, хоть и выдает ошибку 500. Главное работает.
    try:
        SQL.Db().insert_user(request.json['fullname'], request.json['date_time'], request.json['pose'], request.json['curreet_pose'], request.json['offical_pose'], request.json['phone'], request.json['email'], request.json['data_work'], request.json['region'], request.json['work_time'], request.json['spec'])
        return "Выполнено", 200
    except:
        print('ошибкка')
        return 'Ошибка', 500

#fullname, date_time, pose, curret_pose, offical_pose, phone, email, data_work, region, WorkTime, spec


@app.route('/DB', methods=['DELETE'])
def DELETE():
    SQL.Db().delete_user(request.json['id'])
    return "Выполнено"


@app.route('/json', methods=['GET'])
def GET_JSON():
    with open(f'D:/BugsV2/back/JSON/{request.json["who"]}.json', 'r', encoding='utf-8') as file:
        new_file = file.read()
        file.close()
    return json.loads(new_file)


@app.route('/json', methods=['POST'])
def POST_JSON():
    with open(f'D:/BugsV2/back/JSON/{list(request.get_json().keys())[0]}.json', 'w', encoding='utf-8') as file:
        json.dump(request.get_json().get(list(request.get_json().keys())[0]), file)
        file.close()
        return "Выполнено"


@app.route('/json', methods=['DELETE'])
def DELETE_JSON():
    os.remove(f'D:/BugsV2/back/JSON/{request.json["who"]}.json')
    return 'Удаленно'


app.run(debug=True)