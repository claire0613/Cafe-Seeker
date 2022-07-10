from flask import *
from flask_sqlalchemy import SQLAlchemy
from model.models import db
from controller import api
import configs
app=Flask(__name__)

app.config.from_object(configs)
db.init_app(app)

# register blueprint
app.register_blueprint(api, url_prefix="/api")

#main route
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