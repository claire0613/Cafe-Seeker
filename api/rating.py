from . import api
from model.models import City_ref, db,Cafes,Score_rec
from flask import *
from sqlalchemy.sql import func
import jwt,re,sys,os
sys.path.append("..")
from dotenv import load_dotenv
load_dotenv()
def rating_avg(data):
    result_list=[]
    for i in data:
        if i and i !=0.0:
            result_list.append(i)
    if result_list :
        return round(sum(result_list)/len(result_list),1)
    return 0.0
    
#insert rating 分數
@api.route('/rating/<cafe_id>', methods=['POST'])
def post_rating(cafe_id):
    try:
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            data = request.json
            price_rating,wifi_rating,vaca_rating=data['price'],data['wifi'],data['vacancy']
            quiet_rating,comfort_rating,drinks_rating=data['quiet'],data['comfort'],data['drinks']
            food_rating,view_rating,toilets_rating,speed_rating=data['food'],data['view'],data['toilets'],data['speed']
            
            rating=Score_rec(user_id=user_id,cafe_id=cafe_id,wifi=wifi_rating,\
                    speed=speed_rating,vacancy=vaca_rating,comfort=comfort_rating,quiet=quiet_rating,\
                    food=food_rating,drinks=drinks_rating,price=price_rating,view=view_rating,toilets=toilets_rating)
            
            
            rating.insert()
            update=db.session.execute(f'SELECT avg(price), avg(wifi),avg(vacancy) ,avg(quiet),avg(comfort),avg(drinks),avg(food),avg(view),avg(toilets),avg(speed) FROM `score_rec` where cafe_id={cafe_id}').first()
            cafe=Cafes.query.filter_by(id=cafe_id).first()
       
            update_data={
            'price':update[0],'wifi':update[1],'vacancy':update[2],
            'quiet':update[3],'comfort':update[4],'drinks':update[5],'food':update[6],
            'view':update[7],'toilets':update[8],'speed':update[9]
            }
            
            cafe.price=update_data['price']
            cafe.wifi=update_data['wifi']
            cafe.vacancy=update_data['vacancy']
            cafe.quiet=update_data['quiet']
            cafe.comfort=update_data['comfort']
            cafe.drinks=update_data['drinks']
            cafe.food=update_data['food']
            cafe.view=update_data['view']
            cafe.toilets=update_data['toilets']
            cafe.speed=update_data['speed']
            cafe.rating=rating_avg([update_data['price'],update_data['wifi'],update_data['vacancy'],update_data['comfort'],update_data['drinks']])
            
            cafe.update()
            order=db.session.query(Score_rec).order_by(Score_rec.create_time.desc()).filter_by(user_id=user_id,cafe_id=cafe_id).first()
          
            return jsonify({'data':True,'number':order.scr_id})
            
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})
    
