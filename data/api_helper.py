from ast import expr_context
from decimal import Decimal
from sqlalchemy import or_, and_
from model.models import City_ref, Photo, Score_rec, Rank, db, Cafes, Message, Message_like, Users, Cafes_like
import re
def key_search_detail(result):
    
    result_list = []
    for item in result:
        a={'id':item[0],'name':item[1],'area':item[2],'wifi':item[3],'drinks':item[4],'photo_url':item[5]}
        result_list.append(a)

    return result_list

def key_search(page, keyword=None):
    page=page*20
    limit=20
    if not keyword:
        result = db.session.execute(f"select c.id,c.name,c.area,c.wifi,c.drinks,p.photo_url from cafes as c left join photo as p on p.cafe_id=c.id GROUP By c.id LIMIT {page},{limit}").all()
        all_count =len(result)
        total_count = Cafes.query.count()

    else:

        # 有keyword 沒有city
        # keyword中 check city中英
        key_city = City_ref.query.filter(City_ref.city_tw == keyword).first()
        if key_city:
            city_id = key_city.city_id
            result=db.session.execute(f"select c.id,c.name,c.area,c.wifi,c.drinks,p.photo_url from cafes as c left join photo as p on p.cafe_id=c.id WHERE c.city_id={city_id} \
                            and MATCH (name,address) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE)\
                            GROUP By c.id LIMIT {page},{limit}").all()
            
            all_count = len(result)
            total = db.session.execute(f"select c.id,c.name,c.area,c.wifi,c.drinks,p.photo_url from cafes as c left join photo as p on p.cafe_id=c.id WHERE c.city_id={city_id} \
                            and MATCH (name,address) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE) GROUP By c.id ").all()
            total_count=len(total)

        else:
            result=db.session.execute(f"select c.id,c.name,c.area,c.wifi,c.drinks,p.photo_url from cafes as c left \
                        join photo as p on p.cafe_id=c.id WHERE  \
                        MATCH (name,address) AGAINST('{keyword}' IN NATURAL LANGUAGE MODE)GROUP By c.id LIMIT {page},{limit}").all()
            all_count = len(result)
            total = db.session.execute(f"select c.id,c.name,c.area,c.wifi,c.drinks,p.photo_url from cafes as c left \
                        join photo as p on p.cafe_id=c.id WHERE  \
                        MATCH (name,address) AGAINST('{keyword}' IN NATURAL LANGUAGE MODE)GROUP By c.id ").all()
            total_count=len(total)

    answer = key_search_detail(result)

    return {'cafe_list': answer, 'all_count': all_count, 'total_count': total_count}

def city_search_cafe(page, city=None):
    if not city:
        result = Cafes.query.limit(20).offset(page*20).all()
        all_count = Cafes.query.limit(20).offset(page*20).count()
        total_count = Cafes.query.count()

        cafe_list = []
        for cafe in result:
            cafe_dict = {c.name: getattr(cafe, c.name)
                         for c in cafe.__table__.columns}
            cafe_list.append(cafe_dict)

        return {'cafe_list': cafe_list, 'all_count': all_count, 'total_count': total_count}

    else:
        city_search = City_ref.query.filter_by(city=city).first()
        city_id = city_search.city_id
        if city_search:
            all_count = Cafes.query.filter(
                Cafes.city_id == city_id).limit(20).offset(page*20).count()
            result = Cafes.query.filter(Cafes.city_id == city_id).limit(
                20).offset(page*20).all()
            total_count = Cafes.query.filter(Cafes.city_id == city_id).count()
        else:
            return None

        cafe_list = []
        for cafe in result:
            cafe_dict = {c.name: getattr(cafe, c.name)
                         for c in cafe.__table__.columns}
            cafe_list.append(cafe_dict)

        return {'cafe_list': cafe_list, 'all_count': all_count, 'city_tw': city_search.city_tw, 'total_count': total_count}
