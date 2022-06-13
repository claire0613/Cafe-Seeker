from model.models import City_ref, Photo, Score_rec, Rank, db, Cafes, Message, Message_like, Users, Cafes_like,redis_db
from data.api_helper import city_cafe_filter,key_search,get_rank,area_from_city,check_website,check_float
from datetime import datetime
from flask import *
import json
try:
    city_id='1'
    city_tw='台北'

    print('cache now')
    cache_fetch=redis_db.get('fetch')

    
    if not cache_fetch:
        print('消失cache')
        search_count = Rank.query.filter_by(city_id=city_id).order_by(Rank.search_count.desc()).limit(8).all()
        update_time=datetime.strftime(search_count[0].update_time, "%Y-%m-%d %H:%M")
        search_list =get_rank(search_count,city_id)
     
        cafe_favor = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_favor_count.desc()).limit(8).all()
        favor_list =get_rank(cafe_favor,city_id)
        cafe_msg = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_msg_count.desc()).limit(8).all()
        msg_list =get_rank(cafe_msg,city_id)
        cafe_rating = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_rating_count.desc()).limit(8).all()
        rating_list=get_rank(cafe_rating,city_id)
        data=json.dumps({"data": True, "search_count": search_list, "cafe_favor": favor_list, "cafe_msg": msg_list, "cafe_rating": rating_list,'city_name':city_tw,'update_time':update_time})
        redis_db.setex('fetch',200, data)
    
    print('目前有cache',redis_db.get('fetch'))        
    print(data)
    # else:
    #     search_count = Rank.query.filter_by(city_id=city_id).order_by(Rank.search_count.desc()).limit(8).all()
    #     update_time=datetime.strftime(search_count[0].update_time, "%Y-%m-%d %H:%M")
    #     search_list =get_rank(search_count,city_id)
    #     cafe_favor = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_favor_count.desc()).limit(8).all()
    #     favor_list =get_rank(cafe_favor,city_id)
    #     cafe_msg = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_msg_count.desc()).limit(8).all()
    #     msg_list =get_rank(cafe_msg,city_id)
    #     cafe_rating = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_rating_count.desc()).limit(8).all()
    #     rating_list=get_rank(cafe_rating,city_id)
    #     print('no cache 直接fetch')
    #     print(jsonify({"data": True, "search_count": search_list, "cafe_favor": favor_list, "cafe_msg": msg_list, "cafe_rating": rating_list,'city_name':city_tw,'update_time':update_time}))
except:
        print(jsonify({"error": True, "message": "伺服器內部錯誤"})) 
    