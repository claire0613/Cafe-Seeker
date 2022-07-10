# Cafe-Seeker

本專案是整合"Cafe Nomad" & "Cafe and Cowork"的資料並且加入多條件查詢功能的咖啡廳清單網站。

This project is a cafe list website that integrates the data of "Cafe Nomad" and "Cafe and Cowork"
by adding a multi-condition query function.

- Website URL: https://clairego.com/
-  Test account (測試帳號)
  - email: test1@gmail.com
  - password: test1

##  Technique
- Develop with **Python** using **Flask** framework and deploy it to **AWS EC2** by **Docker** in public subnet.
- Use **AJAX & Web Crawler** to integrate **two Data Sources**  with **AWS RDS** in private subnet, then **normalize MySQL in 3NF**, using **Index** & **Full-Text Index** to facilitate query efficiencies.
- Use **Redis in AWS ElastiCache** as caches to store the popular board information for quickly getting data.
- Apply **AWS S3 Hosting with AWS CloudFront CDN service**  to store uploaded photos and  speed up their performance. 
- Set **Crontab**  to update the popular board automatically every three hours.
- Utilize **AWS ELB** for distributing network incoming traffic to automatically handle many workloads. 
- Design API with **REST** architectural style.
- Use **JSON Web Token** to authenticate users.

### Server Architecture
![image](https://user-images.githubusercontent.com/93002296/175466168-6ff6c88c-d589-4fc8-9c9a-4b766091f9d1.png)
### MySQL EER Diagram
![image](https://user-images.githubusercontent.com/93002296/178151667-41c11d27-0cce-4585-a482-408666560cb8.png)
### Back-End Tech Stack
- Language / Web Framework 
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
    - ELB
- Tool
    - Docker

### Front-End Tech Stack
- JavaScript 
- HTML
- CSS / SCSS

### Network 
- NGINX 
  - Domain name system
  - Support HTTP & HTTPS

### Version Control
- Git/GitHub

## Demo / Main Function
### Search System:
- Using keywords and selecting multiple conditions to meet a customer's requirement.
![image](https://github.com/claire0613/gif/blob/main/city_list.gif)

### Popular board:
- Users can find the latest popular cafes or the most inquired-for cafes through the board.
![image](https://github.com/claire0613/gif/blob/main/rank.gif)  

### Shop Page:
- On the cafe's page, users can see the shop's detailed information and save a favor, 
  leave, delete comments, or upload photos of this shop.
![image](https://github.com/claire0613/gif/blob/main/shop.gif)

### Member System：
- Organize records about users' favorite cafes and photos uploaded for cafes, supporting to modify the username.
![image](https://github.com/claire0613/gif/blob/main/member.gif)

## Contact
- 📞 Claire Liang
- 📧 claire0711@gmail.com




