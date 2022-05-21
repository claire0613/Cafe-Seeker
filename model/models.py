
import mysql.connector.pooling
from mysql.connector import Error
import json
import os
from datetime import datetime, timedelta
from sqlalchemy import or_
from dotenv import load_dotenv
load_dotenv()
# from flask import Flask,request,jsonify
# from flask_sqlalchemy import SQLAlchemy

# from env import DB_USER,DB_PASSWORD,DB_HOST,DB_NAME
# # app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
# #     "pool_pre_ping": True,
# #     "pool_recycle": 300,
# #     'pool_timeout': 900,
# #     'pool_size': 10,
# #     'max_overflow': 5,
# # }

# db=SQLAlchemy()

# db.init_app(app)

# dbconfig = {
#         'host': os.getenv("SERVER_HOST"),
#         'user': os.getenv("SERVER_USER"),
#         'password': os.getenv("SERVER_PASSWORD"),
#         'database': os.getenv("SERVER_DATABSE"),
#         'charset': 'utf8',
        
#     }

# connection_pool = mysql.connector.pooling.MySQLConnectionPool(
#         pool_name="pool",
#         pool_size=5,
#         pool_reset_session=True,
#         **dbconfig
#     )

# def connection_db_commit(sql,value):
#     try:
#         connection = connection_pool.get_connection()
#         mycursor = connection.cursor()
#         mycursor.execute(sql, value)  
#         # Commit your changes
#         connection.commit()
#     except mysql.connector.Error as error:
#         print(f"Error while connecting to MySQL using Connection pool{error}")   
#         connection.rollback()
#         # reverting changes because of exception
#     finally:
#             # closing database connection.
#             if connection.is_connected():
#                 mycursor.close()
#                 connection.close()
# def connection_db_search(sql,value):
#     try:
#         connection = connection_pool.get_connection()
#         mycursor = connection.cursor()
#         mycursor.execute(sql, value)
#         result_list=[]
#         results=mycursor.fetchall()
#         if results:
#             for result in results:
#                 result=dict(zip(mycursor.column_names,result))
#                 result_list.append(result)
#         if connection.is_connected():
#             mycursor.close()
#             connection.close()        
#         return result_list
#     except mysql.connector.Error as error:
#         print(f"Error while connecting to MySQL using Connection pool{error}")   
#         connection.rollback()
            
      
   
# class Cafes():

#     def insert_data(self,name,area,city,address,transport,google_maps,latitude,longitude,open_hours,open_time,wifi=[],speed=[],socket='',\
#         vacancy,comfort,quiet,food,drinks,price,view,toilets,music,smoking,standing_tables,outdoor_seating,\
#         cash_only,animals,facebook,instagram,telephone,website,images,review,content,cafe_nomad_id,limited_time):

#         sql="""INSERT INTO cafes (name,area,city,address,transport,google_maps,latitude,longitude,open_hours,open_time,wifi,speed,socket,
#         vacancy,comfort,quiet,food,drinks,price,view,toilets,music,smoking,standing_tables,outdoor_seating,
#         cash_only,animals,facebook,instagram,telephone,website,images,review,content,cafe_nomad_id,limited_time) 
#         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
#         """
#         val=(name,area,city,address,transport,google_maps,latitude,longitude,open_hours,open_time,wifi,speed,socket,\
#         vacancy,comfort,quiet,food,drinks,price,view,toilets,music,smoking,standing_tables,outdoor_seating,\
#         cash_only,animals,facebook,instagram,telephone,website,images,review,content,cafe_nomad_id,limited_time)
#         result=connection_db_commit(sql,val)
#         if result:
#             return True
#         else:
#             return {'error':'upadate failed'}

        
        
        
#     @staticmethod       
#     def cafe_is_existing_nomad(search_name,address):
    
#         sql="SELECT * FROM cafes WHERE name=%s or address=%s"
#         val=(search_name,address)
#         result=connection_db_search(sql,val)
#         return result
        
#     def update_data_nomad(self,name,area,city,address,transport,google_maps,latitude,longitude,open_hours,open_time,wifi,speed,socket,
#         vacancy,comfort,quiet,food,drinks,price,view,toilets,music,smoking,standing_tables,outdoor_seating,
#         cash_only,animals,facebook,instagram,telephone,website,images,review,content,cafe_nomad_id,limited_time):
#         sql="""UPDATE `cafes` SET area=%s,city=%s,address=%s,transport=%s,google_maps=%s,latitude=%s,longitude=%s,open_hours=%s,open_time=%s,wifi=%s,speed=%s,socket=%s,
#         vacancy=%s,comfort=%s,quiet=%s,food=%s,drinks=%s,price=%s,view=%s,toilets=%s,music=%s,smoking=%s,standing_tables=%s,outdoor_seating=%s,
#         cash_only=%s,animals=%s,facebook=%s,instagram=%s,telephone=%s,website=%s,images=%s,review=%s,content=%s,cafe_nomad_id=%s, limited_time=%s WHERE name=%s or address=%s
#         """
#         val=(area,city,address,transport,google_maps,latitude,longitude,open_hours,open_time,wifi,speed,socket,\
#         vacancy,comfort,quiet,food,drinks,price,view,toilets,music,smoking,standing_tables,outdoor_seating,\
#         cash_only,animals,facebook,instagram,telephone,website,images,review,content,cafe_nomad_id,limited_time,name,address)
#         result=connection_db_commit(sql,val)
#         if result:
#             return result
#         else:
#             return {'error':'upadate failed'}
#     @staticmethod
#     def update_place_id(area,city,google_place_id,google_rating,name):
#         sql="UPDATE `cafes` SET area=%s,city=%s google_place_id=%s ,google_rating=%s WHERE name=%s"
#         val=(area,city,google_place_id,google_rating,name)
#         result=connection_db_commit(sql,val)
#         if result:
#             return result
#         else:
#             return {'error':'upadate failed'}
        
