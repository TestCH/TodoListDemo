#coding:utf-8
from flask import Flask, render_template
from app.views import category_bp
from app.todo import todo_bp
from app import app


#注册蓝图
app.register_blueprint(category_bp)
app.register_blueprint(todo_bp)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5200, debug=True)