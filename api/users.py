from . import api

from flask import Blueprint, session, request, jsonify, make_response

import os
from datetime import datetime, timedelta
import jwt,re,sys
import time
from model.models import Users,db
sys.path.append("..")
from dotenv import load_dotenv
load_dotenv()
from data.api_helper import updated_name_pwd


@api.route('/user', methods=['GET'])
def get_user():

    try:
        # 有登入
        token_cookie = request.cookies.get('user_cookie')
        if token_cookie:
            user = jwt.decode(token_cookie, os.getenv(
                "SECRET_KEY"), algorithms=['HS256'])
            data = {"data": user}
            return jsonify(data)
        
        #  token 超時 or 未登入
        else:
            data = {"data": None}
            return jsonify(data)

    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})

# 註冊
@api.route('/user', methods=['POST'])
def signup():
    try:
        data = request.json
        email = data['email']
        password = data['password']
        username=data['username']
        exist_user = Users.query.filter_by(email=email).first()
        if not exist_user:
           
            insert=Users(username=username,email=email,password=password)
            db.session.add(insert)
            db.session.commit()
           
            return jsonify({"ok": True})
            
        else:
            return jsonify({"error": True, "message": "註冊失敗，此Email已被註冊"})
        
    # 伺服器錯誤
    except:
        error = {
            "error": True,
            "message": "伺服器內部錯誤"
        }
        return jsonify(error), 500
   
#登入
@api.route('/user', methods=['PATCH'])
def login():
    try:
        data = request.json
        email = data['email']
        password = data['password']
        user_detail=Users.query.filter_by(email=email).first()
        
        # 登入成功(確認信箱是否存在)
        if user_detail:
            #驗證密碼
            verify_pwd= user_detail.verify_password(password)
            if verify_pwd:
                print(os.getenv("SECRET_KEY"))
                token = jwt.encode({
                    "id": user_detail.user_id,
                    "username": user_detail.username,
                    "email": user_detail.email,
                    "avatar":user_detail.avatar,
                    "exp": datetime.utcnow() + timedelta(days=1)
                }, os.getenv("SECRET_KEY"), algorithm='HS256')
                message = {"ok": True}
                
                response = make_response(jsonify(message))
                response.set_cookie(key='user_cookie', value=token)
                return response
            else:
             message = {
            "error": True,
            "message": "登入失敗，帳號或密碼輸入錯誤"
            }
            response = make_response(jsonify(message), 400)
            return response
    
               
        # 登入失敗
        else:
            message = {
                    "error": True,
                    "message": "請帳號不存在，請註冊帳號"
                }
            response = make_response(jsonify(message), 400)
            return response
        

    # 伺服器錯誤
    except:
        message = {
            "error": True,
            "message": "伺服器內部錯誤"
        }
        response = make_response(jsonify(message), 500)
        return response


@api.route('/user', methods=['DELETE'])
def singout():
    # 登出
    message = {"ok": True}
    response = make_response(jsonify(message))
    response.set_cookie(key='user_cookie', value='', expires=0)
    return response


# 修改會員姓名
@api.route('/user/update', methods=['POST'])
def updateuser():
    try:
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie :
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id=user["id"]
            data = request.json
            newname = data["newName"]
            result=updated_name_pwd(user_id=user_id, new_name=newname,pwd=None)
            if result:
                message = {"ok": True}
                response = make_response(jsonify(message))
                if newname:
                    
                    token = jwt.encode({
                    "id": user['id'],
                    "username": newname,
                    "email": user['email'],
                    "avatar":user["avatar"],
                    "exp": datetime.utcnow() + timedelta(days=1)
                    }, os.getenv("SECRET_KEY"), algorithm='HS256')
                    response.set_cookie(key='user_cookie', value=token)
                    return response
                else:
                    return response
            
        else:
            return jsonify({"error": True,"message":"未登入"})
    # 伺服器錯誤
    except:
        message = {
            "error": True,
            "message": "伺服器內部錯誤"
        }
        response = make_response(jsonify(message), 500)
        return response

