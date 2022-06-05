
from sqlalchemy import update

import yaml
import sys
sys.path.append("..")
from model.models import Cafes, Score_rec,City_ref, Station_ref,Photo
import os,json
from dotenv import load_dotenv
load_dotenv()


def md_in_dir(dir):
    #input 資料夾路徑下 return 此目錄下的所有檔案list
    filenames=[]
    for filename in os.listdir(dir):
        if filename.endswith('.md'):
            filenames.append(os.path.join(dir,filename))
           
            
    return filenames
def listing(data):
    if data:
        return [data]
    else:
        return []
def int_check(data):
    if data:
        return data
    else:
        return None
def check_socket(data):
    if data:
        if data >=3 :
            return 'yes'
        elif data >0:
            return 'maybe'
        elif data ==0:
            return 'no'
    else:
        return ''
def check_address(data):
    if isinstance(data,dict):
        return data.get('zh-tw')
    else:
        return data
def check_hours(data):
    if isinstance(data,str):
        return {'mon':data,'tue':data,'wed':data,'thu':data,'fri':data,'sat':data,'sun':data }
    else:
        if isinstance(data,dict):
            if not data.get('mon'):
                data['mon']='未營業'
            if not data.get('tue'):
                data['tue']='未營業'
            if not data.get('wed'):
                data['wed']='未營業'
            if not data.get('wed'):
                data['thu']='未營業'
            if not data.get('fri'):
                data['fri']='未營業'
            if not data.get('sat'):
                data['sat']='未營業'
            if not data.get('sun'):
                data['sun']='未營業'
        return data       

def set_default_int(data):
    if data:
        return data
    else:
        return 0

def parseFile(filename,dir_f):
    #寫入資料庫
    
    with open(filename,'r',encoding='utf8') as file:
        file_split=file.read().split('---')
        data=yaml.load(file_split[1],Loader=yaml.SafeLoader)
        content='---'.join(file_split[2:]).strip()
        coordinates=data.get("coordinates")
        address=check_address(data.get("address"))
        area=data.get("area")
        if area:
            area=area.lower()
        # imgs=data.get("images")
        # img_list=[]
        # if imgs:
        #     for img in imgs:
            #     image_url=os.getenv("CDN_URL")+f"cafe-seeker/{dir_f}/{filename[7:-3]}/{img}"
            #     img_list.append(image_url)
          
        
       
        if not data.get("closed"):
            
            if data.get('content'):
                data["review"]["en"]=content
            city_a=dir_f
            if dir_f =='taiwan':
                city_a=data.get("area")
                if city_a:
                    city_a=city_a.lower()
                
            if coordinates and address and area:
                latitude=data["coordinates"].split(',')[0]
                longitude=data["coordinates"].split(',')[1]
                city_search=City_ref.query.filter_by(city=city_a).first()
                if city_search:
                    city_id=city_search.city_id
                else:
                    city_id=None
                station=Station_ref.query.filter_by(station=data.get("station")).first()
                
                if station:
                    station=station.station_tw
             
                result=Cafes(name=data.get("name"),area=area,city_id=city_id,address=address,\
                transport=station,google_maps=data.get("google_maps"),latitude=latitude,longitude=longitude,\
                open_hours=json.dumps(check_hours(data.get("hours")), ensure_ascii=False),open_time=data.get("open_time"),wifi=set_default_int(data.get("wifi")),\
                speed=set_default_int(data.get("speed")),vacancy=set_default_int(data.get("vacancy")),\
                comfort=set_default_int(data.get("comfort")),quiet=set_default_int(data.get("quiet")),\
                food=set_default_int(data.get("food")),drinks=set_default_int(data.get("drinks")),price=set_default_int(data.get("price")),\
                view=set_default_int(data.get("view")),toilets=set_default_int(data.get("toilets")),socket=check_socket(data.get("power")),limited_time=None,\
                music=data.get("music"),smoking=data.get("smoking"),standing_tables=data.get("standing_tables"),outdoor_seating=data.get("outdoor_seating"),\
                cash_only=data.get("cash_only"),animals=data.get("animals"),facebook=data.get("facebook"),\
                instagram=data.get("instagram"),telephone=data.get("telephone"),website=data.get("website"))
                result.insert()
                query_id=Cafes().search_by_name(data.get("name"))
                id=query_id[-1].id
                
                record=Score_rec(user_id=2,cafe_id=id,wifi=int_check(data.get("wifi")),\
                speed=int_check(data.get("speed")),\
                vacancy=int_check(data.get("vacancy")),comfort=int_check(data.get("comfort")),quiet=int_check(data.get("quiet")),\
                food=int_check(data.get("food")),drinks=int_check(data.get("drinks")),price=int_check(data.get("price")),\
                view=int_check(data.get("view")),toilets=int_check(data.get("toilets")))
                record.insert()
                
                imgs=data.get("images")
               
                if imgs:
                    for img in imgs:
                        photo=Photo(user_id=2,cafe_id=id,photo_url=os.getenv("CDN_URL")+f"cafe-seeker/{dir_f}/{filename[7:-3]}/{img}",photo_name=img)
                        photo.insert()
                
 
            return data




