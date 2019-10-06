from flask import session
from datetime import timedelta

#设置 session
@app.route('/set_session')
def set_session():
    session.permanent = True #设置session的持久化
    app.permanent_session_lifetime = timedelta(minutes=5)
    session['username'] = 'shixiaolou'
    return 'session success'

#获取 session
@app.route('/get_session')
def get_session():
    value = session.get('username')
    return 'the session value is {}'.format(value)

#移除 session
@app.route('/del_session')
def del_session():
    value = session.pop('username')
    return 'del session , value:{}'.format(value)

