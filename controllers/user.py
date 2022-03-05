
"""
user controller
for login/register and logout
"""
from pythonMVC.core.DB import engine, Session, Base
from pythonMVC.models.user import User
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import bcrypt


#controller for business logic
class user:        
    
    def listAll():
        if not session.get('user_id'):
            return redirect(url_for('login'))
        DBsession = Session()
        users = DBsession.query(User).all()
        return render_template('user_list.html', users = users)
    
    def login():
        DBsession = Session()
        error = None
        if request.method == 'POST':            
            user = DBsession.query(User).filter(User.username == request.form['username']).first()
            if user != None and bcrypt.checkpw(request.form['password'].encode(),user.password_hash.encode()):
                session['user_id'] = user.user_id
                return redirect(url_for('root'))
            else:
                error="Problem logging in!"
        return render_template('login.html', error=error)

    def logout():
            session.pop('user_id', None)
            flash('You were logged out')
            return redirect(url_for('root'))

    def register():
        DBsession = Session()
        error = None
        if request.method == 'POST':            
            user = DBsession.query(User).filter(User.username == request.form['username']).first()
            if user != None:
                error="This username already exists. Select another one."
            elif request.form['password'] != request.form['password_confirm']:
                error="Passwords do not match."
            else:
                DBsession = Session()
                newUser = User(request.form['username'], request.form['password'])
                # persists data
                DBsession.add(newUser)
                # commit and close session
                DBsession.commit()
                DBsession.close()                
                return redirect(url_for('login'))
        return render_template('register.html', error=error)
    