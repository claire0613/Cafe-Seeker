# FROM python:3.8


# WORKDIR /AWSS3

# COPY . /AWSS3

# RUN pip3 install -r requirements.txt

# EXPOSE 80

# CMD [ "python3", "app.py","--host=0.0.0.0" ]


# use Python Image
FROM python:3.8-slim
#Set working dir (切換目錄)
WORKDIR /Cafe-Seeker
# Copy current direction into container /app
COPY . .
#install the need of package in requirement
RUN pip install -r requirements.txt
#Make port 3000 available to the world outside
EXPOSE 5000

#RUN app.py when launch
CMD ["python","app.py"]