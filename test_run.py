# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 15:40
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : test_run.py
# @Software: PyCharm


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=9999)

