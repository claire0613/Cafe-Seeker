from model.models import Users,db,Cafes,Photo,Score_rec,Message,Message_like,Cafes_like,View
from sqlalchemy.sql import func
# import os

# # user=Users(username='a',email='a@gmail.com',password='a')
# # # db.session.add(user)
# # check=Users.query.filter_by(email='aa@gmail.com').first().verify_password(pwd='a')
# # print (check)
# # if check:
# #     print('ok')
# # else:
# #     print('error')
    
# # a=os.urandom(24)
# # print(a)
# cafe_id='2'
# result=Cafes.query.filter_by(wifi='5').first()
# print(result)
# result=result.as_dict()
# print(result)


            
# def binarySearch(arr,target):
#     low=0
#     hight=len(arr)-1
#     while low<=hight:
#         mid=low+hight//2
#         guess=arr[mid]
#         if guess==target:
#             return mid
#         elif(guess>target):
#             hight=mid+1
#         else:
#             low=mid-1
#     return -1
           
       
# photo=db.session.query(Upload).order_by(Upload.create_time.desc()).filter_by(cafe_id=202).limit(15).all()
# photo=Upload.query.order_by(Upload.create_time.desc()).filter_by(cafe_id=202).limit(15).all()
# for i in photo:
#     a=i.photo_url

# a=Score_rec.query.with_entities(func.avg(Score_rec.comfort),func.avg(Score_rec.vacancy)).filter_by(cafe_id=183).scalar()
# print(a)
# print(type(a))
# b=db.session.execute('SELECT avg(wifi) as wifi_avg ,avg(quiet) as quiet_avg FROM `score_rec` where cafe_id=2')
# b=db.engine.execute('SELECT * FROM `score_rec` where cafe_id=2').first()
# print(b)
# update_list=Score_rec.query.filter_by(cafe_id=2022).all()
# count=0
# value=0
# for update in update_list:
    
#     if update.price:
#         count+=1
#         value+=update.price
# cafe.quiet                  
# update=db.session.execute('SELECT avg(price), avg(wifi),avg(vacancy) ,avg(quiet),avg(comfort),avg(drinks),avg(food),avg(view),avg(toilets),avg(speed) FROM `score_rec` where cafe_id=2').first()
# cafe=Cafes.query.filter_by(id=2).first()   



# data={
#         'price':update[0],'wifi':update[1],'vacancy':update[2],
#         'quiet':update[3],'comfort':update[4],'drinks':update[5],'food':update[6],
#         'view':update[7],'toilets':update[8],'speed':update[9],
        
#     }
# print(data)


# rating=Score_rec(user_id=4,cafe_id='2022',wifi='3',\
#         speed='03',vacancy='3',comfort='3',quiet='3',\
#         food='3',drinks='3',price='3',view='3',toilets='3')


# rating.insert()
# cafe_id='2022'
# update=db.session.execute(f'SELECT avg(price), avg(wifi),avg(vacancy) ,avg(quiet),avg(comfort),avg(drinks),avg(food),avg(view),avg(toilets),avg(speed) FROM `score_rec` where cafe_id={cafe_id}').first()
# cafe=Cafes.query.filter_by(id=cafe_id).first()
# print(cafe)
# update_data={
# 'price':update[0],'wifi':update[1],'vacancy':update[2],
# 'quiet':update[3],'comfort':update[4],'drinks':update[5],'food':update[6],
# 'view':update[7],'toilets':update[8],'speed':update[9]
# }
# print(update_data)
# order=db.session.query(Photo).order_by(Photo.create_time.desc()).filter_by(cafe_id=1).limit(15).all()
# print(order)

# order=Photo.query.order_by(Photo.create_time.desc()).filter_by(cafe_id=1).limit(15).all()
# print(order)


# from datetime import datetime
# print(datetime.now().strftime('%Y%m%d%H%M'))

# query_floor=Message.query.filter_by(cafe_id=2).all()
# if query_floor:
#     print('t')
# else:
#     print('f')
# print(query_floor)
# msg_t=[]
# msg_list=Message.query.join(Users,Users.user_id==Message.user_id).order_by(Message.floor).add_columns(Users.avatar).filter_by(cafe_id=1).all()

# print(Message.query.join(Users,Users.user_id==Message.user_id).order_by(Message.floor).add_columns(Users.avatar))
from datetime import datetime
msg_t=[]
msg_list=Message.query.order_by(Message.floor).filter_by(cafe_id=1).all()


# for msg in msg_list:
#     msg_dict=msg.as_dict()
       
#     msg_dict['create_time']=datetime.strftime(msg.create_time,"%Y-%m-%d %H:%M")
#     # msg_dict['create_time']=msg.create_time.strftime('%-m月%-d日%H:%M')    
            
#     msg_t.append(msg_dict)
                
# print(msg_t)   
# a=Message.query.order_by(Message.create_time).filter_by(cafe_id=1).all()
# print(a)


# a=db.session.query(Cafes, Photo).join(Photo, Photo.cafe_id == Cafes.id, isouter=True).group_by(Cafes.id).limit(20).offset(0*20).count()
# print(a)
# for c in a:
#     if c[1]:
#         print(c[1].photo_url)
#     else:
# #         print('none')
# cafe_msg=View.query.order_by(View.cafe_msg_count.desc()).limit(8).all().as_dict()
cafe_rating=db.session.query(Cafes, Photo).join(Photo, Photo.cafe_id == Cafes.id, isouter=True).filter(Cafes.id==1).group_by(Cafes.id).first()
print(cafe_rating)