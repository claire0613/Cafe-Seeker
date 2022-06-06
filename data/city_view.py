import sys
sys.path.append("..")
from model.models import Cafes, Score_rec,Cafes_like,Message,View



cafes=Cafes().search_all()
for cafe in cafes:
    update=View.query.filter_by(cafe_id=cafe.id).first()
    if update:
        cafe_favor=Cafes_like.query.filter_by(cafe_id=cafe.id).count()
        cafe_rating=Score_rec.query.filter_by(cafe_id=cafe.id).count()
        cafe_msg=Message.query.filter_by(cafe_id=cafe.id).count()
        view.search_count=cafe.search_count
        view.cafe_favor_count=cafe_favor
        view.cafe_msg_count=cafe_msg
        view.cafe_rating_count=cafe_rating

        view.update()
    else:
        cafe_favor=Cafes_like.query.filter_by(cafe_id=cafe.id).count()
        cafe_rating=Score_rec.query.filter_by(cafe_id=cafe.id).count()
        cafe_msg=Message.query.filter_by(cafe_id=cafe.id).count()
        view=View(cafe_id=cafe.id,search_count=cafe.search_count,cafe_favor_count=cafe_favor,cafe_msg_count=cafe_msg)
        view.insert()
    
    
    
    
    
    
   
    
    