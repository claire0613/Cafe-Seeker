import sys
sys.path.append("..")
import requests
from env import PLACE_KEY
from model.models import Cafes,db
import json




     



# cafes=Cafes().search_all()
# for cafe in cafes:
# for i in range(32,3511):
    # latitude=cafe.get('latitude')
    # longitude=cafe.get('longitude')
    # name=cafe.get('name')
   
    # query=cafe.search_by_id(cafe.id)

#     url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=500&type=cafe&language=zh-TW&keyword={name}&key={PLACE_KEY}"
#     payload={}
#     headers = {}
#     response = requests.request("GET", url, headers=headers, data=payload)
#     data=json.loads(response.text)
#     results=data['results']  #if fail response= {'html_attributions': [], 'results': [], 'status': 'INVALID_REQUEST'}
#     if results!=[]:
#        Cafes().update_place_id(results[0].get('place_id'),results[0].get('rating'),name)
        
    # latitude=cafes[i].latitude
    # longitude=cafes[i].longitude
    # name=cafes[i].name
    # print(i)               

    # url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=1000&type=cafe&language=zh-TW&keyword={name}&key={PLACE_KEY}"
    # payload={}
    # headers = {}
    # response = requests.request("GET", url, headers=headers, data=payload)
    # data=json.loads(response.text)
    # results=data['results']
    # # print(results)#if fail response= {'html_attributions': [], 'results': [], 'status': 'INVALID_REQUEST'}
    # # print(results[0].get('place_id'),results[0].get('rating'),name)
    # if results!=[]:
    #     plus_code=results[0].get('plus_code')
    #     compound_code=plus_code.get('compound_code')
    #     if compound_code:
    #         area=compound_code.split()[1]
    #         city=compound_code.split()[2]
    #         cafes[i].google_place_id=results[0].get('place_id')
    #         cafes[i].google_rating=results[0].get('rating')
    #         cafes[i].area=area
    #         cafes[i].city=city
    #         db.session.commit()
    #         print(results[0].get('place_id'),results[0].get('rating'),area,city)
    #     else:
    #         cafes[i].google_place_id=results[0].get('place_id')
    #         cafes[i].google_rating=results[0].get('rating')
    #         db.session.commit()
    #         print(results[0].get('place_id'),results[0].get('rating'))






# Cafes().update_place_id(results[0].get('place_id'),results[0].get('rating'),name)




    
