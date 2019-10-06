from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    course = {
    'python': 'lou+ python',
    'java': 'java base',
    'bigdata': 'spark sql',
    'teacher': 'shixiaolou',
    'is_unique': False,
    'has_tag': True,
    'tags': ['c', 'c++','docker']
    }
    return render_template('index.html', course=course)

@app.route('/test')
def test():
    print(url_for('show_courses',name='java',_external=True))
    return redirect(url_for('index'))
    return 'this is test url' 

@app.route('/<username>')
def hello(uername):
    if username == 'shiyanlou':
        return 'Hello {}'.fromat(username)
    else:
        return redirect(url_for('index'))

@app.route('/user/<username>')
def user_index(username):
    return 'hello {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/courses/<name>')
def show_courses(name):
    return 'Courses:{}'.format(name)

@app.route('/httptest', methods=['GET', 'POST'])
def hahaha():
    # 判断请求方法
    if request.method == 'GET':
        # TODO print('xxxx')
        return 'It is a get request!'
    if request.method == 'POST':
        print('method:', request.mothod)
        print('t:', request.form.get('t'))
        print('q:', request.form.get('q'))
        print('Q:', request.form.getlist('Q'))
        return 'It is a post request!'

if __name__ == '__main__':
    app.run()
