
import sys,json
sys.path.append("..")

from model.models import Cafes, City_ref,Station_ref

with open('../locales/zh-tw.json','r',encoding='utf8') as file:
    for line in file:
      
        if line.split(':')[0].strip() =='"Station':
            station=Station_ref(station=line.split(':')[1][:-1].strip(),station_tw=line.split(':')[2].split('"')[1].strip())
            station.insert()


# a=Cafes.query.join(City_ref).add_columns(City_ref.city_tw,City_ref.city_id).first()  