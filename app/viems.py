#!/usr/bin/env python3
# coding=utf-8

from flask import Blueprint
from flask import render_template

blue = Blueprint("viems", __name__)


@blue.route('/home/', methods=['GET'])
def home():
    return render_template("Home.html")


