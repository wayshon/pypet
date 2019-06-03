import os
from flask import Flask, session, redirect, url_for, escape, request, render_template, json,jsonify
from config.mongo import MONGODB_SETTINGS
from pymongo import MongoClient
import urllib.parse

app = Flask(__name__)

dbname = MONGODB_SETTINGS['db']
host = MONGODB_SETTINGS['host']
port = MONGODB_SETTINGS['port']
username = MONGODB_SETTINGS['username']
password = MONGODB_SETTINGS['password']

client = MongoClient(host=host,port=port,username=username,password=password,authSource=dbname,authMechanism='SCRAM-SHA-1')

db = client[dbname]
collection = db['pet']


#设置编码
app.config['JSON_AS_ASCII'] = False

def listItemHandle(item):
    tempId = str(item['_id'])
    item.pop('_id')
    item['id'] = tempId
    return item

@app.route('/')
def index():
    with open(os.path.join(app.root_path, 'static/html/index.html'), 'r') as f:
        return f.read()
        
@app.route('/list')
def pet_list():
    results = collection.find()
    array = [listItemHandle(item) for item in results]
    print(array)
    return jsonify({
        "status": 0,
        "msg": "ok",
        "data": array
    })

@app.route('/detail')
def detail():
    query = request.args.get('q', '')
    return render_template('detail.html', **{
        "name": "hulk",
        "query": query
    })

@app.route('/post', methods=['POST'])
def post():
    bdata = request.get_data()
    data = json.loads(bdata)
    print(data)
    return jsonify({
        "status": 0,
        "msg": "ojbk!",
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True)