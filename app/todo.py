#coding:utf-8
from flask import Blueprint, url_for, render_template, request, redirect,flash
import tkMessageBox
from app import db
from models import Category
from models import Todolist
todo_bp = Blueprint(
    'addtodo',
    __name__,
    template_folder='../templates',
)
@todo_bp.route('/todo', methods=['GET'])
def todo():
    import views
    category_list = db.session.query(Category).all()
    # print category_list
    return render_template(
        'addtodo.html',
        category_list=category_list,
    )

#添加代办事
@todo_bp.route('/add_todo', methods=['GET', 'POST'])
def add_todo():
    _form = request.form
    if request.method == 'POST':
        category = _form["category"]
        # print category
        title = _form["title"]
        # print title
        content = _form["content"]
        # print content
        priority = _form["priority"]
        # print priority
        if title:
            addtodo = Todolist(category,title,content,priority)
            # print addtodo
            # print category_name
            db.session.add(addtodo)
            db.session.commit()
        # category_list.append(title)
        # flash("add category successfully!")
        return redirect(url_for('addtodo.get_todo_list'))

    return render_template(
        'addtodo.html',
   )
#获取todolist
@todo_bp.route('/get_todo_list', methods=['GET'])
def get_todo_list():
    get_list = db.session.query(Todolist).all()  # 查询所有数据
    print get_list
    # for new_list in get_list:
    #     content += '<li>' + str(new_list.category_id) + ', ' + new_list.category_name + '</li>'
    #     # content += '<li>' + new_list.category_name + '</li>'
    #     content += '</ul>'
    #     return content
    return render_template(
        'todo_list.html',
        get_list=get_list,
        page=len(get_list) / 5 + 1,
    )

@todo_bp.route('/get_todo_list', methods=['POST'])
def del_todo():
    data = request.form.getlist('todo_checkbox')
    # print "data=" + data[0]
    if request.method == 'POST':
        for i in data:
            db.session.delete(Todolist.query.get(int(i)))
            db.session.commit()
        flash('删除成功！', 'success')
        get_todo_list()
        return redirect(url_for('addtodo.get_todo_list'))
    return render_template(
        'todo_list.html',
    )