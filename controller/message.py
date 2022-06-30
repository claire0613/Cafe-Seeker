from . import api
from model.models import City_ref, Message_like, db,Cafes,Message
from flask import *
from sqlalchemy.sql import func
import jwt,re,sys,os,datetime
sys.path.append("..")
from dotenv import load_dotenv
load_dotenv()

@api.route('/message', methods=['POST'])
def post_message(): 
	try:
		token_cookie = request.cookies.get('user_cookie')
		if token_cookie:
			user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
			user_id = user["id"]
			user_name=user['username']
			data=request.json
			cafe_id=data['cafe_id']
			message=data['msg_content']
			query_floor=Message.query.filter_by(cafe_id=cafe_id).all()
			floor=1
			if query_floor:
				floor=len(query_floor)+1
			msg_insert=Message(user_id=user_id,cafe_id=cafe_id,user_name=user_name,msg_content=message,floor=floor,create_time=datetime.datetime.now()+ datetime.timedelta(hours=8))
			msg_insert.insert()
			return jsonify({'data':True})
			
       
	except:
		return {"error": True, "message": "伺服器內部錯誤"}, 500

@api.route('/message',methods=['GET'])
def get_message():
	try:
		cafe_id=request.args.get('cafe_id')
		token_cookie = request.cookies.get('user_cookie')
		check_message=Message.query.order_by(Message.floor).filter_by(cafe_id=cafe_id).all()
		if check_message:
			check_message.as_dict()
		
		if token_cookie:
			user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
			user_id = user["id"]
			return jsonify({'data':check_message,'now_user':user_id})
		else:
			return jsonify({'data':check_message})
	
			

	except:
		return {"error": True, "message": "伺服器內部錯誤"}, 500


@api.route("/message", methods=["DELETE"])
def delete_message():
   try:
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie:
            
            data=request.json
            msg_id=data["msg_id"]
            Message.query.filter_by(msg_id=msg_id).first().delete()
	
            return jsonify({ "ok": True }) 
        else:
            return jsonify({ "error": True, "message": "未登入系統，拒絕存取" })
   except:
      return jsonify({ "error": True, "message": "伺服器內部錯誤" })
#收藏msg msg_like+1	
@api.route('/message/favor',methods=['POST'])
def post_msg_favor():
	try:
		cafe_id=request.args.get('cafe_id')
		token_cookie=request.cookies.get('user_cookie')
		if token_cookie:
			user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
			user_id = user["id"]
			data=request.json
			msg_id=data['msg_id']
			msg_like=Message_like(user_id=user_id,msg_id=msg_id)
			msg_like.insert()
			update=Message.query.filter_by(msg_id=msg_id).first()
			update.like_count=Message_like.query.filter_by(msg_id=msg_id).count()
			update.update()

			return jsonify({ "ok": True })
		else:
			return jsonify({ "error": True, "message": "未登入系統，拒絕存取" })
	except:
		return {"error": True, "message": "伺服器內部錯誤"}, 500
#收藏msg msg_like+1	
@api.route('/message/favor',methods=['DELETE'])
def delete_msg_favor():
	try:
		cafe_id=request.args.get('cafe_id')
		token_cookie=request.cookies.get('user_cookie')
		if token_cookie:
			user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
			user_id = user["id"]
			data=request.json
			msg_id=data['msg_id']
			Message_like.query.filter_by(msg_id=msg_id,user_id=user_id).first().delete()
		
			update=Message.query.filter_by(msg_id=msg_id).first()
			like_count=Message_like.query.filter_by(msg_id=msg_id).count()
			update.like_count=like_count
			update.update()

			return jsonify({ "ok": True })
		else:
			return jsonify({ "error": True, "message": "未登入系統，拒絕存取" })
	except:
		return {"error": True, "message": "伺服器內部錯誤"}, 500

@api.route('/message/favor',methods=['GET'])
def get_msg_favor():
	try:
		cafe_id=request.args.get('cafe_id')
		token_cookie=request.cookies.get('user_cookie')
		if token_cookie:
			user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
			user_id = user["id"]
			
			msg_id=request.args.get('msg_id')
			msg_like=Message_like.query.filter_by(msg_id=msg_id,user_id=user_id).first()
			#m已經存在msg_like table
			if msg_like:
					return jsonify({ "data": True })
			else:
				
					return jsonify({ "data": False })
		else:
			return jsonify({ "error": True, "message": "未登入系統，拒絕存取" })
	except:
		return {"error": True, "message": "伺服器內部錯誤"}, 500