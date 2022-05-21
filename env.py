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