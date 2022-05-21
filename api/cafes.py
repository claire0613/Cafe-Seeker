
from ast import keyword
from flask import *
from sqlalchemy import or_
api = Blueprint('api', __name__)
from model.models import City_ref, db,Cafes

def key_search(page, keyword=None):
    if not keyword:
        result = Cafes.query.limit(20).offset(page*20).all()
        all_count = Cafes.query.limit(20).offset(page*20).count()
       
    else:
     
        #有keyword 沒有city
        #keyword中 check city中英
        key_city=City_ref.query.filter(or_(City_ref.city==keyword,City_ref.city_tw==keyword)).first()
        if key_city:
            city_en=key_city.city
            all_count=Cafes.query.filter(or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%'),\
                        Cafes.city==city_en)).limit(20).offset(page*20).count()
            result=Cafes.query.filter(or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%'),\
                        Cafes.city==city_en)).limit(20).offset(page*20).all()
        else: 
            all_count= Cafes.query.filter(or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%'))).\
                limit(20).offset(page*20).count()
            result=Cafes.query.filter(or_(Cafes.name.like(f'%{keyword}%'),Cafes.address.like(f'%{keyword}%')))\
                .limit(20).offset(page*20).all()
                
                  
    cafe_list=[]
    for cafe in result:
        cafe_dict = {c.name: getattr(cafe, c.name) for c in cafe.__table__.columns}
        cafe_list.append(cafe_dict)

    return {'cafe_list':cafe_list,'all_count':all_count}
    
def city_search_cafe(page,city=None):
    if not  city:
            result = Cafes.query.limit(20).offset(page*20).all()
            all_count = Cafes.query.limit(20).offset(page*20).count()
        
    else:
            all_count=Cafes.query.filter(Cafes.city==city).limit(20).offset(page*20).count()
            result=Cafes.query.filter(Cafes.city==city).limit(20).offset(page*20).all()
            
        
   
    
                  
    cafe_list=[]
    for cafe in result:
        cafe_dict = {c.name: getattr(cafe, c.name) for c in cafe.__table__.columns}
        cafe_list.append(cafe_dict)

    return {'cafe_list':cafe_list,'all_count':all_count}
    

# @api.route('/cafes', methods=['GET'])
# def get_attraction():
#     try: 
      
#         page = int(request.args.get('page'))
#         keyword=request.args.get('keyword')
        
#         allcount=attraction_count(page=page,keyword=keyword)
        
#         data = search_attracion(page=page,keyword=keyword)
#         count=allcount-page*12
#         if count<12:
#             nextpage=None
#         else:
#             nextpage=page+1
#         return jsonify({"nextPage": nextpage, "data": data}) 
#     except:
#             return jsonify({"error": True, "message": "伺服器內部錯誤"})
        
        
        
# @api.route('/attraction/<attractionId>', methods=['GET'])
# def get_attractionid(attractionId):
#     try:
#         if attractionId:
#             data=search_attractionid(attractionId)
#             return jsonify({"data": data})
#         else:
#             return jsonify({"error": True, "message": "景點編號不正確"})
        
#     except:
#         return jsonify({"error": True, "message": "伺服器內部錯誤"})        
        
        
# @api.route('/attraction/<attractionId>', methods=['GET'])
# def get_attractionid(attractionId):
#     try:
#         if attractionId:
#             data=search_attractionid(attractionId)
#             return jsonify({"data": data})
#         else:
#             return jsonify({"error": True, "message": "景點編號不正確"})
        
#     except:
#         return jsonify({"error": True, "message": "伺服器內部錯誤"})
    

# def shop_count(page,keyword=None):
#     if keyword:
#         all_count=Cafes().query.filter_by(name=keyword).count()

    
#     else:
#         all_count=Cafes().query..count()


# @api.route('/cafe/city', methods=['GET'])
# def search_city():
#     result=db.session.query(Cafes.city).distinct().all()
#     print(result)
    
    
#     city_list=[]
#     for city in result:
#         city_list.append(city[0])


#     print(city_list)
#     return  'ok'
    
@api.route('/city', methods=['GET'])
def get_city():
    try:
        page = int(request.args.get('page'))
        limit=4
        result_list=[]
        nextpage=1
        if page==1:
            page=page*4
            limit=limit+11
            nextpage=None
        result=db.session.query(City_ref).order_by(City_ref.city_id).offset(page).limit(limit).all()
        for item in result:
            data={
                'city':item.city,
                'city_tw':item.city_tw,
                'city_id':item.city_id,
                
            }
            result_list.append(data)
        return  jsonify({'data':result_list,'nextPage':nextpage})
    except:
        return jsonify({"error": True, "message": "伺服器內部錯誤"})
@api.route('/search',methods=['GET'])
def get_shop_key():
    page = int(request.args.get('page'))
    keyword=request.args.get('keyword')
    result=key_search(page=page,keyword=keyword)
    surplus=result['all_count']

    if surplus==0:
        next_page=None
    else:
        next_page=page+1
    return jsonify({"nextPage": next_page, "data": result['cafe_list']}) 
         
         
     
     