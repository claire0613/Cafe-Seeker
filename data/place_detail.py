
import urllib.request
import requests 
from bs4 import BeautifulSoup

import urllib.request as req

import re 
import sys,json
sys.path.append("..")
from model.models import Cafes, City_ref, Open_hours, Rating,Score_rec,db,Photo

def rating_avg(data):
    result_list=[]
  
    for i in data:
        if i !=0.0 and i is not None:
            result_list.append(i)
    if result_list :
        return round(sum(result_list)/len(result_list),1)
    return 0.0
def check_num(data):
    if not data:
        return 0.0
    else:
        return data 



cafes=Cafes().search_all()
for cafe in cafes:
    check_rating=Rating.query.filter_by(cafe_id=cafe.id).first()
    if check_rating:
        update=db.session.execute(f'SELECT avg(price), avg(wifi),avg(vacancy) ,avg(quiet),avg(comfort),avg(drinks),avg(food),avg(view),avg(toilets),avg(speed) FROM `score_rec` where cafe_id={cafe.id}').first()
        update_data={
        'price':check_num(update[0]),'wifi':check_num(update[1]),'vacancy':check_num(update[2]),
        'quiet':check_num(update[3]),'comfort':check_num(update[4]),'drinks':check_num(update[5]),'food':check_num(update[6]),
        'view':check_num(update[7]),'toilets':check_num(update[8]),'speed':check_num(update[9])
        }
        check_rating.price=update_data['price']
        check_rating.wifi=update_data['wifi']
        check_rating.vacancy=update_data['vacancy']
        check_rating.quiet=update_data['quiet']
        check_rating.comfort=update_data['comfort']
        check_rating.drinks=update_data['drinks']
        check_rating.food=update_data['food']
        check_rating.view=update_data['view']
        check_rating.toilets=update_data['toilets']
        check_rating.speed=update_data['speed']
        check_rating.rating=rating_avg([update_data['price'],update_data['wifi'],update_data['vacancy'],update_data['comfort'],update_data['drinks']])
        check_rating.update()
    else:
        renew=db.session.execute(f'SELECT avg(price), avg(wifi),avg(vacancy) ,avg(quiet),avg(comfort),avg(drinks),avg(food),avg(view),avg(toilets),avg(speed) FROM `score_rec` where cafe_id={cafe.id}').first()
        renew_data={
        'price':check_num(renew[0]),'wifi':check_num(renew[1]),'vacancy':check_num(renew[2]),
        'quiet':check_num(renew[3]),'comfort':check_num(renew[4]),'drinks':check_num(renew[5]),'food':check_num(renew[6]),
        'view':check_num(renew[7]),'toilets':check_num(renew[8]),'speed':check_num(renew[9])
        }
        rating_new=Rating(cafe_id=cafe.id,wifi=renew_data.get("wifi"),\
                        speed=renew_data.get("speed"),vacancy=renew_data.get("vacancy"),\
                        comfort=renew_data.get("comfort"),quiet=renew_data.get("quiet"),\
                        food=renew_data.get("food"),drinks=renew_data.get("drinks"),price=renew_data.get("price"),\
                        view=renew_data.get("view"),toilets=renew_data.get("toilets"),\
                        rating=rating_avg([renew_data['price'],renew_data['wifi'],renew_data['vacancy'],renew_data['comfort'],renew_data['drinks']]))
        rating_new.insert()
        
        
    cafe_nomad_id=cafe.cafe_nomad_id
    if cafe_nomad_id:
        url=f'https://cafenomad.tw/shop/{cafe_nomad_id}'
        request=req.Request(url,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
        })
        with req.urlopen(request) as response:
            data=response.read().decode('utf-8')

        soup=BeautifulSoup(data,'lxml')
        items=soup.find_all('div',{'class':'openinghours-box'})
        times=soup.find_all('div',{'class':'time'})
        imgs=soup.find_all('div',{'class':'_thumbnail'})
        city_div=soup.find_all('div',{'style':'margin-top: 5px;'})
        details=soup.find_all('div',{'class':'col-xs-6'})
                     
        # if details:
        #     detail=details[2].select(".rating-box")
        #     detail_list=[None,None,None]
        #     for i in range(len(detail)):
        #         result=detail[i].text.split()[-1]

        #         if result=='Yes':
        #             result=True
        #         elif result=='No':
        #             result=False
        #         else:
        #             result= None
        #         detail_list[i]=result
            
        #     cafe.single_selling=detail_list[0]
        #     cafe.dessert_selling=detail_list[1]
        #     cafe.meal_selling=detail_list[2]
        #     cafe.update()
        
        # if city_div !=[]:
        #     for city in city_div:
        #         target=city.text.strip()
        #         cafe.area=target
        #         cafe.update()

        #     if imgs !=[]:
        #         for img in imgs:
        #             img_list=img.select('.photo')
        #             num=1
        #             for item in img_list:
        #                 num+=1
        #                 target='https://cafenomad.tw'+item.get('src')
        #                 check_photo_url=Photo.query.filter_by(photo_url='https://cafenomad.tw'+item.get('src')).first()
        #                 if not check_photo_url:
        #                     photo=Photo(user_id=3,cafe_id=cafe.id,photo_url=target,photo_name=f'{cafe.id}_cafe_nomad.{num}')
        #                     photo.insert()
        #             num=1
        
        time_list=[]
        if times !=[]:
            for time in times:
                target=time.text.strip()
                time_list.append(target)
            hours_dic={
                'mon':time_list[0],'tue':time_list[1],'wed':time_list[2],'thu':time_list[3],'fri':time_list[4],'sat':time_list[5],'sun':time_list[6]
            }
            check=Open_hours.query.filter_by(cafe_id=cafe.id).first()
            if not check:
                hour=Open_hours(cafe_id=cafe.id,mon=hours_dic['mon'],tue=hours_dic['tue'],wed=hours_dic['wed'],thu=hours_dic['thu'],fri=hours_dic['fri'],sat=hours_dic['sat'],sun=hours_dic['sun'])
                hour.insert()

        
                
            



    
 

     
        
 
# cafes=Cafes().search_all()
# for cafe in cafes:
#     if cafe.area.isalpha():
#         area=cafe.address
#         city=re.findall(r"(\w{2}[縣市])",area)
#         area_detail=re.findall(r"[縣市](\w+?[鄉鎮市區])",area)
#         if city !=[]:
#             city=city[0].strip()
#             if area_detail !=[]:
#                 area_detail=area_detail[0].strip()
#                 target=f'{city} ⋅ {area_detail}'
#                 cafe.area=target
#                 cafe.update()
#             else:
#                 target=f'{city}'
#                 cafe.area=target
#                 cafe.update()
#         else:
#             query=City_ref.query.filter_by(city_id=cafe.city_id).first()
#             cafe.area=query.city_tw
#             cafe.update()
    
         
        


       
        
        
#         wifi=db.session.query(db.func.avg(Score_rec.wifi)).filter_by(cafe_id=cafe.id).scalar()
#         print(wifi,cafe.wifi)


        # if cafe.images ==[] or cafe.images ==None:
        #      if imgs !=[]:
        #         new_img=[]
        #         for img in imgs:
        #             img_list=img.select('.photo')
        #             for item in img_list:
        #                 target='https://cafenomad.tw'+item.get('src')
        #                 new_img.append(target)
                
        #         cafe.images=json.dumps(new_img)
        #         cafe.update()