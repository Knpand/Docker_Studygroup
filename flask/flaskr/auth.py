from random import *
import os

from flask import Flask, jsonify, make_response, render_template, request
from flask_cors import CORS
from flask_restful import Api, Resource

import datetime
import time

import mysql.connector as mysql
from flaskr.db import get_db
from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        db.execute('SELECT * FROM user WHERE username = %s', (username,))
        user = db.fetchone()
        print(type(user[2]))
        print((user[2]))

        print(type(password))
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user[2].decode("utf-8") , password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user[1]
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        db.execute('SELECT id FROM user WHERE username = %s', (username,))
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        
        elif db.fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (%s, %s)',
                (username, generate_password_hash(password))
            )
            g.db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        get_db().execute('SELECT * FROM user WHERE id = %s', (user_id,))
        g.user = get_db.fetchone()
        
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))