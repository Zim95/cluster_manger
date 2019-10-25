FROM ubuntu:16.04
MAINTAINER Namah shresthanamah@gmail.com
RUN apt-get update -y
RUN apt-get install python3-pip python3-dev build-essential -y
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]