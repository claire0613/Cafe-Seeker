

from flask import *
from sqlalchemy import or_,and_
from . import api
import jwt,sys,os
sys.path.append("..")
from dotenv import load_dotenv
load_dotenv()
from model.models import City_ref, Photo, db,Cafes,Message,Message_like,Users
from datetime import datetime

def key_search(page, keyword=None):
    if not keyword:
        result = Cafes.query.limit(20).offset(page*20).all()
        all_count = Cafes.query.limit(20).offset(page*20).count()
        total_count=Cafes.query.count()
       
    else:
     
        #有keyword 沒有city
        #keyword中 check city中英
        key_city=City_ref.query.filter(City_ref.city_tw==keyword).first()
        if key_city:
            city_id=key_city.city_id
            query=Cafes.query.filter(or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%'),\
                        Cafes.city_id==city_id))
            all_count=query.limit(20).offset(page*20).count()
            total_count=query.count()
            
            
            result=query.limit(20).offset(page*20).all()
        else: 
            query=Cafes.query.filter(or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%'))).\
                limit(20).offset(page*20)
            all_count= query.count()
            total_count= query.count()
            result= query.all()
                
                  
    cafe_list=[]
    for cafe in result:
        cafe_dict = {c.name: getattr(cafe, c.name) for c in cafe.__table__.columns}
        cafe_list.append(cafe_dict)
  
    return {'cafe_list':cafe_list,'all_count':all_count,'total_count':total_count}

    
def city_search_cafe(page,city=None):
    if not city:
        result = Cafes.query.limit(20).offset(page*20).all()
        all_count = Cafes.query.limit(20).offset(page*20).count()
        total_count= Cafes.query.count()
        
        cafe_list=[]
        for cafe in result:
            cafe_dict = {c.name: getattr(cafe, c.name) for c in cafe.__table__.columns}
            cafe_list.append(cafe_dict)

        return {'cafe_list':cafe_list,'all_count':all_count,'total_count':total_count}
        
    else:
        city_search=City_ref.query.filter_by(city=city).first()
        city_id=city_search.city_id
        if city_search:
            all_count=Cafes.query.filter(Cafes.city_id==city_id).limit(20).offset(page*20).count()
            result=Cafes.query.filter(Cafes.city_id==city_id).limit(20).offset(page*20).all()
            total_count= Cafes.query.filter(Cafes.city_id==city_id).count()  
        else:
            return None
                    
        cafe_list=[]
        for cafe in result:
            cafe_dict = {c.name: getattr(cafe, c.name) for c in cafe.__table__.columns}
            cafe_list.append(cafe_dict)

        return {'cafe_list':cafe_list,'all_count':all_count,'city_tw':city_search.city_tw,'total_count':total_count}
    
    


 
def city_cafe_filter(page,keyword,city,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling):
        if not city:
            result = Cafes.query.limit(20).offset(page*20).all()
            all_count = Cafes.query.limit(20).offset(page*20).count()
            total_count= Cafes.query.count()
            
            cafe_list=[]
            for cafe in result:
                cafe_dict = {c.name: getattr(cafe, c.name) for c in cafe.__table__.columns}
                cafe_list.append(cafe_dict)

            return {'cafe_list':cafe_list,'all_count':all_count,'total_count':total_count}
       
        else :
            city_search=City_ref.query.filter_by(city=city).first()
            city_id=city_search.city_id
            if keyword:
                if (meal_selling or  meal_selling is False ) or limited_time:
                        query=Cafes.query.filter(and_\
                    (Cafes.city_id==city_id,or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%')),Cafes.price>=price,Cafes.wifi>=wifi,Cafes.vacancy>=vacancy,\
                        Cafes.drinks>=drinks,Cafes.quiet>=quiet,Cafes.comfort>=comfort,\
                        or_(Cafes.limited_time=='yes',Cafes.limited_time=='maybe'),Cafes.meal_selling.is_(meal_selling)))
                        print('++')

                elif limited_time:
                    query=Cafes.query.filter(and_\
                    (Cafes.city_id==city_id,or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%')),Cafes.price>=price,Cafes.wifi>=wifi,Cafes.vacancy>=vacancy,\
                        Cafes.drinks>=drinks,Cafes.quiet>=quiet,Cafes.comfort>=comfort,or_(Cafes.limited_time=='yes',Cafes.limited_time=='maybe'),Cafes.meal_selling==meal_selling))
                elif limited_time is False:
                    query=Cafes.query.filter(and_\
                    (Cafes.city_id==city_id,or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%')),Cafes.price>=price,Cafes.wifi>=wifi,Cafes.vacancy>=vacancy,\
                        Cafes.drinks>=drinks,Cafes.quiet>=quiet,Cafes.comfort>=comfort,Cafes.limited_time=='no',Cafes.meal_selling==meal_selling))
                elif (meal_selling or  meal_selling is False ) or limited_time is False:
                    query=Cafes.query.filter(and_\
                    (Cafes.city_id==city_id,or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%')),Cafes.price>=price,Cafes.wifi>=wifi,Cafes.vacancy>=vacancy,\
                        Cafes.drinks>=drinks,Cafes.quiet>=quiet, Cafes.comfort>=comfort,Cafes.limited_time=='no',Cafes.meal_selling.is_(meal_selling)))
                elif (meal_selling or  meal_selling is False ):
                        query=Cafes.query.filter(and_\
                    (Cafes.city_id==city_id,or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%')),Cafes.price>=price,Cafes.wifi>=wifi,Cafes.vacancy>=vacancy,\
                        Cafes.drinks>=drinks,Cafes.quiet>=quiet, Cafes.comfort>=comfort,Cafes.meal_selling.is_(meal_selling)))     
                    
                    
                    
                else:   
      
          
                    query=Cafes.query.filter(and_\
                    (Cafes.city_id==city_id,or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%')),Cafes.rating>=rating,Cafes.price>=price,Cafes.wifi>=wifi,\
                        Cafes.vacancy>=vacancy,Cafes.drinks>=drinks,Cafes.quiet>=quiet,Cafes.comfort>=comfort))
                
            else:
                
                if (meal_selling or  meal_selling is False ) and limited_time:
                    query=Cafes.query.filter(and_\
                    (Cafes.city_id==city_id,Cafes.price>=price,Cafes.wifi>=wifi,Cafes.vacancy>=vacancy,Cafes.drinks>=drinks,Cafes.quiet>=quiet,\
                        Cafes.comfort>=comfort,or_(Cafes.limited_time=='yes',Cafes.limited_time=='maybe'),Cafes.meal_selling==meal_selling))

                elif limited_time:
                    query=Cafes.query.filter(and_\
                    (Cafes.city_id==city_id,Cafes.price>=price,Cafes.wifi>=wifi,Cafes.vacancy>=vacancy,Cafes.drinks>=drinks,Cafes.quiet>=quiet,\
                        Cafes.comfort>=comfort,or_(Cafes.limited_time=='yes',Cafes.limited_time=='maybe')))
                elif limited_time is False:
                    query=Cafes.query.filter(and_\
                    (Cafes.city_id==city_id,Cafes.price>=price,Cafes.wifi>=wifi,Cafes.vacancy>=vacancy,Cafes.drinks>=drinks,Cafes.quiet>=quiet,\
                        Cafes.comfort>=comfort,Cafes.limited_time=='no'))
                elif (meal_selling or  meal_selling is False ) and limited_time is False:
                    query=Cafes.query.filter(and_\
                    (Cafes.city_id==city_id,Cafes.price>=price,Cafes.wifi>=wifi,Cafes.vacancy>=vacancy,Cafes.drinks>=drinks,Cafes.quiet>=quiet,\
                        Cafes.comfort>=comfort,Cafes.limited_time=='no'))
            
            
                else:   
                    query=Cafes.query.filter(and_\
                        (Cafes.city_id==city_id,Cafes.rating>=rating,Cafes.price>=price,Cafes.wifi>=wifi,Cafes.vacancy>=vacancy,Cafes.drinks>=drinks,Cafes.quiet>=quiet,\
                            Cafes.comfort>=comfort))
                                
            all_count = query.limit(20).offset(page*20).count()
            result = query.limit(20).offset(page*20).all()
            total_count = query.count()

                            
            cafe_list=[]
            for cafe in result:
                cafe_dict = {c.name: getattr(cafe, c.name) for c in cafe.__table__.columns}
                cafe_list.append(cafe_dict)

            return {'cafe_list':cafe_list,'all_count':all_count,'city_tw':city_search.city_tw,'total_count':total_count}
    
# print(city_cafe_filter(page=0,city='taipei',keyword=None,price=0,wifi=0,vacancy=0,drinks=0,quiet=0,comfort=0,limited_time=None,meal_selling=None,rating=0))  
# print(cafe_filter(page=0,city='taipei',price=0.0,wifi=0.0,vacancy=0.0,drinks=0.0,quiet=0.0,toilets=0.0,limited_time=None,meal_selling=None,rating=0.0))  




    
@api.route('/city', methods=['GET'])
def get_city():
    # try:
        page = int(request.args.get('page'))
        limit=4
        result_list=[]
        nextpage=1
        if page==1:
            page=page*4
            limit=limit+11
            nextpage=None
        result=City_ref.query.offset(page).limit(limit).all()
        
        for item in result:
            data={
                'city':item.city,
                'city_tw':item.city_tw,
                'city_id':item.city_id,
                
            }
            result_list.append(data)
        return  jsonify({'data':result_list,'nextPage':nextpage})
    # except:
    #     return jsonify({"error": True, "message": "伺服器內部錯誤"})
    
    
@api.route('/search',methods=['GET'])
def get_shop_key():
    try:
        page = int(request.args.get('page'))
        keyword=request.args.get('keyword')
        result=key_search(page=page,keyword=keyword)
        surplus=result['all_count']
        if surplus<20:
            next_page=None
        else:
            next_page=page+1
    
        return jsonify({"nextPage": next_page, "data": result['cafe_list'],'totalPage':result['total_count']//20,'totalCount':result['total_count']}) 
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})



    
    
@api.route('/city/list/filter', methods=['GET'])
def get_city_filter():
    try:
        page = int(request.args.get('page'))
        city=request.args.get('city')
      

        rating=request.args.get('rating')
        price=request.args.get('price')
        keyword=request.args.get('keyword')
        wifi= request.args.get('wifi')
        vacancy=request.args.get('vacancy')
        drinks=request.args.get('drinks')
        quiet=request.args.get('quiet')
        comfort=request.args.get('comfort')
        limited_time=request.args.get('limited_time')
        meal_selling=request.args.get('meal_selling')
  

        if  limited_time :
            limited_time=bool(int(request.args.get('limited_time')))
        if  meal_selling :
            meal_selling=bool(int(request.args.get('meal_selling')))   
   
            
        
        result=city_cafe_filter(page=page,city=city,keyword=keyword,price=price,wifi=wifi,vacancy=vacancy,drinks=drinks,quiet=quiet,comfort=comfort,\
        limited_time=limited_time,meal_selling=meal_selling,rating=rating)

        # if keyword:
        #     keyword='aaa'
        # else:
        #     keyword='000'
        # return f'{page},{city},{price},{keyword},{rating},{wifi},{vacancy},{food},{quiet},{comfort},{limited_time},{meal_selling}'
       
    
        if result:
            surplus=result['all_count']
            if surplus<20:
                next_page=None
            else:
                next_page=page+1
            return  jsonify({"city_tw":result['city_tw'],"nextPage": next_page, "data": result['cafe_list'],'totalCount':result['total_count']})
        else:
            return  jsonify({"error": True, "message": 'NO DATA'})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})
    
    
    
@api.route('/shop/<cafe_id>', methods=['GET'])
def get_shop(cafe_id):
    try:
        if cafe_id:
            result=Cafes.query.filter_by(id=cafe_id).first()
            photo_t=[]
            photo_list=Photo.query.order_by(Photo.create_time.desc()).filter_by(cafe_id=cafe_id).limit(15).all()
            msg_t=[]
            msg_list=Message.query.order_by(Message.create_time).filter_by(cafe_id=cafe_id).all()
            token_cookie=request.cookies.get('user_cookie')
            for photo in photo_list:
                photo_t.append(photo.photo_url)
            for msg in msg_list:
                msg_dict=msg.as_dict()
                msg_dict['user_avatar']=Users.query.filter_by(user_id=msg_dict.get('user_id')).first().avatar
                msg_dict['create_time']=datetime.strftime(msg.create_time,"%Y-%m-%d %H:%M")
                if token_cookie:
                    user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
                    user_id=user['id']
                    is_favor=Message_like.query.filter_by(msg_id=msg.msg_id,user_id=user_id).first()
                    if is_favor:
                        is_favor=True
                    else:
                        is_favor=False
                    msg_dict['is_favor']=is_favor
                    msg_dict['now_user']=user_id
                    
                msg_t.append(msg_dict)
                
                 
            result=result.as_dict()
            return  jsonify({ "data": result,"photo_url":photo_t,'message':msg_t})
        
            
        
        else:
            return  jsonify({"error": True, "message": 'no Cafe'})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})
     
    #  db.session.query(City_ref).order_by(City_ref.city_id).offset(page).limit(limit).all()
    # page=0&city=taipei&keyword=&rating=&price=&wifi=&vacancy=&food=&quiet=&comfort=&limted_time=&meal_selling=