from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return 'this is the test'

@app.route('/user/<username>')
def user_index(username):
    return render_template('user_index.html', username=username)

@app.route('/courses/<coursesname>')
def show_courses(coursesname):
    return render_template('courses.html', coursesname=coursesname)

@app.route('/httptest', methods=['get', 'post'])
def hahaha():
    # 判断请求方法
    if request.method == 'GET':
        # TODO print('xxxx')
        return 'It is a get request!'
    if request.method == 'POST':
        # TODO print('xxxx')
        return 'It is a post request!'

if __name__ == '__main__':
    app.run()

