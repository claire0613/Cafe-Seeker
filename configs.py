from dotenv import load_dotenv
import os
load_dotenv()

S3_ACCESS_KEY=os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY=os.getenv("S3_SECRET_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")
CDN_URL= os.getenv("CDN_URL")
SECRET_KEY=os.getenv("SECRET_KEY")
DB_HOST= os.getenv("SERVER_HOST")
DB_USER= os.getenv("SERVER_USER")
DB_PASSWORD=os.getenv("SERVER_PASSWORD")
DB_NAME= os.getenv("SERVER_DATABSE")
PLACE_KEY=os.getenv("GOOGLE_PLACES_API_KEY")
basepath = os.path.join(os.path.dirname(__file__), "static", "upload")
REDIS_HOST = os.getenv("REDIS_HOST")

SQLALCHEMY_ENGINE_OPTIONS={
    "pool_pre_ping": True,
    "pool_recycle": 60,
    'pool_timeout': 180,
    'pool_size': 20,
    'max_overflow': 40,
}
SQLALCHEMY_DATABASE_URI= f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"

SQLALCHEMY_TRACK_MODIFICATIONS=False


DEBUG = False
JSON_AS_ASCII = False
TEMPLATES_AUTO_RELOAD = True

# app.config["JSON_AS_ASCII"] = False
# app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.config["JSON_SORT_KEYS"]=False
# app.config["SECRET_KEY"] = SECRET_KEY
# app.config['SQLALCHEMY_DATABASE_URI'] 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = 




# class Config:
#     DEBUG = False
#     TESTING = False
# class Development(Config):
#     ENV = 'development'
#     DEBUG = True
#     JSON_AS_ASCII = False
#     TEMPLATES_AUTO_RELOAD = True
#     SECRET_KEY = SECRET_KEY
#     REDIS_HOST = REDIS_HOST
#     TEMPLATES_AUTO_RELOAD = True    

#     SLALCHEMY_DATABASE_URI=f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
#     SQLALCHEMY_ENGINE_OPTIONS={
#     "pool_pre_ping": True,
#     "pool_recycle": 60,
#     'pool_timeout': 180,
#     'pool_size': 20,
#     'max_overflow': 40,
# }

# class Production(Config):
    
#     ENV = 'Prodction'
#     DEBUG = False
#     JSON_AS_ASCII = False
#     TEMPLATES_AUTO_RELOAD = True
    
#     SECRET_KEY = SECRET_KEY
#     SLALCHEMY_DATABASE_URI=f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
#     SQLALCHEMY_ENGINE_OPTIONS={
#     "pool_pre_ping": True,
#     "pool_recycle": 60,
#     'pool_timeout': 180,
#     'pool_size': 20,
#     'max_overflow': 40,
# }
#     REDIS_HOST = REDIS_HOST