def read_md_and_insert_db(dir,dir_f):
    mds=md_in_dir(dir)
    
    for filename in mds:
        parseFile(filename,dir_f)
    
city=['taipei', 'keelung', 'taoyuan', 'hsinchu','miaoli','taichung','Nantou','changhua','yunlin','chiayi', 'Tainan','kaohsiung','pingtung', 'yilan','hualien', 'penghu', 'taitung', 'lienchiang','Kinmen']
city_tw=['台北','基隆','桃園','新竹','苗栗','台中','南投','彰化','雲林','嘉義','台南','高雄','屏東','宜蘭','花蓮','澎湖','台東','連江','金門',]
for i in range (len(city)):
    city_insert=City_ref(city=city[i].lower(),city_id=i+1,city_tw=city_tw[i])
    city_insert.insert()
    
    
    
read_md_and_insert_db('taipei',dir_f='taipei')
read_md_and_insert_db('taiwan',dir_f='taiwan')


# def img_in_dir(dir):
#     #input 資料夾路徑下 return 此目錄下的所有檔案list
#     filenames=[]
#     for filename in os.listdir(dir):
#         if filename.endswith('.md'):
#             filenames.append(os.path.join(dir,filename)) 
#     return filenames
# def read_img_and_insert_db(dir,dir_f):
#     imgs=img_in_dir(dir)
#     for filename in imgs:
#         print(filename)
#         # parseFile(filename,dir_f)
# read_img_and_insert_db('../images/taipei/',dir_f='taipei')


                # record=Score_rec(user_id=2,cafe_id=id,wifi=json.dumps(listing(data.get("wifi"))),\
                # speed=json.dumps(listing(data.get("speed"))),\
                # vacancy=json.dumps(listing(data.get("vacancy"))),comfort=json.dumps(listing(data.get("comfort"))),quiet=json.dumps(listing(data.get("quiet"))),\
                # food=json.dumps(listing(data.get("food"))),drinks=json.dumps(listing(data.get("drinks"))),price=json.dumps(listing(data.get("price"))),\
                # view=json.dumps(listing(data.get("view"))),toilets=json.dumps(listing(data.get("toilets"))))
                
                
                # result=Cafes(name=data.get("name"),area=area,city_id=city_id,address=address,\
                # transport=station,google_maps=data.get("google_maps"),latitude=latitude,longitude=longitude,\
                # open_hours=json.dumps(check_hours(data.get("hours")), ensure_ascii=False),open_time=data.get("open_time"),wifi=set_default_int(data.get("wifi")),\
                # speed=set_default_int(data.get("speed")),vacancy=set_default_int(data.get("vacancy")),\
                # comfort=set_default_int(data.get("comfort")),quiet=set_default_int(data.get("quiet")),\
                # food=set_default_int(data.get("food")),drinks=set_default_int(data.get("drinks")),price=set_default_int(data.get("price")),\
                # view=set_default_int(data.get("view")),toilets=set_default_int(data.get("toilets")),socket=check_socket(data.get("power")),limited_time=None,\
                # music=data.get("music"),smoking=data.get("smoking"),standing_tables=data.get("standing_tables"),outdoor_seating=data.get("outdoor_seating"),\
                # cash_only=data.get("cash_only"),animals=data.get("animals"),facebook=data.get("facebook"),\
                # instagram=data.get("instagram"),telephone=data.get("telephone"),website=data.get("website"),\
                # images=json.dumps(img_list, ensure_ascii=False),review=json.dumps(data.get("review"), ensure_ascii=False))