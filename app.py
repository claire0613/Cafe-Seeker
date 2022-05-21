from flask import *
from flask_sqlalchemy import SQLAlchemy
from env import DB_USER,DB_PASSWORD,DB_HOST,DB_NAME,SECRET_KEY
from model.models import db
from api.cafes import api

app=Flask(__name__)
app.register_blueprint(api, url_prefix="/api")
# register blueprint






# 設定資料庫位置，並建立 app

app.config["JSON_AS_ASCII"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["JSON_SORT_KEYS"]=False
app.config["SECRET_KEY"] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
    "pool_recycle": 60,
    'pool_timeout': 180,
    'pool_size': 10,
    'max_overflow': 5,
}

# with app.app_context():
#     db.create_all() #創建所有table,如果不存在會自動創建

db.init_app(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/shop/<id>")
def shop(id):
    return render_template("shop.html")

@app.route("/<city>")
def city(city):
    return render_template("city.html")

@app.route("/<city>/list")
def city_list(city):
    return render_template("citylist.html")
@app.route("/search",methods=['GET'])
def search():
    return render_template("search.html")






@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)