
import jwt,sys,os
sys.path.append("..")
from flask import *
from . import api
from dotenv import load_dotenv
from data.api_helper import city_cafe_filter,key_search,get_rank,area_from_city,check_website,check_float
from model.models import City_ref, Photo, Score_rec, Rank, db, Cafes, Message, Message_like, Users, Cafes_like,redis_db,DecimalEncoder
from datetime import datetime
load_dotenv()


@api.route('/city', methods=['GET'])
def get_city():
    try:
        page = int(request.args.get('page'))
        limit = 4
        result_list = []
        nextpage = 1
        if page == 1:
            page = page*4
            limit = limit+11
            nextpage = None
        result = City_ref.query.offset(page).limit(limit).all()

        for item in result:
            data = {
                'city': item.city,
                'city_tw': item.city_tw,
                'city_id': item.city_id,

            }
            result_list.append(data)
        return jsonify({'data': result_list, 'nextPage': nextpage})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})


@api.route('/search', methods=['GET'])
def get_shop_key():
    try:
        page = int(request.args.get('page'))
        keyword = request.args.get('keyword')
        result = key_search(page=page, keyword=keyword)

        surplus = result['all_count']
        if surplus < 20:
            next_page = None
        else:
            next_page = page+1

        return jsonify({"nextPage": next_page, "data": result['cafe_list'], 'totalPage': result['total_count']//20, 'totalCount': result['total_count']})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})


@api.route('/city/list/filter', methods=['GET'])
def get_city_filter():
    try:
        page = int(request.args.get('page'))
        city = request.args.get('city')

        rating = request.args.get('rating')
        price = request.args.get('price')
        keyword = request.args.get('keyword')
        wifi = request.args.get('wifi')
        vacancy = request.args.get('vacancy')
        drinks = request.args.get('drinks')
        quiet = request.args.get('quiet')
        comfort = request.args.get('comfort')
        limited_time = request.args.get('limited_time')
        meal_selling = request.args.get('meal_selling')
       
        if limited_time!= "":
            limited_time = request.args.get('limited_time')
          
        if meal_selling!="":
            meal_selling  = request.args.get('meal_selling')

        result = city_cafe_filter(page=page, city=city, keyword=keyword, price=price, wifi=wifi, vacancy=vacancy, drinks=drinks, quiet=quiet, comfort=comfort,
                                  limited_time=limited_time, meal_selling=meal_selling, rating=rating)

        if result:
            surplus = result['all_count']
            if surplus < 20:
                next_page = None
            else:
                next_page = page+1
            return jsonify({"city_tw": result['city_tw'], "nextPage": next_page, "data": result['cafe_list'], 'totalCount': result['total_count']})
        else:
            return jsonify({"error": True, "message": 'NO DATA'})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})



@api.route('/shop/<cafe_id>', methods=['GET'])
def get_shop(cafe_id):
    try:
        result = Cafes.query.filter_by(id=cafe_id).first()
        if result:
          
            photo_t = []
            photo_list = Photo.query.order_by(Photo.create_time.desc()).filter_by(
                cafe_id=cafe_id).limit(15).all()
            msg_t = []
            msg_list = Message.query.order_by(
                Message.create_time).filter_by(cafe_id=cafe_id).all()
            token_cookie = request.cookies.get('user_cookie')

            score_count = Score_rec.query.filter_by(cafe_id=cafe_id).count()
            if token_cookie:
                is_login = True
            else:
                is_login = False
            for photo in photo_list:
                photo_t.append(photo.photo_url)
            for msg in msg_list:
                msg_dict = msg.as_dict()
                msg_dict['user_avatar'] = Users.query.filter_by(
                    user_id=msg_dict.get('user_id')).first().avatar
                msg_dict['create_time'] = datetime.strftime(
                    msg.create_time, "%Y-%m-%d %H:%M")
                if token_cookie:
                    user = jwt.decode(token_cookie, os.getenv(
                        "SECRET_KEY"), algorithms=['HS256'])
                    user_id = user['id']

                    is_favor = Message_like.query.filter_by(
                        msg_id=msg.msg_id, user_id=user_id).first()
                    if is_favor:
                        is_favor = True
                    else:
                        is_favor = False
                    msg_dict['is_favor'] = is_favor
                    msg_dict['now_user'] = user_id

                msg_t.append(msg_dict)

            result = result.as_dict()
            return jsonify({"data": result, "photo_url": photo_t, 'message': msg_t, 'is_login': is_login, 'score_count': score_count})

        else:
            return jsonify({"error": True, "message": 'no Cafe'})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})


