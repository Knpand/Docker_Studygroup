import mysql.connector as mysql

import click
from flask import current_app, g
from flask.cli import with_appcontext

user_name = "light"
password = "light"
host = "database"  # docker-composeで定義したMySQLのサービス名
database_name = "db"

def get_db():
    #接続
    if 'db' not in g:
        #コネクションの作成
        g.db =  mysql.connect(
            host="database",#Dockerのコンテナ名と一致
            user="light",
            passwd="light",
            port=3306,
            database="db"
        )
        #DB操作用にカーソルを作成（テーブルの作成）
        cur = g.db.cursor()

    return cur

#コネクションがあればを閉じる
def close_db(e=None):
    #'db'を持てばConnectionオブジェクトを返し、持たなければ'None'を返す
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    #コネクションの接続
    db = get_db()

    # f(schema.sql)読込('r'モード) → 'utf-8'でデコード → dbに書き込み
    #open_resource()はflaskrからの相対pathで指定されたファイルを開く
    with current_app.open_resource('schema.sql') as f:
        # print(f.read().decode('utf8'))
        db.execute(f.read().decode('utf8'))

#init_db関数を呼び出すコマンドラインのコマンドinit-dbを定義し，成功メッセージを表示
@click.command('init-db')
@with_appcontext
def init_db_command():
    #既存のデータを削除し，新しいテーブルを作成
    init_db()
    click.echo('Initialized the database.')

#アプリケーションへの登録
def init_app(app):
    #レスポンスを返した後「close_db()」を呼び出す
    app.teardown_appcontext(close_db)
    #flaskから呼び出すコマンド作成（_init_.py_）
    app.cli.add_command(init_db_command)