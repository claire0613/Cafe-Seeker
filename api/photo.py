from . import api
import boto3
from model.models import City_ref, db,Cafes,Score_rec,Photo
from flask import *
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename
import jwt,re,sys,os
from datetime import datetime
import logging
sys.path.append("..")
from dotenv import load_dotenv
load_dotenv()

@api.route('/photo/upload', methods=['POST'])
def post_photo(): 
    try:
        token_cookie = request.cookies.get('user_cookie')
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            cafe_id=request.form['cafe_id']
            
            file_list= request.files.getlist("file[]") #接收多檔案
            for image in file_list:
                if image and allowed_file(image.filename):
                        image.filename = secure_filename(image.filename)
                        record=datetime.now().strftime('%Y%m%d%H%M%S%f')
                        image_filename=f'{record}{user_id}_{image.filename}'
                        image_url=os.getenv("CDN_URL")+'cafe-seeker/userupload/'+image_filename
                        s3 = boto3.client('s3', 
                        aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
                        aws_secret_access_key=os.getenv("S3_SECRET_KEY")
                        )
                        
                        s3.upload_fileobj(image,os.getenv("S3_BUCKET"),'cafe-seeker/userupload/'+image_filename)
                        photo=Photo(user_id=user_id,cafe_id=cafe_id,photo_name=image_filename,photo_url=image_url)
                        photo.insert()
            return jsonify({'data':True})
            
    except Exception as e:
        logging.error(e)
        return jsonify({ "error": True, "message": "伺服器內部錯誤" })

@api.route('/photo/upload',methods=['GET'])
def get_photo():
    try:
        cafe_id=request.args.get('cafe_id')
        data=Photo.query.order_by(Photo.create_time.desc()).filter_by(cafe_id=cafe_id).limit(15).all()
        photo_url_list=[]
        if data:
            for photo in data:
                photo_url_list.append(photo.photo_url)
                

            return jsonify({'photo_url_list':photo_url_list})

    except:
        return {"error": True, "message": "伺服器內部錯誤"}, 500
@api.route('/photo/upload',methods=['DELETE'])
def delete_photo():
    try:
        data=request.json
        photo_id=data['photo_id']
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            data=request.json
            photo=Photo.query.filter_by(photo_id=photo_id,user_id=user_id).first()
           
            photo_name=photo.photo_name
            photo.delete()
            s3 = boto3.client('s3', 
            aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("S3_SECRET_KEY")
            )
            
            s3.delete_object(Bucket=os.getenv("S3_BUCKET"), Key=f'cafe-seeker/userupload/{photo_name}')
            
            
            return jsonify({ "ok": True })
        else:
            return jsonify({ "error": True, "message": "未登入系統，拒絕存取" })
    except:
        return {"error": True, "message": "伺服器內部錯誤"}, 500

def allowed_file(filename):
    
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {"png", "jpg", "jpeg"}



		