def city_cafe_filter(page, keyword, city, rating, price, wifi, vacancy, drinks, quiet, comfort, limited_time, meal_selling):
    page=page*20
    limit=20
    city_search = City_ref.query.filter_by(city=city).first()
    city_id = city_search.city_id
    if keyword:
        if  (meal_selling == '1' or  meal_selling == '0')  and limited_time=='1' :
            result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE) and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet} and (limited_time ='yes' or limited_time ='maybe') and  meal_selling = {meal_selling}LIMIT {page},{limit}").all()
            total=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE) and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet} and (limited_time ='yes' or limited_time ='maybe') and meal_selling = {meal_selling}").all()
          
        elif limited_time =='1':
                result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE)and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and (limited_time ='yes' or limited_time ='maybe') LIMIT {page},{limit} )").all()          
                total=db.session.execute(f"select id,name,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE)and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and (limited_time ='yes' or limited_time ='maybe')").all()  
        elif limited_time =='0':
            result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE)and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and limited_time ='no' LIMIT {page},{limit} )").all()          
            total=db.session.execute(f"select id,name,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE)and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and limited_time ='no')").all()                
        elif(meal_selling == '1' or  meal_selling == '0')  and limited_time=='0' :
            result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE) and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet} and limited_time ='no' and  meal_selling = {meal_selling}LIMIT {page},{limit}").all() 
            total=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE) and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet} and limited_time ='no' and  meal_selling = {meal_selling}").all()
        elif (meal_selling == '1' or  meal_selling == '0') :
            result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE) and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet}  and  meal_selling = {meal_selling} LIMIT {page},{limit}").all()
            total=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE) and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet}  and  meal_selling = {meal_selling}").all() 
        else:
            result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name,address) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE) and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} LIMIT {page},{limit}").all()  
            total=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and MATCH (name,address) AGAINST('{keyword}'IN NATURAL LANGUAGE MODE)and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort}").all()
    else:
        if  (meal_selling == '1' or  meal_selling == '0')  and limited_time=='1' :
            result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet} and (limited_time ='yes' or limited_time='maybe') and  meal_selling = {meal_selling} LIMIT {page},{limit}").all()
            total=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet} and (limited_time ='yes' or limited_time='maybe') and  meal_selling = {meal_selling}").all()
        elif (meal_selling == '1' or  meal_selling == '0')  and limited_time=='0':
            result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                        where city_id={city_id} and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                        and comfort >={comfort} and quiet >={quiet} and limited_time ='no' and  meal_selling = {meal_selling} LIMIT {page},{limit}").all()
            total=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                        where city_id={city_id} and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                        and comfort >={comfort} and quiet >={quiet} and limited_time ='no' and  meal_selling = {meal_selling}").all() 
    
        elif limited_time =='1':
            result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet} and (limited_time ='yes' or limited_time ='maybe') ").all()
            total=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet} and (limited_time ='yes' or limited_time ='maybe')  ").all()        
           
        elif limited_time =='0':
            result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet} and limited_time ='no'LIMIT {page},{limit}").all()
            total=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet} and limited_time ='no' ").all()   

        elif (meal_selling == '1' or  meal_selling == '0') :
            result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet}  and  meal_selling = {meal_selling} LIMIT {page},{limit}").all()
            total=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and rating >={rating} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and quiet >={quiet}  and  meal_selling = {meal_selling}").all()  
         
            
        else:
            result=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                                and comfort >={comfort} and rating >={rating} LIMIT {page},{limit}").all()
            total=db.session.execute(f"select id,name,rating,price,wifi,vacancy,drinks,quiet,comfort,limited_time,meal_selling,open_hours,transport from cafes\
                            where city_id={city_id} and price>={price} and wifi>={wifi} and vacancy>={vacancy} and drinks>={drinks}\
                            and comfort >={comfort} and rating >={rating} ").all()
       
    all_count = len(result)
    total_count=len(total)
    result_list = []
    for item in result:
        a={'id':item[0],'name':item[1],'rating':item[2],'price':item[3],'wifi':item[4],'vacancy':item[5],'drinks':item[6],'quiet':item[7],'comfort':item[8],'limited_time':item[9],'meal_selling':item[10],'open_hours':item[11],'transport':item[12]}
        result_list.append(a)

    return {'cafe_list': result_list, 'all_count': all_count, 'city_tw': city_search.city_tw,'total_count':total_count}


def get_rank(value, city_id):
    result_list = []
    for search in value:
        search_data = db.session.query(Cafes, Photo).join(Photo, Photo.cafe_id == Cafes.id, isouter=True).filter(and_(Cafes.id == search.cafe_id,Cafes.city_id==city_id)).group_by(Cafes.id).first()
        search_t = search_data[0].as_dict()
        
        if search_data[1]:
            search_t['photo_url'] = search_data[1].photo_url
        else:
            search_t['photo_url'] = None
        result_list.append(search_t)
    return result_list

def area_from_city(address,city_id):
    try:
        area=address
        city=re.findall(r"(\w{2}[縣市])",area)
        area_detail=re.findall(r"[縣市](\w+?[鄉鎮市區])",area)
        if city !=[]:
            city=city[0].strip()
            if area_detail !=[]:
                area_detail=area_detail[0].strip()
                target=f'{city} ⋅ {area_detail}'
                area=target
                
            else:
                target=f'{city}'
                area=target
                
        else:
            query=City_ref.query.filter_by(city_id=city_id).first()
            area=query.city_tw
            
        return area
    except:
        query=City_ref.query.filter_by(city_id=city_id).first()
        area=query.city_tw
        return area
            


def updated_name_pwd(user_id=None,new_name=None,pwd=None):
    try:
        if new_name:
                query=Users.query.filter_by(user_id=user_id).first()
                print(query.username)
                query.username=new_name
                query.update()
              
        elif pwd:
                query=Users.query.filter_by(user_id=user_id).first()
                query.password=pwd
                query.update()
        return True
        
    except: 
        return None

def check_float(value):
    if value:
        return float(value)
    else:
        return None
def check_website(data,status):
    if 'facebook' in data and 'fb' in status:
        result=data
    elif 'instagram'in data and 'ig' in status:
        result=data
    elif 'web' in status:
        result=data
    else:
        result=None
    return result