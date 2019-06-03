import os
from flask import Flask, session, redirect, url_for, escape, request, render_template, json,jsonify
app = Flask(__name__)

#设置编码
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    with open(os.path.join(app.root_path, 'static/html/index.html'), 'r') as f:
        return f.read()

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