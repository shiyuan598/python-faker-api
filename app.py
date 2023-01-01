# coding=utf8
import os
import requests
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示
# 全局允许跨域
CORS(app, supports_credentials=True)

BASE_URL_PREFIX = "/api"

# 用户
from routes.user import user
app.register_blueprint(user, url_prefix=BASE_URL_PREFIX + "/user")

# 图片
from routes.image import image
app.register_blueprint(image, url_prefix=BASE_URL_PREFIX + "/image")


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/mzzi')
def mzzi():
    url = "https://api.dujin.org/bing/1920.php"
    res = requests.get(url)
    response = make_response(res.content)
    response.headers["Content-Type"] = "application/octet-stream; charset=UTF-8"
    response.headers["Content-Disposition"] = "attachment;filename*=\
        utf-8''{}".format("2022-12-30") + '.png'
    return response


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 9005))
    app.run(host='localhost', port=port, debug=True)
