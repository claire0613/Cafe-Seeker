from . import api
from model.models import City_ref, db,Cafes,Cafes_like
from flask import *
from sqlalchemy.sql import func
import jwt,re,sys,os
sys.path.append("..")
from dotenv import load_dotenv
load_dotenv()




#收藏cafe 	
@api.route('/shop/favor',methods=['POST'])
def post_cafe_favor():
    try:
        data=request.json
        cafe_id=data['cafe_id']
       
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            cafe_like=Cafes_like(user_id=user_id,cafe_id=cafe_id)
            cafe_like.insert()
           
            return jsonify({ "ok": True })
        else:
            return jsonify({ "error": True, "message": "未登入系統，拒絕存取" })
    except:
        return {"error": True, "message": "伺服器內部錯誤"}, 500
#收藏msg msg_like+1	
@api.route('/shop/favor',methods=['DELETE'])
def delete_cafe_favor():
    try:
        data=request.json
        cafe_id=data['cafe_id']
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            data=request.json
            Cafes_like.query.filter_by(cafe_id=cafe_id,user_id=user_id).first().delete()
            return jsonify({ "ok": True })
        else:
            return jsonify({ "error": True, "message": "未登入系統，拒絕存取" })
    except:
        return {"error": True, "message": "伺服器內部錯誤"}, 500

@api.route('/shop/favor',methods=['GET'])
def get_cafe_favor():
    try:
     
        cafe_id=request.args.get('cafe_id')
        token_cookie=request.cookies.get('user_cookie')
        count=Cafes_like.query.filter_by(cafe_id=cafe_id).count()
        is_favor=False
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
        
            is_favor=Cafes_like.query.filter_by(cafe_id=cafe_id,user_id=user_id).first()
            if is_favor:
                
                is_favor=True
      
                
        return jsonify({ "data": True, "count": count,'is_favor':is_favor})
        
    except:
        return {"error": True, "message": "伺服器內部錯誤"}, 500
    


