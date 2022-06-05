from . import api
from model.models import City_ref, db,Cafes,Score_rec,Update_detail
from flask import *
from sqlalchemy.sql import func
import jwt,re,sys,os
sys.path.append("..")
from dotenv import load_dotenv
load_dotenv()

#insert shop_detail updatedform
@api.route('/shop_detail/<cafe_id>', methods=['POST'])
def post_detail(cafe_id):
    try:
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            data = request.json
            single_selling,dessert_selling,meal_selling=data['single_selling'],data['dessert_selling'],data['meal_selling']
            limited_time,socket,staning_tables,music=data['limited_time'],data['socket'],data['staning_tables'],data['music']
            outdoor_seating,cash_only,animals=data['outdoor_seating'],data['cash_only'],data['animals']
            open_hours,website,mrt,address,phone=data['open_hours'],data['website'],data['mrt'],data['address'],data['phone']
            update=Update_detail(user_id=user_id,cafe_id=cafe_id,single_selling=single_selling,\
                    dessert_selling=dessert_selling,meal_selling=meal_selling,limited_time=limited_time,socket=socket,\
                    staning_tables=staning_tables,music=music,outdoor_seating=outdoor_seating,cash_only=cash_only,animals=animals,\
                    open_hours=open_hours,website=website,transport=mrt,address=address,phone=phone)
            
            
            update.insert()
            order=db.session.query(Update_detail).order_by(Update_detail.create_time.desc()).filter_by(user_id=user_id,cafe_id=cafe_id).first()
          
            return jsonify({'data':True,'number':order.upd_id})
            
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})
#GET shop_detail updatedform    
@api.route('/shop_detail/<upd_id>', methods=['GET'])
def get_rating(upd_id):
    try:
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            scr_id=scr_id
            order=Update_detail.query.filter_by(upd_id=upd_id,user_id=user_id).first()
            result={
            'upd_id':order.upd_id,'cafe_id':order.cafe_id,
            'single_selling':order.single_selling,'dessert_selling':order.dessert_selling,'meal_selling':order.meal_selling,
            'limited_time':order.limited_time,'socket':order.socket,'drinks':order.drinks,'staning_tables':order.staning_tables,
            'music':order.music,'outdoor_seating':order.outdoor_seating,'cash_only':order.cash_only,'animals':order.animals,
            'open_hours':order.open_hours,'website':order.website,'mrt':order.transport,'address':order.address,'phone':order.phone,'status':order.status
            }
            
        return jsonify({'data':result})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})
    
#修改shop_detail表單   
@api.route('/shop_detail/<upd_id>', methods=['PATCH'])
def update_detail_form(upd_id):
    try:
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            scr_id=scr_id
            history=Update_detail.query.filter_by(upd_id=upd_id,user_id=user_id,status=False).first()
            data = request.json
            history.single_selling=data['single_selling']
            history.dessert_selling=data['dessert_selling']
            history.meal_selling=data['meal_selling']
            history.limited_time=data['limited_time']
            history.socket=data['socket']
            history.staning_tables=data['staning_tables']
            history.outdoor_seating=data['outdoor_seating']
            history.cash_only=data['cash_only']
            history.animals=data['animals']
            history.open_hours=data['open_hours']
            history.music=data['music']
            history.update()


            

        return jsonify({'data':True})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})
@api.route('/shop_detail/shop/<scr_id>', methods=['PATCH'])
def update_to_cafe(upd_id):
    try:
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            history=Update_detail.query.filter_by(upd_id=upd_id,status=False).first()
            cafe=Cafes.query.filter_by(id=history.cafe_id).first()
            cafe.single_selling=history.single_selling
            cafe.dessert_selling=history.dessert_selling
            cafe.meal_selling=history.meal_selling
            cafe.limited_time=history.limited_time
            cafe.socket=history.socket
            cafe.staning_tables=history.staning_tables
            cafe.outdoor_seating=history.outdoor_seating
            cafe.cash_only=history.cash_only
            cafe.staning_tables=history.staning_tables
            cafe.animals=history.animals
            cafe.open_hours=history.open_hours
            cafe.music=history.music
            cafe.update()
            history.status=True
            history.update()
        return jsonify({'data':True})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})

        
        