import flask
from flask import request
import geoip2.database
reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
app = flask.Flask(__name__,static_url_path='')
@app.route('/')
def login():
       print(request.remote_addr)
       try:
              country = reader.city(request.remote_addr).country.names["zh-CN"]
       except:
              return app.send_static_file('index.html')
       if country == '中国':
              return app.send_static_file('indexchina.html')
       else:
              return app.send_static_file('index.html')
app.run(host='0.0.0.0',port=8888)
