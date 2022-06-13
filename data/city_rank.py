import sys,datetime
sys.path.append("..")
from model.models import Cafes, Score_rec,Cafes_like,Message,Rank



cafes=Cafes().search_all()
for cafe in cafes:
    update=Rank.query.filter_by(cafe_id=cafe.id).first()
    if update:
        cafe_favor=Cafes_like.query.filter_by(cafe_id=cafe.id).count()
        cafe_rating=Score_rec.query.filter_by(cafe_id=cafe.id).count()
        cafe_msg=Message.query.filter_by(cafe_id=cafe.id).count()
        update.search_count=cafe.search_count
        update.cafe_favor_count=cafe_favor
        update.cafe_msg_count=cafe_msg
        update.cafe_rating_count=cafe_rating
        update.city_id=cafe.city_id
        update.update()
    else:
        cafe_favor=Cafes_like.query.filter_by(cafe_id=cafe.id).count()
        cafe_rating=Score_rec.query.filter_by(cafe_id=cafe.id).count()
        cafe_msg=Message.query.filter_by(cafe_id=cafe.id).count()
        view=Rank(cafe_id=cafe.id,search_count=cafe.search_count,cafe_favor_count=cafe_favor,cafe_msg_count=cafe_msg,city_id=cafe.city_id)
        view.insert()
print(datetime.datetime.now())
    
    
    
    
    
    
   
    
    