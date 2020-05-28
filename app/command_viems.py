#!/usr/bin/env python3
# coding=utf-8

from flask import Blueprint
from flask import render_template
from flask import request
from page.command.edit_command import edit_command, edit_testfile

blue = Blueprint("command_viems", __name__)


@blue.route('/log/command', methods=['GET',"POST"])
def command():
    html = ""
    method = request.method
    context = edit_command()
    if method == "GET":
        html = render_template("command/command.html", context=context)
    elif method == "POST":
        html = render_template("command/command.html", context=context)
    return html


@blue.route('/log/testfile', methods=['GET',"POST"])
def testfile():
    html = ""
    method = request.method
    context = edit_testfile()
    if method == "GET":
        html = render_template("command/testfile.html", context=context)
    elif method == "POST":
        html = render_template("command/testfile.html", context=context)
    return html








