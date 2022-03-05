from random import *

import mysql.connector as mysql
from flaskr.db import get_db
from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
bp = Blueprint('auth', __name__, url_prefix='/auth')

#URL/auth/registerにアクセスすると,registerview関数は入力用フォームを返す
@bp.route('/register', methods=('GET', 'POST'))
def register():
    #ユーザが値を入力した場合
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        ###なにこれ###
        db.execute('SELECT id FROM user WHERE username = %s', (username,))
        ###なにこれ###

        #usernameが空の場合
        if not username:
            error = 'Username is required.'
        #passwordが空の場合
        elif not password:
            error = 'Password is required.'
        #usernameが既に登録されているか
        elif db.fetchone() is not None:
            error = f"User {username} is already registered."

        #正しく入力された場合
        if error is None:
            #パスワードのハッシュ値をデータベースに保存
            db.execute(
                'INSERT INTO user (username, password) VALUES (%s, %s)',
                (username, generate_password_hash(password))
            )
            #クエリはデータを変更
            g.db.commit()
            #ログインページにリダイレクト
            return redirect(url_for('auth.login'))

        flash(error)
    #最初の画面 or エラーで再描画
    return render_template('auth/register.html')

#URL/auth/loginにアクセスすると起動
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        #ユーザの照合
        db.execute('SELECT * FROM user WHERE username = %s', (username,))
        user = db.fetchone()

        if user is None:
            error = 'Incorrect username.'
        #パスワードをハッシュ値の比較で照合
        elif not check_password_hash(user[2] , password):
            error = 'Incorrect password.'

        #ユーザIDの登録
        if error is None:
            session.clear()
            session['user_id'] = user[1]
            return redirect("https://sites.google.com/view/doshisha-isdl")

        flash(error)

    return render_template('auth/login.html')