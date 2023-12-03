FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
##Create app directory
WORKDIR /app 

#copy all the code to app directory
COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]