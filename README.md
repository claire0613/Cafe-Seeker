# Cafe-Seeker

本專案是整合"CafeNoamd" & "Cafe and Cowork"的資料並且加入多條件查詢功能的咖啡廳清單網站。
This project is a cafe list website that integrates the data of "Cafe Noamd" and "Cafe and Cowork"
with adding a multi-condition query function.
## Main Function
### 查詢系統 (Query System):
-利用關鍵字以及多條件篩選尋找理想的店家。
-Input keyword and multi-condition can search the store that the best matches your expectation.
### 定時刷新排名 (Update Ranking):
-每三小時固定更新排名，例如搜尋店家排名以及最多人收藏的店家排名。
-The ranking is updated every three hours, like search ranking and saving ranking for cafes. 
### 上傳與留言系統(Upload and Message System)：
-使用者可以在店家頁面中進行上傳照片、留言、按喜愛並且刪除留言等功能。
-User can upload the photos for sharing and  leave, click the like button and delete the comment. 
-### 會員系統 (Member System)：
-整理喜愛的店家收藏以及上傳店家照片的紀錄整理、修改姓名等功能。
-Organize records about user's favorite cafes and uploaded photos for cafes, supporting to modify the username.

## Demo

-Website URL : https://clairego.com/

-測試帳號

- 帳號 : test1@gmail.com
- 密碼 : test1

## Server Architecture

![image](https://user-images.githubusercontent.com/93002296/173636339-7efbbb21-8499-4972-9825-7d1e34f15ed7.png)


## MySQL EER Diagram
![image](https://user-images.githubusercontent.com/93002296/173243687-e0ae566c-0ae7-4780-b9d7-4ffb029bc4a7.png)

##  Technique
### Language / Web Framework
- Python / Flask
#### Database
- MySQL
    - Using Index and Fulltext Index for speeding up query efficiency
- Redis 
    -Speed up getting the cafe ranking data.

#### Cloud Service (AWS)
- EC2
- RDS
- S3, CloudFront
- ElastiCache
#### Tool
- Docker
- NGINX
- Domain Name System (DNS)
- SSL (Let's Encrypt)

#### Version Cotrol
- Git/GitHub







