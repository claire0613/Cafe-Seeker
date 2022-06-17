import sys,datetime,os
sys.path.append("..")
from flask import Flask  
from sqlalchemy import Index,text,or_
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy import Index,text,or_
# from model.models import Cafes, Score_rec,Cafes_like,Message,Rank
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from sqlalchemy.sql import expression

from werkzeug.security import generate_password_hash,check_password_hash
load_dotenv()
DB_HOST= os.getenv("SERVER_HOST")
DB_USER= os.getenv("SERVER_USER")
DB_PASSWORD=os.getenv("SERVER_PASSWORD")
DB_NAME= os.getenv("SERVER_DATABSE")
app=Flask(__name__)
# 設定資料庫位置，並建立 app
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
    "pool_recycle": 300,
    'pool_timeout': 900,
    'pool_size': 10,
    'max_overflow': 5,
}




db = SQLAlchemy(app)

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
        #機台在美國(晚台灣8hr)
        update.update_time=datetime.datetime.now()+ datetime.timedelta(hours=8)
        update.update()
    else:
        cafe_favor=Cafes_like.query.filter_by(cafe_id=cafe.id).count()
        cafe_rating=Score_rec.query.filter_by(cafe_id=cafe.id).count()
        cafe_msg=Message.query.filter_by(cafe_id=cafe.id).count()
        view=Rank(cafe_id=cafe.id,search_count=cafe.search_count,cafe_favor_count=cafe_favor,cafe_msg_count=cafe_msg,city_id=cafe.city_id)
        view.insert()
time=datetime.datetime.now()+ datetime.timedelta(hours=8)
print(time)
    
    
    
    
    
    
   
    
    