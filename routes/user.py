# coding=utf8
from faker import Faker
from flask import Blueprint, request, jsonify, make_response

fake = Faker(locale="zh_CN")
user = Blueprint("user", __name__)

@user.route('/', methods=["GET"])
def profile():
    try:
        result = [fake.simple_profile() for item in range(10)]
        return jsonify({"code": 0, "data": result, "pagination": {"total": 33, "current": 1, "pageSize": 10}, "msg": "成功"})
    except Exception as e:
          return jsonify({"code": 1, "msg": str(e)})
      
@user.route('/name', methods=["GET"])
def name():
    try:
        count = int(request.args.get("count", 10))
        result = [fake.name() for item in range(count)]
        return jsonify({"code": 0, "data": result, "msg": "成功"})
    except Exception as e:
          return jsonify({"code": 1, "msg": str(e)})
      
@user.route('/email', methods=["GET"])
def email():
    try:
        count = int(request.args.get("count", 10))
        result = [fake.free_email() for item in range(count)]
        return jsonify({"code": 0, "data": result, "msg": "成功"})
    except Exception as e:
          return jsonify({"code": 1, "msg": str(e)})
      
@user.route('/telephone', methods=["GET"])
def telephone():
    try:
        count = int(request.args.get("count", 10))
        result = [fake.phone_number() for item in range(count)]
        return jsonify({"code": 0, "data": result, "msg": "成功"})
    except Exception as e:
          return jsonify({"code": 1, "msg": str(e)})
      
@user.route('/ssn', methods=["GET"])
def ssn():
    try:
        count = int(request.args.get("count", 10))
        result = [fake.ssn() for item in range(count)]
        return jsonify({"code": 0, "data": result, "msg": "成功"})
    except Exception as e:
          return jsonify({"code": 1, "msg": str(e)})
      
@user.route('/job', methods=["GET"])
def job():
    try:
        count = int(request.args.get("count", 10))
        result = [fake.job() for item in range(count)]
        return jsonify({"code": 0, "data": result, "msg": "成功"})
    except Exception as e:
          return jsonify({"code": 1, "msg": str(e)})
      
@user.route('/address', methods=["GET"])
def address():
    try:
        count = int(request.args.get("count", 10))
        result = [fake.address() for item in range(count)]
        return jsonify({"code": 0, "data": result, "msg": "成功"})
    except Exception as e:
          return jsonify({"code": 1, "msg": str(e)})