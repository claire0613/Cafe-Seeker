import mysql.connector.pooling
import os
from dotenv import load_dotenv
load_dotenv()
dbconfig = {
        'host': os.getenv("SERVER_HOST"),
        'user': os.getenv("SERVER_USER"),
        'password': os.getenv("SERVER_PASSWORD"),
        'database': os.getenv("SERVER_DATABSE"),
        'charset': 'utf8',
        
    }
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="pool",
    pool_size=5,
    pool_reset_session=True,
    **dbconfig
)
connection = connection_pool.get_connection()


mycursor = connection.cursor()
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS cafes(
    id BIGINT AUTO_INCREMENT, name VARCHAR(255) NOT NULL , area VARCHAR(100) NOT NULL, 
    city VARCHAR(255) NOT NULL, address VARCHAR(255) NOT NULL , transport TEXT, google_maps TEXT, 
    latitude DOUBLE , longitude DOUBLE ,open_hours JSON,open_time VARCHAR(255),google_rating FLOAT,wifi FLOAT, speed FLOAT,socket VARCHAR(10),
    vacancy FLOAT,comfort FLOAT, quiet FLOAT, food FLOAT, drinks FLOAT, price FLOAT, view FLOAT, toilets FLOAT,
    music BOOLEAN, smoking BOOLEAN, standing_tables BOOLEAN, outdoor_seating BOOLEAN, cash_only BOOLEAN, animals BOOLEAN,limited_time VARCHAR(10),
    facebook TEXT,instagram TEXT, telephone VARCHAR(100), website TEXT,
    images JSON, review JSON, content TEXT,google_place_id VARCHAR(255),cafe_nomad_id VARCHAR(255),
    PRIMARY KEY (id)) ENGINE=InnoDB, charset=utf8; 
    """
)  # InnoDB 儲存引擎 具備Commit, Rollback和當掉復原的事務處理能力，可保護使用者資料
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS score_his(
    cafe_id BIGINT ,cafe_name VARCHAR(255) NOT NULL UNIQUE, speed JSON,vacancy JSON,comfort JSON, quiet JSON, food JSON, drinks JSON, price JSON, view JSON, toilets JSON,
    PRIMARY KEY (scr_id),
    FOREIGN KEY(cafe_id)REFERENCES cafes(id)ON DELETE CASCADE) ENGINE=InnoDB, charset=utf8; 
    """
)









# mycursor.execute("""
#    CREATE TABLE IF NOT EXISTS users(
#       id BIGINT  AUTO_INCREMENT,
#       name VARCHAR(255) NOT NULL, 
#       email VARCHAR(255) NOT NULL UNIQUE, 
#       password VARCHAR(255) NOT NULL, 
#       PRIMARY KEY (id)) charset=utf8;
#    """
# )

# mycursor.execute("""
#    CREATE TABLE IF NOT EXISTS bookings(
#     id BIGINT NOT NULL AUTO_INCREMENT, 
#     attractionId INT NOT NULL, 
#     userId BIGINT NOT NULL, 
#     date DATE NOT NULL, 
#     time VARCHAR(255) NOT NULL, 
#     price INT NOT NULL,
#     status INT DEFAULT 1,
#     totalPrice INT ,
#     ordernum varchar(255) DEFAULT NULL,
#     rec_trade_id VARCHAR(255)DEFAULT NULL,
#     phone VARCHAR(255),
#     PRIMARY KEY(id),
#     FOREIGN KEY(userId)REFERENCES users(id)ON DELETE CASCADE) charset=utf8;
#    """
# )

connection.commit()




