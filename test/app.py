#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    teacher = {
    'name': 'Aiden',
    'email': 'luojin@qq.com'
    }

    course = {
    'name': 'Python Basic',
    'teacher': teacher
    }
    return render_template('index.html', course=course)

    