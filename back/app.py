from flask import Flask, request, jsonify
from flask_restful import Api
app = Flask(__name__)
api = Api(app)
import SQL

@app.route('/Bugs', methods=['GET'])
def GET():
    return SQL.Db().select_all_user()

@app.route('/Bugs', methods=['POST'])
def POST(): #Не ебу как, но оно работает, хоть и выдает ошибку 500. Главное работает.
    SQL.Db().insert_user(request.json['fullname'], request.json['date_time'], request.json['pose'], request.json['curreet_pose'], request.json['offical_pose'], request.json['email'], request.json['data_work'], request.json['region'], request.json['phone'], request.json['work_time'], request.json['spec'])

@app.route('/Bugs', methods=['DELETE'])
def DELETE():
    SQL.Db().delete_user(request.json['id'])
    print(request.json['id'])

app.run(debug=True)