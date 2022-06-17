from data.api_helper import key_search_detail
from . import api
import boto3
from model.models import City_ref, db,Cafes,Score_rec,Photo,Cafes_like,Users
from flask import *
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename
import jwt,re,sys,os
from datetime import datetime
from datetime import datetime, timedelta
sys.path.append("..")
from dotenv import load_dotenv
load_dotenv()
from .photo import allowed_file



@api.route('/member/favor',methods=['GET'])
def get_member_cafe_favor():
    try:
        token_cookie=request.cookies.get('user_cookie')
        m_cafe_page=int(request.args.get('page'))
        
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            cafe_id_list=[]
            result_list=[]
            next_page=0
            cafe_favor=Cafes_like.query.filter_by(user_id=user_id).offset(m_cafe_page*10).limit(10).all()
           
            for cafe in cafe_favor:
                cafe_id_list.append(cafe.cafe_id)
            
            for item in cafe_id_list:
                data= db.session.execute(f"select c.id,c.name,c.area,c.wifi,c.drinks,p.photo_url from cafes as c left join photo as p on p.cafe_id=c.id \
                                            WHERE c.id={item} GROUP By c.id ").first()
                result_list.append(data)
            answer=key_search_detail(result_list)
            if len(cafe_favor)<6:
                next_page = None
            else:
                next_page = m_cafe_page+1
           
                
        return jsonify({ "data": answer,"nextPage":next_page})
        
    except:
        return {"error": True, "message": "伺服器內部錯誤"}, 500
    
@api.route('/member/photo',methods=['GET'])
def get_member_photo():
    try:
        token_cookie=request.cookies.get('user_cookie')
        m_photo_page=int(request.args.get('page'))
        
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            result_list=[]
            photo_list=Photo.query.filter_by(user_id=user_id).offset(m_photo_page*10).limit(10).all()
            
            for photo in photo_list:
                result=photo.as_dict()
                result['create_time']=datetime.strftime(photo.create_time, "%Y-%m-%d %H:%M")
                result['cafe_name']=Cafes.query.filter_by(id=photo.cafe_id).first().name
                result_list.append(result)
            if len(photo_list)<6:
                next_page = None
            else:
                next_page = m_photo_page+1
                
            
        return jsonify({ "data":result_list,"nextPage":next_page})
        
    except:
        return {"error": True, "message": "伺服器內部錯誤"}, 500
    
#更換大頭貼
@api.route('/member/userphoto',methods=['POST'])
def post_member_userphoto():
    try:
        token_cookie=request.cookies.get('user_cookie')
        if token_cookie:
            user=jwt.decode(token_cookie,os.getenv("SECRET_KEY"),algorithms=['HS256'])
            user_id = user["id"]
            now_user=Users.query.filter_by(user_id=user_id).first()
            image= request.files["file"] #接收檔案
            # print(now_user.id,image)
            if image and allowed_file(image.filename):
                    image.filename = secure_filename(image.filename)
                    record=datetime.now().strftime('%Y%m%d%H%M%S%f')
                    image_filename=f'{record}{user_id}_{image.filename}'
                    image_url=os.getenv("CDN_URL")+'cafe-seeker/useravatar/'+image_filename
                    s3 = boto3.client('s3', 
                    aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
                    aws_secret_access_key=os.getenv("S3_SECRET_KEY")
                    )
                    
                    s3.upload_fileobj(image,os.getenv("S3_BUCKET"),'cafe-seeker/useravatar/'+image_filename)
                    now_user.avatar=image_url
                    now_user.update()
                   
                    message = {"ok": True}
                    response = make_response(jsonify(message))
                    
                    token = jwt.encode({
                        "id": user['id'],
                        "username": user['username'],
                        "email": user['email'],
                         "avatar":image_url,
                        "exp": datetime.utcnow() + timedelta(days=1)
                        }, os.getenv("SECRET_KEY"), algorithm='HS256')
                    response.set_cookie(key='user_cookie', value=token)
                    return response
            # return image            
            
        else:
            return jsonify({"error": True,"message":"未登入"})
        
    except:
        return {"error": True, "message": "伺服器內部錯誤"}, 500
    
    
