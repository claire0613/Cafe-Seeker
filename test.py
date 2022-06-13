from model.models import City_ref, Photo, Score_rec, Rank, db, Cafes, Message, Message_like, Users, Cafes_like,redis_db
from data.api_helper import city_cafe_filter,key_search,get_rank,area_from_city,check_website,check_float
from datetime import datetime
from flask import *
try:
    city_id='1'
    city_tw='台北'
    try:
        print('cache now')
        cache_update_time=redis_db.get('update_time')
        cache_search_list=redis_db.get('search_list')
        cache_favor_list=redis_db.get('favor_list')
        cache_msg_list=redis_db.get('msg_list')
        cache_rating_list=redis_db.get('rating_list')
        print('已經有cache', cache_update_time)
        if not cache_update_time:
            print('消失cache', cache_update_time)
            search_count = Rank.query.filter_by(city_id=city_id).order_by(Rank.search_count.desc()).limit(8).all()
            update_time=datetime.strftime(search_count[0].update_time, "%Y-%m-%d %H:%M")
            search_list =get_rank(search_count,city_id)
            redis_db.set('search_list',search_list,ex=2000)
            redis_db.set('update_time',update_time,ex=2000)
            
            

            cafe_favor = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_favor_count.desc()).limit(8).all()
            favor_list =get_rank(cafe_favor,city_id)
            redis_db.set('favor_list',favor_list,ex=2000)
            

            cafe_msg = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_msg_count.desc()).limit(8).all()
            msg_list =get_rank(cafe_msg,city_id)
            redis_db.set('msg_list',msg_list,ex=2000)
          
    
            cafe_rating = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_rating_count.desc()).limit(8).all()
            rating_list=get_rank(cafe_rating,city_id)
            redis_db.set('rating_list', rating_list,ex=2000)
    
            
        print(jsonify({"data": True, "search_count": cache_search_list, "cafe_favor": cache_favor_list, "cafe_msg": cache_msg_list, "cafe_rating": cache_rating_list,'city_name':city_tw,'update_time':cache_update_time})) 
    except:
        search_count = Rank.query.filter_by(city_id=city_id).order_by(Rank.search_count.desc()).limit(8).all()
        update_time=datetime.strftime(search_count[0].update_time, "%Y-%m-%d %H:%M")
        search_list =get_rank(search_count,city_id)
        cafe_favor = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_favor_count.desc()).limit(8).all()
        favor_list =get_rank(cafe_favor,city_id)
        cafe_msg = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_msg_count.desc()).limit(8).all()
        msg_list =get_rank(cafe_msg,city_id)
        cafe_rating = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_rating_count.desc()).limit(8).all()
        rating_list=get_rank(cafe_rating,city_id)
        print('no cache')
        print(jsonify({"data": True, "search_count": search_list, "cafe_favor": favor_list, "cafe_msg": msg_list, "cafe_rating": rating_list,'city_name':city_tw,'update_time':update_time}))
except:
        print(jsonify({"error": True, "message": "伺服器內部錯誤"})) 
    