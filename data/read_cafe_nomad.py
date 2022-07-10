
import urllib.request as req
import json
import sys
sys.path.append("..")
from model.models import Cafes, City_ref,Score_rec,db,Rating
from api_helper import rating_avg
def main():

    url="https://cafenomad.tw/api/v1.2/cafes"
    #建立一個request物件 附加 Request Header的資訊
    request=req.Request(url,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'
    })


    with req.urlopen(request) as response:
        data=response.read().decode('utf-8')  #f取得資料是JSON格式
    #解析JSON格式的資料
    results=json.loads(data)
    

    count=0        

    for result in results:
        cafe=Cafes()
        query_id=cafe.search_by_name(result.get("name"))        
        exist=cafe.search_nomad(search_name=result.get('name'))
        if not '已結束營業' in result.get("open_time") and not '停業'in result.get("open_time") and not'已結束營業' in result.get("name") and not'停業' in result.get("name"):
            if exist :
                
                exist.longitude=check_coordinate(result.get("longitude"))
                exist.latitude=check_coordinate(result.get("latitude"))
                exist.transport=check_data_str(exist.transport,result.get('mrt'))
                # exist.open_time=result.get("open_time")
                
                # exist.wifi=check_score_f(exist.wifi,result.get('wifi'))
                # exist.vacancy=check_score_f(exist.vacancy,result.get('seat'))
                # exist.quiet=check_score_f(exist.quiet,result.get('quiet'))
                # exist.food=check_score_f(exist.food,result.get('tasty'))
                # exist.drinks=check_score_f(exist.drinks,result.get('tasty'))
                # exist.price=check_score_f(exist.quiet,result.get('cheap'))
                
                exist.socket=check_data_str(exist.socket,result.get('socket'))
                exist.music=check_music(exist.music,result.get('music'))
                exist.facebook=check_fb_ig_web(exist.facebook,result.get('url'),'fb')
                exist.instagram=check_fb_ig_web(exist.instagram,result.get('url'),'ig')
                exist.website=check_fb_ig_web(exist.website,result.get('url'),'web')
                exist.standing_tables=check_standing_desk(exist.standing_tables,result.get('standing_desk'))
                
                exist.cafe_nomad_id=result.get('id')
                exist.limited_time=result.get('limited_time')
                cafe.update()
                if query_id:
                    cafe_id=query_id[-1].id
           
                    record=Score_rec(user_id=3,cafe_id=cafe_id,wifi=int_nomad(result.get('wifi')),\
                    vacancy=int_nomad(result.get('seat')),comfort=int_nomad(result.get('music')),quiet=int_nomad(result.get('quiet')),\
                    food=int_nomad(result.get('tasty')),drinks=int_nomad(result.get('tasty')),price=int_nomad(result.get('cheap')))
                    record.insert() 
                

            else:
                latitude=check_coordinate(result.get("latitude"))
                longitude=check_coordinate(result.get("longitude"))
                if latitude and longitude:
                    city_id=City_ref.query.filter_by(city=result.get("city")).first().city_id
                    insert_data=Cafes(name=result.get("name"),area=result.get("city"),city_id=city_id,address=result.get("address"),\
                        transport=result.get("mrt"),latitude=latitude,longitude=longitude,\
                        socket=result.get('socket'),limited_time=result.get('limited_time'),\
                        music=check_music_i(result.get('music')),standing_tables=check_standing_desk_i(result.get('standing_desk')),facebook=check_url(result.get('url'),'fb'),\
                        instagram=check_url(result.get('url'),'ig'),website=check_url(result.get('url'),'web'),\
                        cafe_nomad_id=result.get('id'))
                    insert_data.insert()
                    query_id=cafe.search_by_name(result.get("name"))
                    if query_id:
                        cafe_id=query_id[-1].id
        
                        record=Score_rec(user_id=3,cafe_id=cafe_id,wifi=int_nomad(result.get('wifi')),\
                        vacancy=int_nomad(result.get('seat')),comfort=int_nomad(result.get('music')),quiet=int_nomad(result.get('quiet')),\
                        food=int_nomad(result.get('tasty')),drinks=int_nomad(result.get('tasty')),price=int_nomad(result.get('cheap')))
                        record.insert()
                        rating_query=Rating.query.filter_by(cafe_id=cafe_id).first()
                
                        if not rating_query:
                            rating_new=Rating(cafe_id=cafe_id,wifi=result.get('wifi'),speed=0,\
                            vacancy=result.get("seat"),comfort=result.get('music'),quiet=result.get("quiet"),food=result.get("tasty"),drinks=result.get("tasty"),price=result.get("cheap"))
                            rating_new.insert()
                        else:
                            update=db.session.execute(f'SELECT avg(price), avg(wifi),avg(vacancy) ,avg(quiet),avg(comfort),avg(drinks),avg(food),avg(view),avg(toilets),avg(speed) FROM `score_rec` where cafe_id={id}').first()
                            update_data={
                            'price':update[0],'wifi':update[1],'vacancy':update[2],
                            'quiet':update[3],'comfort':update[4],'drinks':update[5],'food':update[6],
                            'view':update[7],'toilets':update[8],'speed':update[9]
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

def listing_nomad(data):
    if data!=0:
        return json.dumps([data])
    else:
        return json.dumps([])
    
def int_nomad(data):
    if data!=0:
        return data
    else:
        return None


        
def check_fb_ig_web(exist_d,result,status):
    if exist_d:
        #cowork後是否有存data
        if result!='':
                #nomad api ['url'] retrun ''
            if 'facebook' in result and 'facebook' in exist_d:
                        exist_d=result
            if 'instagram'in result and 'instagram' in exist_d  and 'ig' in status:
                        exist_d=result
            if 'facebook' not in result and 'instagram' not in result \
                    and 'facebook' not in exist_d and 'instagram' not in exist_d:
                        exist_d=result
    else:
        if 'facebook' in result and 'fb' in status:
            exist_d=result
        elif 'instagram'in result and 'ig' in status:
            exist_d=result
        elif 'facebook' not in result and 'instagram' not in result and 'web' in status:
            exist_d=result
        elif 'web' in status:
            exist_d=result
        else:
            exist_d=None
            
    return exist_d

def check_score_js(exist_d,result):
    if exist_d:
        if result != 0:
            return json.dumps(exist_d+[result])
        else:
            return json.dumps(exist_d+[])
    else:
        if result != 0:
            return json.dumps(exist_d+[result])
        else:
            return json.dumps([])
def check_score_f(exist_d,result):
    if exist_d:
        if result != 0:
            return round((exist_d+result)/2,1)
        else:
            return exist_d
    else:
        return exist_d
        
def check_music(exist_d,result):
    if exist_d == True or exist_d ==False:
        if result ==0:
            return None
        elif result > 0  :
            return True
        else:
            return exist_d
    else:
        if result ==0:
            return None
        elif result > 0  :
            return True
        else:
            return exist_d
def check_music_i(result):
        if result > 0  :
            return True
        else:
            return None

        
def check_standing_desk(exist_d,result):
    if not exist_d:
        if result =='yes' or result=='maybe':
            return True
        elif result=='no':
            return False
        else:
            return None
def check_standing_desk_i(result):
        if result =='yes' or result=='maybe':
            return True
        elif result=='no':
            return False
        else:
            return None
    
def check_data_str(exist_d,result):
    if exist_d:
        if result != '':
            return result
        else:
            return exist_d
    else:
        if result != '':
            return result
        else:
            return None

def check_url(data,status):
    if data != '':
        if 'facebook' in data and 'fb' in status and data.startswith('http'):
             return data
        elif 'instagram'in data and 'ig' in status and data.startswith('http'):
             return data  
        elif  'web' in status and data.startswith('http'):
             return data
    else:
        data=None
        return data

    
def check_j_l(data):
    if data:
        return json.loads(data)
    else:
        return []
def check_coordinate(data):
    if data != '0.00000000':
        return data
    return None



if __name__ == '__main__':
    main()