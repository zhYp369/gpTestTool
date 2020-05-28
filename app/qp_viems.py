from flask import Blueprint, request
from flask import render_template
from page.qp.cdk import get_result_dict as cdk_result
from page.qp.loyalty import get_result_dict as loyalty_result


blue = Blueprint("qp_viems", __name__)


@blue.route('/qp/cdk', methods=['GET', 'POST'])
def cdk():

    method = request.method

    if method == "GET":
        html = render_template("qp/qp_cdk.html")

    elif method == 'POST':
        req_url = request.form["req_url"]
        req_method = request.form["req_method"]
        glo_date = request.form["Global_data"]
        req_date = request.form["request_data"]
        context = cdk_result(req_url, req_method, glo_date, req_date)
        html = render_template("qp/qp_cdk.html", **context)

    else:
        html = "<h1>请求方式错误</h1>"
    return html


@blue.route('/qp/loyalty', methods=['GET', 'POST'])
def loyalty():

    method = request.method

    if method == "GET":
        html = render_template("qp/qp_loyalty.html")

    elif method == 'POST':
        req_url = request.form["req_url"]
        req_method = request.form["req_method"]
        glo_date = request.form["Global_data"]
        req_date = request.form["request_data"]
        context = loyalty_result(req_url, req_method, glo_date, req_date)
        html = render_template("qp/qp_loyalty.html", **context)

    else:
        html = "<h1>请求方式错误</h1>"
    return html