#     @staticmethod
#     def search_cafe_all():
#         sql="SELECT * FROM cafes "
#         val=()
#         result=connection_db_search(sql,val)
#         return result
        
# class Score_his():
    
#     @staticmethod
#     def insert_cafe_score_his(self,name,wifi=[],speed=[],vacancy=[],comfort=[],quiet=[],food=[],drinks=[],price=[],view=[],toilets=[]):
    
#         sql="""INSERT INTO cafes (name,wifi,speed,socket,vacancy,comfort,quiet,food,drinks,price,view,toilets) 
#                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
#             """
#         val=(name,wifi,speed,vacancy,comfort,quiet,food,drinks,price,view,toilets)
#         result=connection_db_commit(sql,val)
#         if result:
#             return True
#         else:
#             return {'error':'upadate failed'}
        
        
        
        
#     # def as_dict(self):
#     #     return{c.name: getattr(self, c.name) for c in self.__table__.columns}
    
from flask import Flask  
from flask_sqlalchemy import SQLAlchemy

import sys
sys.path.append("..")
from env import DB_USER,DB_PASSWORD,DB_HOST,DB_NAME
from sqlalchemy import Index
from sqlalchemy.dialects.mysql import DOUBLE

        
from werkzeug.security import generate_password_hash,check_password_hash
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

class Cafes(db.Model):
    __tablename__='cafes'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(255),nullable=False)
    area=db.Column(db.String(100),nullable=False)
    city=db.Column(db.String(100),db.ForeignKey('city_ref.city'),nullable=False)
    
    address=db.Column(db.String(255),nullable=False)
    transport=db.Column(db.Text)
    google_maps=db.Column(db.Text)
    latitude=db.Column(DOUBLE())
    longitude=db.Column(DOUBLE())
    open_hours=db.Column(db.JSON)
    open_time=db.Column(db.String(255))
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
    images=db.Column(db.JSON)
    review=db.Column(db.JSON)

    favor=db.Column(db.Integer)
    comment=db.Column(db.Integer)
    searching_count=db.Column(db.Integer)
    
    cafe_nomad_id=db.Column(db.String(255),unique=True)
    
    db_cafes_score_rec = db.relationship("Score_rec", backref="cafes")
    
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    @classmethod
    def search_nomad(cls,search_name,address):
        return cls.query.filter(or_(cls.name==search_name,cls.address==address)).first()

    
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
    @classmethod
    def update(cls):
        db.session.commit()
        
        
Index('cafe_id_name_index', Cafes.id, Cafes.name)    


            
        

    
    
class Score_rec(db.Model):
    __tablename__='score_rec'
    cafe_id=db.Column(db.Integer,db.ForeignKey('cafes.id'),primary_key=True,nullable=False)
    wifi=db.Column(db.JSON)
    speed=db.Column(db.JSON)
    vacancy=db.Column(db.JSON)
    comfort=db.Column(db.JSON)
    quiet=db.Column(db.JSON)
    food=db.Column(db.JSON)
    drinks=db.Column(db.JSON)
    price=db.Column(db.JSON)
    view=db.Column(db.JSON)
    toilets=db.Column(db.JSON)
    
    
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    @classmethod
    def search_id(cls,cafe_id):
        return cls.query.filter_by(cafe_id=cafe_id).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def update(cls):
        db.session.commit()
    

class Users(db.Model):
    __tablename__='users'
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),unique=True,nullable=False)
    pwd_hash=db.Column(db.String(255),nullable=False)
    
        
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns} 
        
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
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
    
Index('email_name_index',Users.email,Users.username)

class City_ref(db.Model):
    __tablename__='city_ref'
    
   
    city=db.Column(db.String(100),primary_key=True,nullable=False)
    city_id=db.Column(db.Integer,unique=True,autoincrement=True)
    city_tw=db.Column(db.String(100),nullable=False)
    
    db_cafes_city_ref_=db.relationship("Cafes", backref="city_ref")

    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns} 
        
    
# class Post(db.Model):
    

