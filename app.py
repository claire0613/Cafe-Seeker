from flask import *
from flask_sqlalchemy import SQLAlchemy
# from env import DB_USER,DB_PASSWORD,DB_HOST,DB_NAME,SECRET_KEY
from model.models import db
from api.cafes import api
from api.users import api
from api.rating import api
from api.photo import api
from api.message import api
from api.favor import api
from api.member import api
import configs
app=Flask(__name__)

#config for flask object
app.config.from_object(configs)


app.register_blueprint(api, url_prefix="/api")

# register blueprint

# 設定資料庫位置，並建立 app


db.init_app(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/rating/<cafe_id>")
def rating(cafe_id):
    return render_template("rating.html")

@app.route("/success/<scr_id>")
def rating_success(scr_id):
    return render_template("ratingsuccess.html")
@app.route("/fail/<scr_id>")
def rating_fail(scr_id):
    return render_template("ratingfail.html")


@app.route("/shop/<id>")
def shop(id):
    return render_template("shop.html")

@app.route("/rank/<city>")
def city(city):
    return render_template("rank.html")

@app.route("/<city>/list")
def city_list(city):
    return render_template("citylist.html")

@app.route("/keyword",methods=['GET'])
def keyword():
    return render_template("keyword.html")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route("/member")
def member():
    return render_template("member.html")
@app.route("/insertcafe")
def insertCafe():
    return render_template("insertcafe.html")

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500



@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)