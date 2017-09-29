#coding:utf-8
from datetime import datetime
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class Category(db.Model):
    """定义数据模型"""
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(120), unique=True)

    def __init__(self, category_name):
        # self.category_id = category_id
        self.category_name = category_name

    # def getlist(self):
    #     getcategory = Category.query.all()
    #     return getcategory

        # 重构__repr__
    def __repr__(self):
        return "(Category %s)" % (self.category_name)

class Todolist(db.Model):
    """定义数据模型"""
    __tablename__ = 'todolist'
    todolist_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.category_id"))
    todolist_title = db.Column(db.String(30))
    todolist_content = db.Column(db.String(200))
    todolist_priority = db.Column(db.String(4))
    todolist_create_time = db.Column(db.DateTime)
    category = db.relationship("Category",backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, category_id,todolist_title,todolist_content,todolist_priority,todolist_create_time=None):
        # self.todolist_id = todolist_id
        self.todolist_title = todolist_title
        self.category_id = category_id
        self.todolist_content = todolist_content
        self.todolist_priority = todolist_priority
        if todolist_create_time is None:
            pub_date = datetime.utcnow()
        self.todolist_create_time = pub_date
        # self.category = category

    # 重构__repr__
    def __repr__(self):
        return '<Todolist %r>' % self.todolist_title


db.create_all()