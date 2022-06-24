import sys,os
sys.path.append("..")
from dotenv import load_dotenv
from requests import delete
load_dotenv()
from flask import Flask  
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import expression
from sqlalchemy import Index,text,or_
from sqlalchemy.dialects.mysql import DOUBLE
from werkzeug.security import generate_password_hash,check_password_hash
import redis
import json
from decimal import *
import configs
from configs import REDIS_HOST




app=Flask(__name__)
# 設定資料庫位置，並建立 app
app.config.from_object(configs)


db = SQLAlchemy(app)

class Redis_set:
    def __init__(self):
        self.redis_set = redis.Redis(host=REDIS_HOST,port=6379,decode_responses=True)

redis_db = Redis_set()


class Cafes(db.Model):
    __tablename__='cafes'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(255),unique=True,nullable=False)
    area=db.Column(db.String(100),nullable=False)
    city_id=db.Column(db.Integer,db.ForeignKey('city_ref.city_id'),nullable=False)
    address=db.Column(db.String(255),nullable=False)
    transport=db.Column(db.Text)
    google_maps=db.Column(db.Text)
    latitude=db.Column(DOUBLE())
    longitude=db.Column(DOUBLE())
    open_hours=db.Column(db.JSON)
    open_time=db.Column(db.String(255))
    rating=db.Column(db.Float)
    wifi=db.Column(db.Float)
    speed=db.Column(db.Float)
    vacancy=db.Column(db.Float)
    comfort=db.Column(db.Float)
    quiet=db.Column(db.Float)
    food=db.Column(db.Float)
    drinks=db.Column(db.Float)
    price=db.Column(db.Float)
    view=db.Column(db.Float)
    toilets=db.Column(db.Float)
    socket=db.Column(db.String(10))
    limited_time=db.Column(db.String(10))
    music=db.Column(db.Boolean)
    smoking=db.Column(db.Boolean)
    standing_tables=db.Column(db.Boolean)
    outdoor_seating=db.Column(db.Boolean)
    cash_only=db.Column(db.Boolean)
    animals=db.Column(db.Boolean)
    single_selling=db.Column(db.Boolean)
    dessert_selling=db.Column(db.Boolean)
    meal_selling=db.Column(db.Boolean)
    facebook=db.Column(db.Text)
    instagram=db.Column(db.Text)
    telephone=db.Column(db.String(100))
    website=db.Column(db.Text)
  
    search_count= db.Column(db.Integer, server_default=text("0"), nullable=False)
    cafe_nomad_id=db.Column(db.String(255),unique=True)
    
    db_cafes_score_rec = db.relationship("Score_rec", backref="cafes")
    db_cafes_cafes_like = db.relationship("Cafes_like", backref="cafes")

    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    @classmethod
    def search_nomad(cls,search_name):
        return cls.query.filter(cls.name==search_name).first()

    
    @classmethod
    def search_all(cls):
        return cls.query.all()
    @classmethod
    def search_by_name(cls,search_name):
        return cls.query.filter_by(name=search_name).all()
    def search_by_id(cls,search_id):
        return cls.query.filter_by(id=search_id).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
        
        
Index('cafe_id_name_index', Cafes.id, Cafes.name) 
   
    
class Score_rec(db.Model):
    __tablename__='score_rec'
    scr_id=db.Column(db.Integer,primary_key=True,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.user_id', ondelete='CASCADE'),nullable=False)
    cafe_id=db.Column(db.Integer,db.ForeignKey('cafes.id', ondelete='CASCADE'),nullable=False)
    wifi=db.Column(db.Float)
    speed=db.Column(db.Float)
    vacancy=db.Column(db.Float)
    comfort=db.Column(db.Float)
    quiet=db.Column(db.Float)
    food=db.Column(db.Float)
    drinks=db.Column(db.Float)
    price=db.Column(db.Float)
    view=db.Column(db.Float)
    toilets=db.Column(db.Float)
    create_time = db.Column(db.DateTime, server_default=text('NOW()'))
    
    
    
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    @classmethod
    def search_id(cls,cafe_id):
        return cls.query.filter_by(cafe_id=cafe_id).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    

class Users(db.Model):
    __tablename__='users'
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),unique=True,nullable=False)
    pwd_hash=db.Column(db.String(255),nullable=False)
    avatar = db.Column(db.String(255), server_default="https://d2ltlh9sj9r3jz.cloudfront.net/cafe-seeker/images/user.png")
    verify=db.Column(db.Boolean,server_default=expression.false())
    identity=db.Column(db.Integer)
    
    db_users_score_rec = db.relationship("Score_rec", backref="users")    
    db_users_cafes_like = db.relationship("Cafes_like", backref="users")
    db_users_message = db.relationship("Message", backref="users")   
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns} 
        
    

    
    @classmethod    
    def search_by_id(cls,search_id):
        return cls.query.filter_by(user_id=search_id).first()
       
    
    @property   
    def password(self):
       raise AttributeError('password is not a readable attribute!')
   
    @password.setter
    def password(self,password):
       self.pwd_hash=generate_password_hash(password)
  
    def verify_password(self,pwd):
        return check_password_hash(self.pwd_hash,pwd)
    def update(self):
        db.session.commit()
