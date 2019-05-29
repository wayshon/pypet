from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><head><title>hello word</title></dead><body><h1>hello word !</h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True)