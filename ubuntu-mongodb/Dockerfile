# VERSION 0.01
#
# Setup mongodb 2.6.4 on Ubuntu 14.04 LTS (Trusty Tahr)

FROM ubuntu:14.04
MAINTAINER Matt Selph <matt.selph@gmail.com> | github.com/mattselph

# install mongodb and start it
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list
RUN apt-get update  \ 
	&& apt-get install -y mongodb-org=2.6.4
RUN mkdir -p /data/db

EXPOSE 27017
ENTRYPOINT usr/bin/mongod
