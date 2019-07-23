import flask
from flask import request
app = flask.Flask(__name__,static_url_path='')
@app.route('/')
def login():
       print(request.remote_addr)
       return app.send_static_file('index.html')
app.run(host='0.0.0.0',port=8888)
