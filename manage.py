#!/usr/bin/env python3
# coding=utf-8

from flask import Flask
from flask_script import Manager
from app.viems import blue as home
from app.qp_viems import blue as qp
from app.zdyt_viems import blue as zdyt
from app.tool_viems import blue as tool
from app.command_viems import blue as command
# import logging
# from utils.edit_os.edit_path import *
# from utils.edit_date.edit_num import get_time

app = Flask(__name__)
manage = Manager(app=app)
app.register_blueprint(blueprint=home)
app.register_blueprint(blueprint=qp)
app.register_blueprint(blueprint=zdyt)
app.register_blueprint(blueprint=tool)
app.register_blueprint(blueprint=command)

# logfilename = "catalina.%s.log" % get_time('%Y-%m-%d')
# # project_path = os.path.dirname(os.path.abspath(__file__))
# project_path = r'/opt/var/logs/test_tool'
# log_file = os.path.join(project_path, logfilename)
#
# logging.basicConfig(filename=log_file, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    manage.run()








