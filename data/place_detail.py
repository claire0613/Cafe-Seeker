
import urllib.request
import requests 
from bs4 import BeautifulSoup

import urllib.request as req

import re 
import sys,json
sys.path.append("..")
from model.models import Cafes, City_ref,Score_rec,db,Photo

def rating_avg(data):
    result_list=[]
    for i in data:
        if i !=0.0 and not None:
            result_list.append(i)
    if result_list :
        return round(sum(result_list)/len(result_list),1)
    return 0.0
 
# cafes=Cafes().search_all()
# for cafe in cafes: 



# cafes=Cafes().search_all()
# for cafe in cafes:
#     cafe_nomad_id=cafe.cafe_nomad_id
#     cafe.rating=rating_avg([cafe.price,cafe.wifi,cafe.vacancy,cafe.comfort,cafe.quiet,cafe.drinks])
#     cafe.update()
#     if cafe_nomad_id:
#         url=f'https://cafenomad.tw/shop/{cafe_nomad_id}'
#         request=req.Request(url,headers={
#             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
#         })
#         with req.urlopen(request) as response:
#             data=response.read().decode('utf-8')

#         soup=BeautifulSoup(data,'lxml')
#         items=soup.find_all('div',{'class':'openinghours-box'})
#         times=soup.find_all('div',{'class':'time'})
#         imgs=soup.find_all('div',{'class':'_thumbnail'})
#         city_div=soup.find_all('div',{'style':'margin-top: 5px;'})
#         details=soup.find_all('div',{'class':'col-xs-6'})
                     
#         if details:
#             detail=details[2].select(".rating-box")
#             detail_list=[None,None,None]
#             for i in range(len(detail)):
#                 result=detail[i].text.split()[-1]

#                 if result=='Yes':
#                     result=True
#                 elif result=='No':
#                     result=False
#                 else:
#                     result= None
#                 detail_list[i]=result
            
#             cafe.single_selling=detail_list[0]
#             cafe.dessert_selling=detail_list[1]
#             cafe.meal_selling=detail_list[2]
#             cafe.update()
        
#         if city_div !=[]:
#             for city in city_div:
#                 target=city.text.strip()
#                 cafe.area=target
#                 cafe.update()
#         # if cafe.images ==[] or cafe.images ==None:
#             if imgs !=[]:
#                 for img in imgs:
#                     img_list=img.select('.photo')
#                     num=1
#                     for item in img_list:
#                         num+=1
#                         target='https://cafenomad.tw'+item.get('src')
#                         photo=Photo(user_id=3,cafe_id=cafe.id,photo_url=target,photo_name=f'{cafe.id}_cafe_nomad.{num}')
#                         photo.insert()
#                     num=1
        
#         time_list=[]
#         if times !=[]:
#             for time in times:
#                 target=time.text.strip()
#                 time_list.append(target)
#             time_dict={
#                 'mon':time_list[0],'tue':time_list[1],'wed':time_list[2],'thu':time_list[3],'fri':time_list[4],'sat':time_list[5],'sun':time_list[6]
#             }
#             cafe.open_hours=json.dumps(time_dict,ensure_ascii=False)
#             cafe.update()



    
 

     
        
 
cafes=Cafes().search_all()
for cafe in cafes:
    if cafe.area.isalpha():
        area=cafe.address
        city=re.findall(r"(\w{2}[縣市])",area)
        area_detail=re.findall(r"[縣市](\w+?[鄉鎮市區])",area)
        if city !=[]:
            city=city[0].strip()
            if area_detail !=[]:
                area_detail=area_detail[0].strip()
                target=f'{city} ⋅ {area_detail}'
                cafe.area=target
                cafe.update()
            else:
                target=f'{city}'
                cafe.area=target
                cafe.update()
        else:
            query=City_ref.query.filter_by(city_id=cafe.city_id).first()
            cafe.area=query.city_tw
            cafe.update()
    
         
        


       
        
        
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