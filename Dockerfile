# pull ubuntu 16.04
FROM ubuntu:16.04

# add maintainer
MAINTAINER Namah shresthanamah@gmail.com

# update repositories
RUN apt-get update -y

# install all build essentials and python3
RUN apt-get install python3-pip python3-dev build-essential -y

# move into app directory inside docker
COPY . /app
WORKDIR /app

# install requirements
RUN pip3 install -r requirements.txt

# execute the app
ENTRYPOINT ["python3"]
CMD ["app.py"]