Index('email_name_index',Users.email,Users.username)

class Cafes_like(db.Model):
    __tablename__ = 'cafes_like'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    cafe_id = db.Column(db.Integer, db.ForeignKey('cafes.id', ondelete='CASCADE'), nullable=False)
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}

Index('users_cafes_index',Cafes_like.user_id, Cafes_like.cafe_id)

class City_ref(db.Model):
    __tablename__='city_ref'
    
    city_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    city=db.Column(db.String(100),unique=True,nullable=False)
    city_tw=db.Column(db.String(100),nullable=False)
    
    db_cafes_city_ref_=db.relationship("Cafes", backref="city_ref")

    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns} 
        
class Station_ref(db.Model):
    __tablename__='station_ref'
    station_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    station=db.Column(db.String(255),unique=True,nullable=False)
    station_tw=db.Column(db.String(255),nullable=False)
   
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns} 
class Photo(db.Model):
    __tablename__='photo'
    photo_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    cafe_id=db.Column(db.Integer, db.ForeignKey('cafes.id', ondelete='CASCADE'), nullable=False)
    photo_url=db.Column(db.Text, nullable=False)
    photo_name=db.Column(db.String(255),nullable=False)
    create_time = db.Column(db.DateTime, server_default=text('NOW()'))
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}


class Message(db.Model):
    __tablename__='message'
    msg_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    cafe_id=db.Column(db.Integer, db.ForeignKey('cafes.id', ondelete='CASCADE'), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    msg_content=db.Column(db.Text, nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    like_count = db.Column(db.Integer, server_default=text("0"), nullable=False)
    create_time = db.Column(db.DateTime, server_default=text('NOW()'))
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    
class Message_like(db.Model):
    __tablename__ = 'message_like'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    msg_id = db.Column(db.Integer, db.ForeignKey('message.msg_id', ondelete='CASCADE'), nullable=False)
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}

    

Index('message_like_user_index', Message_like.msg_id, Message_like.user_id)
class Update_detail(db.Model):
    __tablename__='update_detail'
    upd_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    socket=db.Column(db.String(10))
    limited_time=db.Column(db.String(10))
    music=db.Column(db.Boolean)
    smoking=db.Column(db.Boolean)
    standing_tables=db.Column(db.Boolean)
    outdoor_seating=db.Column(db.Boolean)
    cash_only=db.Column(db.Boolean)
    animals=db.Column(db.Boolean)
    single_selling=db.Column(db.Boolean)
    dessert_selling=db.Column(db.Boolean)
    meal_selling=db.Column(db.Boolean)
    facebook=db.Column(db.Text)
    instagram=db.Column(db.Text)
    telephone=db.Column(db.String(100))
    website=db.Column(db.Text)
    review=db.Column(db.JSON)
    status=db.Column(db.Boolean)
    create_time = db.Column(db.DateTime, server_default=text('NOW()'))
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    
class Rank(db.Model):
    __tablename__='rank'
    rank_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    cafe_id=db.Column(db.Integer, db.ForeignKey('cafes.id', ondelete='CASCADE'), nullable=False)
    search_count=db.Column(db.Integer, server_default=text("0"), nullable=False)
    cafe_favor_count=db.Column(db.Integer, server_default=text("0"), nullable=False)
    cafe_rating_count=db.Column(db.Integer, server_default=text("0"), nullable=False)
    cafe_msg_count=db.Column(db.Integer, server_default=text("0"), nullable=False)
    city_id=db.Column(db.Integer,db.ForeignKey('city_ref.city_id'),nullable=False)
    update_time=db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
    
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)
    


        
    

