import mysql.connector as mysql

import click
from flask import current_app, g
from flask.cli import with_appcontext

user_name = "light"
password = "light"
host = "database"  # docker-composeで定義したMySQLのサービス名
database_name = "db"

def get_db():
    if 'db' not in g:
        g.db =  mysql.connect(
            host="database",
            user="light",
            passwd="light",
            port=3306,
            database="db"
        )
        cur = g.db.cursor()

    return cur


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        # print(f.read().decode('utf8'))
        db.execute(f.read().decode('utf8'))

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')