from pythonMVC.core.DB import engine, Session, Base

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from pythonMVC.controllers.user import user

app = Flask(__name__)
app.config.from_object(__name__) # load config from this file

app.secret_key = 'super secret key'

@app.route("/")
def root():
    return user.listAll()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return user.login()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return user.register()

@app.route('/logout')
def logout():
    return user.logout()