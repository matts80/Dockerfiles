# VERSION 0.02
#
# Setup mongodb 3.0 on Ubuntu 14.04 LTS (Trusty Tahr)
#
# Version history
#	3/5/2015 - updated to mongodb 3.0; bumped to 0.02

FROM ubuntu:14.04
MAINTAINER Matt Selph <matt.selph@gmail.com> | github.com/mattselph

# install mongodb and start it
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo 'deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse' | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
RUN apt-get update  \ 
	&& apt-get install -y mongodb-org=3.0.0 \ 
			 mongodb-org-server=3.0.0 \ 
			 mongodb-org-shell=3.0.0 \ 
			 mongodb-org-mongos=3.0.0 \
			 mongodb-org-tools=3.0.0

RUN mkdir -p /data/db

EXPOSE 27017
ENTRYPOINT usr/bin/mongod
