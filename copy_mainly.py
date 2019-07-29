#encoding:gbk
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()
import flask
from flask import request
import geoip2.database
import pymysql
from flask import render_template
reader = geoip2.database.Reader('./GeoLite2-City.mmdb')#这里是获取ip地址归属地的数据库
mysql = pymysql.connect(host = 'localhost',user = 'root',password = 'root',db='ezywipe')
cursor = mysql.cursor()
app = flask.Flask(__name__,static_url_path='',template_folder='templates')
app.jinja_env.auto_reload = True #reload热加载flask，否则会一直卡在一个页面
app.config['TEMPLATES_AUTO_RELOAD'] = True
#下面是mysql的连接


@app.route('/retail',methods=['POST','GET'])
def shop():
    #此时就要读入数据库动态生成html
    #看看get值里面url传参的页面

    mysql.ping(reconnect=True)

    if request.method == 'GET':
        if request.args.get('pageindex') != None:
            obj={}
            pageindex = int(request.args.get("pageindex"))
            #print(pageindex)
            #如果pageindex=1 那么获取结果就是id : 1-10
            #如果pageindex =11 那么获取结果就是 id:11 - 20
            strran = str(pageindex)
            for i in range(pageindex+1,pageindex+9):
                strran += ","+str(i)
            cursor.execute('select id,name,price from retail where id IN('+strran+");")
            res = cursor.fetchall()
            #                     print(res)

            j = 0
            for i in res:
                j+=1
                obj['link'+str(j)] = '?goindex=' + str(i[0])
                obj['name'+str(j)] = str(i[1])
                obj['price'+str(j)] = str(i[2])
                obj['pic'+str(j)] = 'image_retail/'+str(i[0])+'[0].jpg'#这里说明了只能放jpg
            #规则如下:
            #封面图就是第一张图
            #一个产品有假设有四张图（但是这边硬性规定6张图
            #for example:
            #1[0].jpg , 1[1].jpg , 1[2].jpg , 1[3].jpg 其中1[0]为首页图
            #print(render_template('listing_retail.html',obj=obj))
            return render_template('listing.html',obj=obj)
        else:
            if request.args.get('goindex')!=None:
                obj = {}
                goindex = request.args.get('goindex')
                cursor.execute('select name,price,content from retail where id =' +goindex + ";")
                res = cursor.fetchall()
                #                            print (res , 'select name,price,content from retail where id =' +goindex + ";")
                obj['name'] = res[0][0]#获取name ，price，content等信息
                obj['Price'] = res[0][1]
                obj['content'] = res[0][2]
                for i in range(0,6):
                    obj['pic'+str(i)] = 'image_retail/'+goindex+'['+str(i)+'].jpg'
                return render_template('detail.html',obj=obj)
            # return render_template()
            else:
                return render_template('404.html')

@app.route('/foodservice',methods=['POST','GET'])
def foodservicing():
    #此时就要读入数据库动态生成html
    #看看get值里面url传参的页面
    mysql.ping(reconnect=True)
    if request.method == 'GET':
        if request.args.get('pageindex') != None:
            obj={}
            pageindex = int(request.args.get("pageindex"))
            #print(pageindex)
            #如果pageindex=1 那么获取结果就是id : 1-10
            #如果pageindex =11 那么获取结果就是 id:11 - 20
            strran = str(pageindex)
            for i in range(pageindex+1,pageindex+9):
                strran += ","+str(i)
            cursor.execute('select id,name,price from foodservice where id IN('+strran+");")
            res = cursor.fetchall()
            #                     print(res)

            j = 0
            for i in res:
                j+=1
                obj['link'+str(j)] = '?goindex=' + str(i[0])
                obj['name'+str(j)] = str(i[1])
                obj['price'+str(j)] = str(i[2])
                obj['pic'+str(j)] = 'image_foodservice/'+str(i[0])+'[0].jpg'#这里说明了只能放jpg
            #规则如下:
            #封面图就是第一张图
            #一个产品有假设有四张图（但是这边硬性规定6张图
            #for example:
            #1[0].jpg , 1[1].jpg , 1[2].jpg , 1[3].jpg 其中1[0]为首页图
            #print(render_template('listing_retail.html',obj=obj))
            return render_template('listing.html',obj=obj)
        else:
            if request.args.get('goindex')!=None:
                obj = {}
                goindex = request.args.get('goindex')
                cursor.execute('select name,price,content from foodservice where id =' +goindex + ";")
                res = cursor.fetchall()
                #                            print (res , 'select name,price,content from retail where id =' +goindex + ";")
                obj['name'] = res[0][0]#获取name ，price，content等信息
                obj['Price'] = res[0][1]
                obj['content'] = res[0][2]
                for i in range(0,6):
                    obj['pic'+str(i)] = 'image_foodservice/'+goindex+'['+str(i)+'].jpg'
                return render_template('detail.html',obj=obj)
            # return render_template()
            else:
                return render_template('404.html')


