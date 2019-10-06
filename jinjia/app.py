from flask import Flask, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
   
    return 'Hello World!'

@app.route('/test')
def test():
    app.logger.info(url_for('index'))
    app.logger.info(url_for('user_index',username='shiyanlou'))
    app.logger.info(url_for('show_post', post_id=1, _external=True))
    app.logger.info(url_for('show_post', post_id=2, q='python 03'))
    app.logger.info(url_for('show_post', post_id=2, q='python can'))
    app.logger.info(url_for('show_post', post_id=2, _anchor='a'))
    return '从主页重定向到test'

@app.route('/<username>')
def hello(username):
    if username == 'shixiaolou':            # 如果这个参数的值是 shixiaolou
        return 'Hello {}'.format(username)  # 就返回这个
    else:                                   # 否则
        url = url_for('index')
        app.logger.info(url)
        return redirect(url)

@app.route('/user/<username>')
def user_index(username):
    print('User_Agent:', request.header.get('User_Agent'))
    print('time:', request.args.get('time'))
    print('q:', request.args.get('q'))
    print('Q:', request.args.getlist('Q'))
    return 'hello {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)
@app.route('/courses/<name>')
def show_courses(name):
    return 'Courses:{}'.format(name)

@app.route('/register', methods=['GET', 'POST'])
def register():
    print('method:', request.method)
    print('name:', request.form. get('name'))
    print('password:', request.form.get('password'))
    print('hobbies:', request.form.getlist('hobbies'))
    print('age:', request.form.get('age', default=18))
    return 'registerd successfully!'


if __name__ == '__main__':
    app.run()


