# Cafe-Seeker

本專案是整合"CafeNoamd" & "Cafe and Cowork"的資料並且加入多條件查詢功能的咖啡廳清單網站。
This project is a cafe list website that integrates the data of "Cafe Noamd" and "Cafe and Cowork"
with adding a multi-condition query function.
## Main Function
### Search System:
-Inputing keyword and multi-condition can search the cafes that the best matches your expectation.
### Update Ranking:
-The ranking is updated every three hours, like search ranking and saving ranking for cafes. 
### Upload and Message System：
-User can upload the photos for sharing and  leave, click the like button and delete the comment. 
### Member System：
-Organize records about user's favorite cafes and uploaded photos for cafes, supporting to modify the username.

## Demo

-Website URL : https://clairego.com/

-測試帳號

- 帳號 : test1@gmail.com
- 密碼 : test1

## Server Architecture

![image](https://user-images.githubusercontent.com/93002296/173863774-3c766ea4-d983-4122-aa59-62fad41866c5.png)


## MySQL EER Diagram
![image](https://user-images.githubusercontent.com/93002296/173243687-e0ae566c-0ae7-4780-b9d7-4ffb029bc4a7.png)

##  Technique
### Backend Tech Stack
- Python / Flask
  
- Web Crawler
    - source
        - Cafe Nomad
        - Cafe and Cowork

<br/>
- Authentication
  - JSON Web Token (JWT)
<br/>
- Database
    - MySQL
    - Redis
<br/>
- Cloud Service (AWS)
    - EC2
    - RDS
    - S3, CloudFront
    - ElastiCache
<br/>
- Tool
    - Docker (deploying web) 


### Front-End Tech Stack
- javasrcipt
- html
- css/scss

#### NetWork 
- NGINX 
  - Domain name system
  - support Http & Https

#### Version Cotrol
- Git/GitHub

## Contact

- 📞 Claire Liang
- 📧 claire0711@gmail.com