@app.route('/healthcare',methods=['POST','GET'])
def healthcare():
    #此时就要读入数据库动态生成html
    #看看get值里面url传参的页面
    mysql.ping(reconnect=True)
    tbname = 'healthcare'
    if request.method == 'GET':
        if request.args.get('pageindex') != None:
            obj={}
            pageindex = int(request.args.get("pageindex"))
            #print(pageindex)
            #如果pageindex=1 那么获取结果就是id : 1-10
            #如果pageindex =11 那么获取结果就是 id:11 - 20
            strran = str(pageindex)
            for i in range(pageindex+1,pageindex+9):
                strran += ","+str(i)
            cursor.execute('select id,name,price from '+tbname+' where id IN('+strran+");")
            res = cursor.fetchall()
            #                     print(res)

            j = 0
            for i in res:
                j+=1
                obj['link'+str(j)] = '?goindex=' + str(i[0])
                obj['name'+str(j)] = str(i[1])
                obj['price'+str(j)] = str(i[2])
                obj['pic'+str(j)] = 'image_'+tbname+'/'+str(i[0])+'[0].jpg'#这里说明了只能放jpg

            return render_template('listing.html',obj=obj)
        else:
            if request.args.get('goindex')!=None:
                obj = {}
                goindex = request.args.get('goindex')
                cursor.execute('select name,price,content from '+tbname+' where id =' +goindex + ";")
                res = cursor.fetchall()
                #                            print (res , 'select name,price,content from retail where id =' +goindex + ";")
                obj['name'] = res[0][0]#获取name ，price，content等信息
                obj['Price'] = res[0][1]
                obj['content'] = res[0][2]
                for i in range(0,6):
                    obj['pic'+str(i)] = 'image_'+tbname+'/'+goindex+'['+str(i)+'].jpg'
                return render_template('detail.html',obj=obj)
            # return render_template()
            else:
                return render_template('404.html')


@app.route('/beauty',methods=['POST','GET'])
def beauty():
    # 此时就要读入数据库动态生成html
    # 看看get值里面url传参的页面
    mysql.ping(reconnect=True)
    tbname = 'beauty'
    if request.method == 'GET':
        if request.args.get('pageindex') != None:
            obj = {}
            pageindex = int(request.args.get("pageindex"))
            # print(pageindex)
            # 如果pageindex=1 那么获取结果就是id : 1-10
            # 如果pageindex =11 那么获取结果就是 id:11 - 20
            strran = str(pageindex)
            for i in range(pageindex + 1, pageindex + 9):
                strran += "," + str(i)
            cursor.execute('select id,name,price from ' + tbname + ' where id IN(' + strran + ");")
            res = cursor.fetchall()

            j = 0
            for i in res:
                j += 1
                obj['link' + str(j)] = '?goindex=' + str(i[0])
                obj['name' + str(j)] = str(i[1])
                obj['price' + str(j)] = str(i[2])
                obj['pic' + str(j)] = 'image_' + tbname + '/' + str(i[0]) + '[0].jpg'  # 这里说明了只能放jpg

            return render_template('listing.html', obj=obj)
        else:
            if request.args.get('goindex') != None:
                obj = {}
                goindex = request.args.get('goindex')
                cursor.execute('select name,price,content from ' + tbname + ' where id =' + goindex + ";")
                res = cursor.fetchall()
                obj['name'] = res[0][0]  # 获取name ，price，content等信息
                obj['Price'] = res[0][1]
                obj['content'] = res[0][2]
                for i in range(0, 6):
                    obj['pic' + str(i)] = 'image_' + tbname + '/' + goindex + '[' + str(i) + '].jpg'
                return render_template('detail.html', obj=obj)
                # return render_template()
            else:
                return render_template('404.html')

@app.route('/cleaning',methods=['POST','GET'])
def cleaning():
    # 此时就要读入数据库动态生成html
    # 看看get值里面url传参的页面
    mysql.ping(reconnect=True)
    tbname = 'cleaning'
    if request.method == 'GET':
        if request.args.get('pageindex') != None:
            obj = {}
            pageindex = int(request.args.get("pageindex"))
            # print(pageindex)
            # 如果pageindex=1 那么获取结果就是id : 1-10
            # 如果pageindex =11 那么获取结果就是 id:11 - 20
            strran = str(pageindex)
            for i in range(pageindex + 1, pageindex + 9):
                strran += "," + str(i)
            cursor.execute('select id,name,price from ' + tbname + ' where id IN(' + strran + ");")
            res = cursor.fetchall()


            j = 0
            for i in res:
                j += 1
                obj['link' + str(j)] = '?goindex=' + str(i[0])
                obj['name' + str(j)] = str(i[1])
                obj['price' + str(j)] = str(i[2])
                obj['pic' + str(j)] = 'image_' + tbname + '/' + str(i[0]) + '[0].jpg'  # 这里说明了只能放jpg

            return render_template('listing.html', obj=obj)
        else:
            if request.args.get('goindex') != None:
                obj = {}
                goindex = request.args.get('goindex')
                cursor.execute('select name,price,content from ' + tbname + ' where id =' + goindex + ";")
                res = cursor.fetchall()
                obj['name'] = res[0][0]  # 获取name ，price，content等信息
                obj['Price'] = res[0][1]
                obj['content'] = res[0][2]
                for i in range(0, 6):
                    obj['pic' + str(i)] = 'image_' + tbname + '/' + goindex + '[' + str(i) + '].jpg'
                return render_template('detail.html', obj=obj)
                # return render_template()
            else:
                return render_template('404.html')



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
http_server = WSGIServer(('0.0.0.0', 8888), app)
http_server.serve_forever()
