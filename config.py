# -*- coding: utf-8 -*-
from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///e:/db/category.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
