# Cafe-Seeker

本專案是整合"CafeNoamd" & "Cafe and Cowork"的資料並且加入多條件查詢功能的咖啡廳清單網站。

This project is a cafe list website that integrates the data of "Cafe Noamd" and "Cafe and Cowork"
with adding a multi-condition query function.

- Website URL : https://clairego.com/

- 測試帳號

- 帳號 : test1@gmail.com
- 密碼 : test1


## Demo
### Search System:
- Using keywords and selecting multipule condition to meet a customer's requirement.
![image](https://github.com/claire0613/gif/blob/main/city_list.gif)

### Rank & Shop Page:
- Users can find the latest popular cafes or the most people inquired cafes through the Rank.
- In the cafe's pages, user can see what 
![image](https://github.com/claire0613/gif/blob/main/shop.gif)


## Main Function
### Search System:
- By MySQL Inedex and FullIndex, users can input keywords and select multiple conditions to meet a customer's requirement.
### Ranking:
- The rank of cafes would automatically be updated every three hours, like search ranking and saving ranking for cafes.
- Use Redis as Cache to get faster data.
### Upload and Message System：
- Uplaod photos to Amazon S3 hosting with AWS Cloudfront.
- Users can upload the photos for sharing and  leave, delete the comment on the page of cafe's shop. 
### Member System：
- Using Json Web Token to authenticate users.
- Organize records about user's favorite cafes and uploaded photos for cafes, supporting to modify the username.



## Server Architecture

![image](https://user-images.githubusercontent.com/93002296/174286883-cb22332b-d4ba-46cb-bb78-b223e843da4e.png)


## MySQL EER Diagram
![image](https://user-images.githubusercontent.com/93002296/173243687-e0ae566c-0ae7-4780-b9d7-4ffb029bc4a7.png)




##  Technique
### Backend Tech Stack

- Language / Web Framwork 
  - Python / Flask

- Authentication
  - JSON Web Token (JWT)
  - werkzeug.security (Encode & Verify Password)

- Database
    - MySQL
    - Redis
    
- Cloud Service (AWS)
    - EC2
    - RDS
    - S3, CloudFront
    - ElastiCache

- Tool
    - Docker (deploying web) 

### Front-End Tech Stack
- JavaScript 
- HTML
- CSS / SCSS

#### NetWork 
- NGINX 
  - Domain name system
  - Support Http & Https

#### Version Cotrol
- Git/GitHub

## Contact

- 📞 Claire Liang
- 📧 claire0711@gmail.com




