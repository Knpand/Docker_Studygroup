from flask import Flask, render_template, jsonify, request, make_response
from flask_restful import Api, Resource
from flask_cors import CORS
from random import *
from isbn import RAKUTENAPI
from sql import sql_arg
RA = RAKUTENAPI()
SQLARG = sql_arg()
#FlaskとVueの連携
app = Flask(__name__, static_folder='../../frontend/app/dist/static', template_folder='../../frontend/app/dist')
#日本語
app.config['JSON_AS_ASCII'] = False
#CORS=Ajaxで安全に通信するための規約
api = Api(app)
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/post_isbn', methods=['POST'])
def postdata():
    # global isbns
    message = ['貸出完了！！']
    # postしてきたデータを取得
    id = request.form['id']
    tempisbn = request.form['tempisbn']
    isbns = request.form['isbns'].split(',')
    # 全てのデータを格納
    isbns.append(tempisbn)
    print(isbns)
    add_book(isbns)
    result_data = {
        'message': message
    }
    return jsonify(result_data)

@app.route('/user_name', methods=['POST'])
def username():
    message = ['ログイン完了']
    email = request.form['email']
    id = get_userid(email)

    # 全てのデータを格納
    username= get_username(id)
    result_data = {
        'message': message,
        'username': username
    }
    return jsonify(result_data)

@app.route('/user_info', methods=['POST'])
def userinfo():
    message = []
    # email = request.form['email']
    # id = get_userid(email)
    id = request.form['user_id']

    ren_books,his_books = get_userinfo(id)

    user_info = {
        'ren_books': ren_books,
        'his_books': his_books
    }
    return jsonify(user_info)
    
@app.route('/userid', methods=['POST'])
def user_id():
    email = request.form['email']
    id = get_userid(email)
    message = ['貸出完了']
    result_data = {
        'message': message,

    }
    return jsonify(result_data)

@app.route('/rental_register', methods=['POST'])
def rentbook():
    message = ['success']
    email = request.form['user_id']
    # id = get_userid(email)
    tempisbn = request.form['tempisbn']
    isbns = request.form['isbns'].split(',')
    if tempisbn !='':
        isbns.append(tempisbn)
    # 全てのデータを格納
    result = rent(id,isbns)
    result_data = {
        'message': message,

    }
    return jsonify(result_data)

@app.route('/return_register', methods=['POST'])
def returnbook():
    message = ['success']
    # email = request.form['email']
    id = request.form['user_id']
    # id = get_userid(email)
    # tempisbn = request.form['tempisbn']
    # isbn = request.form['isbn'].split(',')
    isbn = request.form['isbn']
    # isbns =[]
    # if tempisbn != '':
            # isbns.append(tempisbn)

    if(isbn != ''):
        isbn.append(isbn)
    else:
        message = "error"

    # 全てのデータを格納
    if len(isbn) != 0:
        result = returnbooks(id,isbn)
        print(result)
    result_data = {
        'message': message,

    }
    return jsonify(result_data)

@app.route('/book_list', methods=['POST'])
def getallbooks():
    booklist = getbooks()
    # print(booklist)
    # result_data = {
    #     'booklist': booklist,
    # }
    return jsonify(booklist)

@app.route('/bookinfo', methods=['POST'])
def getbookinfo():
    isbn = request.form['isbn']
    booktitle,bookauthor,bookpublisher = bookinfo(isbn)
    # print(booklist)
    book_info = {
        'title': booktitle,
        'author':bookauthor,
        'publisher':bookpublisher
    }
    return jsonify(book_info)


def add_book(isbns):
    print("a")
    for isbn in isbns:
       book_info=RA.get_book_info_by_isbn(isbn)
       print(book_info)
       SQLARG.insert_book_data(values=book_info)

def get_username(id):
    username = SQLARG.get_name(id)
    print(username)
    return username

def get_userid(email):
    id = SQLARG.get_userid(email)
    print(id)
    return id

def get_userinfo(id):
    username = SQLARG.get_userinfo(id)
    print(username)
    return username

def bookinfo(isbn):
    booktitle,bookauthor,bookpublisher = SQLARG.get_bookinfo(isbn)
    return booktitle,bookauthor,bookpublisher

def rent(id,isbns):
    print("b")
    for isbn in isbns:
        SQLARG.rent_book(id, isbn)

def returnbooks(id,isbns):
    print("b")
    for isbn in isbns:
        SQLARG.return_book(id,isbn)

def getbooks():
    return SQLARG.get_all_book_data()



if __name__ == '__main__':
    app.run(host='0.0.0.0')
