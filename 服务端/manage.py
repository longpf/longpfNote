from ast import And
from flask import Flask, jsonify
from requests import Response
import sql
import json


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello longpf"

@app.route("/deviceId=<string:deviceId>")
def search(deviceId):
    succ,levels,lastCommit = sql.search(deviceId=deviceId)
    res = ""
    error = 0
    if succ:
        res += "查找到了deviceId为%s的用户" % deviceId
    else:
        res += "未查找到了deviceId为%s的用户" % deviceId
        error = 1 
    if levels != None:
        res += ", 最高到达%d关卡" % levels
    if lastCommit != None:
        res += ", 最后提交的时间为 %d" % lastCommit
    t = {
        'error':error,
        'msg': res
    }
    return jsonify(t)

@app.route("/update/<string:deviceId>/<int:levels>")
def update(deviceId,levels):
    res = sql.update(deviceId=deviceId,levels=levels)
    t = {}
    if res:
        t = {
            'error':0,
            'msg': '设置成功'
        }
    else:
        t = {
            'error': 1,
            'msg':'更新失败'
        }
    return jsonify(t)

@app.route("/longpf")
def moco():
    return "Hello longpf123"

@app.route("/id=<int:id>")
def api(id):
    reqeust_id = int(id)
    res = "hello world"
    return res
	

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=6000)
    app.run(port=50001)
