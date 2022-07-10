from . import api
from model.models import City_ref, db,Cafes,Score_rec,Rating
from flask import *
from data.api_helper import rating_avg,check_num
import jwt,re,sys,os
sys.path.append("..")
from dotenv import load_dotenv
load_dotenv()

    
@api.route('/rating/<scr_id>', methods=['GET'])
def get_rating(scr_id):
    try:
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            scr_id=scr_id
            order=Score_rec.query.filter_by(scr_id=scr_id).first()
            cafe_name=Cafes.query.filter_by(id=order.cafe_id).first().name
            result={
            'price':order.price,'wifi':order.wifi,'vacancy':order.vacancy,
            'quiet':order.quiet,'comfort':order.comfort,'drinks':order.drinks,'food':order.food,
            'view':order.view,'toilets':order.toilets,'speed':order.speed,'cafe_name':cafe_name,
            'cafe_id':order.cafe_id
            }

        return jsonify({'data':result})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})    
    
    
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
         
          
            rating_query=Rating.query.filter_by(cafe_id=cafe_id).first()
            update=db.session.execute(f'SELECT avg(price), avg(wifi),avg(vacancy) ,avg(quiet),avg(comfort),avg(drinks),avg(food),avg(view),avg(toilets),avg(speed) FROM `score_rec` where cafe_id={cafe_id}').first()
            update_data={
            'price':check_num(update[0]),'wifi':check_num(update[1]),'vacancy':check_num(update[2]),
            'quiet':check_num(update[3]),'comfort':check_num(update[4]),'drinks':check_num(update[5]),'food':check_num(update[6]),
            'view':check_num(update[7]),'toilets':check_num(update[8]),'speed':check_num(update[9])
            }
            rating_query.price=update_data['price']
            rating_query.wifi=update_data['wifi']
            rating_query.vacancy=update_data['vacancy']
            rating_query.quiet=update_data['quiet']
            rating_query.comfort=update_data['comfort']
            rating_query.drinks=update_data['drinks']
            rating_query.food=update_data['food']
            rating_query.view=update_data['view']
            rating_query.toilets=update_data['toilets']
            rating_query.speed=update_data['speed']
            rating_query.rating=rating_avg([update_data['price'],update_data['wifi'],update_data['vacancy'],update_data['comfort'],update_data['drinks']])
            
            rating_query.update()
            order=db.session.query(Score_rec).order_by(Score_rec.create_time.desc()).filter_by(user_id=user_id,cafe_id=cafe_id).first()
          
            return jsonify({'data':True,'number':order.scr_id})
            
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})
    
