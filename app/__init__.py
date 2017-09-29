# -*- coding: utf-8 -*-


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from config import basedir

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
# or
app.secret_key = '123456'
# or
app.config.update(SECRET_KEY='123456')

app.config.from_object('config')  # 载入配置文件

db = SQLAlchemy(app)  # 初始化 db 对象

# from app import views, models    # 引用视图和模型
import views, models
