# coding=utf8
import requests
import datetime
from flask import Blueprint, request, jsonify, make_response

image = Blueprint("image", __name__)

@image.route('/', methods=["GET"])
def get_image_by_type():
    try:
        download = request.args.get("download", False)
        type = int(request.args.get("type", 0))
        category = "{dongman,fengjing,biying,meinv}"
        if type == 0:
            category = "{dongman,fengjing,biying,meinv}"
        elif type == 1:
            category = "dongman"
        elif type == 2:
            category = "fengjing"
        elif type == 3:
            category = "biying"
        elif type == 4:
            category = "meinv"
        url = "https://tuapi.eees.cc/api.php?type=302&category={}".format(category)
        res = requests.get(url)
        print("url:\n", url)
        response = make_response(res.content)
        if download == True:
            response.headers["Content-Type"] = "application/octet-stream; charset=UTF-8"
            response.headers["Content-Disposition"] = "attachment;filename*=\
                utf-8''{}".format(int(datetime.datetime.now().timestamp())) + '.png'
        else:
            response.headers["Content-Type"] = "image/JPEG; charset=UTF-8"
            response.headers["Content-Disposition"] = "inline;"
        return response
    except Exception as e:
          return jsonify({"code": 1, "msg": str(e)})
      
@image.route('/meta', methods=["GET"])
def meta():
    try:
        result = {
            "美女": "https://cdn.seovx.com/?mom=302",
            "动漫": "https://cdn.seovx.com/d/?mom=302",
            "古风": "https://cdn.seovx.com/ha/?mom=302",
            "Bing当日美图": "https://api.dujin.org/bing/1920.php",
            "分类图片": "https://tuapi.eees.cc/api.php?category={dongman,fengjing,biying,meinv}",
            "随机图片": "https://picsum.photos/{width}/{height}"
        }
        return jsonify({"code": 0, "data": result, "msg": "成功"})
    except Exception as e:
        return jsonify({"code": 1, "msg": str(e)})