@api.route('/shop/view/<cafe_id>', methods=['POST'])
def post_shop_browse(cafe_id):
    try:

        cafe = Cafes.query.filter_by(id=cafe_id).first()
        add = cafe.search_count+1
        cafe.search_count = add
        cafe.update()
        return jsonify({"data": True, "now_search_count": add})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})


@api.route('/city/rank', methods=['GET'])
def get_city_rank():
    try:
    
        city=request.args.get('city')
        city_search = City_ref.query.filter_by(city=city).first()
        city_id = city_search.city_id
        city_tw=city_search.city_tw
        try:
            cache_fetch=redis_db.get('fetch')
            if not cache_fetch:
                search_count = Rank.query.filter_by(city_id=city_id).order_by(Rank.search_count.desc()).limit(8).all()
                update_time=datetime.strftime(search_count[0].update_time, "%Y-%m-%d %H:%M")
                search_list =get_rank(search_count,city_id)
                cafe_favor = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_favor_count.desc()).limit(8).all()
                favor_list =get_rank(cafe_favor,city_id)
                cafe_msg = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_msg_count.desc()).limit(8).all()
                msg_list =get_rank(cafe_msg,city_id)
                cafe_rating = Rank.query.filter_by(city_id=city_id).order_by(Rank.cafe_rating_count.desc()).limit(8).all()
                rating_list=get_rank(cafe_rating,city_id)
                data=json.dumps({"data": True, "search_count": search_list, "cafe_favor": favor_list, "cafe_msg": msg_list, "cafe_rating": rating_list,'city_name':city_tw,'update_time':update_time}, cls=DecimalEncoder,ensure_ascii=False)
                redis_db.setex('fetch',200, data)
            return jsonify(json.loads(cache_fetch)),200
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
            return jsonify({"data": True, "search_count": search_list, "cafe_favor": favor_list, "cafe_msg": msg_list, "cafe_rating": rating_list,'city_name':city_tw,'update_time':update_time})
    except:
            return jsonify({"error": True, "message": "伺服器內部錯誤"})
        
        
@api.route('/shop/insert', methods=['POST'])
def post_cafe_insert():
    try:
        data=request.json
        cafe_name=data['name']
        exist=Cafes.query.filter_by(name=cafe_name).first()
        city_id=data['city_id']
        address=data['address']
        area=area_from_city(address,city_id)
        latitude=check_float(data['latitude'])
        longitude=check_float(data['longitude'])

        single_selling,dessert_selling,meal_selling=int(data['single_selling']),int(data['dessert_selling']),int(data['meal_selling'])
        limited_time,socket,staning_tables,music=data['limited_time'],data['socket'],int(data['standing_tables']),int(data['music'])
        outdoor_seating,cash_only,animals=int(data['outdoor_seating']),int(data['cash_only']),int(data['animals'])
        open_hours,website,mrt,phone=data['open_hours'],data['website'],data['mrt'],data['phone']

        if not exist:
            result=Cafes(name=cafe_name,area=area,city_id=city_id,address=address,\
                rating=0.0,wifi=0.0,speed=0.0,vacancy=0.0,comfort=0.0,quiet=0.0,food=0.0,drinks=0.0,price=0.0,view=0.0,toilets=0.0,\
                transport=mrt,latitude=latitude,longitude=longitude,socket=socket,limited_time=limited_time,\
                music=music, single_selling= single_selling,dessert_selling=dessert_selling,standing_tables=staning_tables,\
                outdoor_seating=outdoor_seating,meal_selling=meal_selling,open_hours=json.dumps(open_hours, ensure_ascii=False),\
                cash_only=cash_only,animals=animals,facebook=check_website(website,'fb'),\
                instagram=check_website(website,'ig'),telephone=phone,website=website)
            result.insert()
            cafe_id=Cafes.query.filter_by(name=cafe_name).first().id
            
 
            return jsonify({"ok": True,'cafe_id':cafe_id})
        else:
            return jsonify({"error": True, "message":"店家已經重複請再次確認"})
    except:
            return jsonify({"error": True, "message": "伺服器內部錯誤"})



