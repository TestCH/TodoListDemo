#coding:utf-8
from flask import Blueprint, url_for, render_template, request, redirect,flash
import tkMessageBox
from app import db
from models import Category
category_bp = Blueprint(
    'category',
    __name__,
    template_folder='../templates',
)

# category_list = ['11','222']

@category_bp.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
    )

@category_bp.route('/create', methods=['GET', 'POST'])
def cate_category():
    _form = request.form
    if request.method == 'POST':
            title = _form["category"]
            # print title
            if title:
                category_name1 = Category(title)
                # print category_name
                db.session.add(category_name1)
                db.session.commit()
            # category_list.append(title)
            # flash("add category successfully!")
            return redirect(url_for('category.get_category_list'))

    return render_template(
        'category.html',
        # category=category
   )

@category_bp.route('/add_category', methods=['GET'])
def add_category():
    return render_template(
        'category.html',
    )

@category_bp.route('/category_list', methods=['GET'])
def get_category_list():
    # new1 = db.session.query(Category) # 查询所有数据
    get_list = db.session.query(Category).all()  # 查询所有数据
    # print get_list
    # for new_list in get_list:
    #     content += '<li>' + str(new_list.category_id) + ', ' + new_list.category_name + '</li>'
    #     # content += '<li>' + new_list.category_name + '</li>'
    #     content += '</ul>'
    #     return content
    return render_template(
        'category_list.html',
        get_list=get_list,
    )

@category_bp.route('/category_list', methods=['POST'])
def del_category():
    data = request.form.getlist('customer_check')
    # print "data=" + data[0]
    if request.method == 'POST':
        for i in data:
            db.session.delete(Category.query.get(int(i)))
            db.session.commit()
        flash('删除成功！', 'success')
        get_category_list()
        return redirect(url_for('category.get_category_list'))
    return render_template(
        'category_list.html',
    )

'''
@category_bp.route('/add_category', methods=['GET'])
def update_category():
    data = request.form.getlist('customer_check')
    print "data=" + data[0]
    if request.method == 'GET':
        if len(data) > 1:
            tkMessageBox.showinfo(title='提示', message='只能选择一条数据编辑')
        else:
            category = Category.query.filter_by(category_id=int(data[0])).first()
            # db.session.add(admin)
            db.session.commit()
        # flash('顾客删除成功！', 'success')
        get_category_list()
        return redirect(url_for('category.get_category_list'))
    return render_template(
        'category.html',
    )
'''

