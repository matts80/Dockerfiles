# riak
#
# VERSION	0.0.1

FROM debian:wheezy
MAINTAINER Matt Selph <matt.selph@gmail.com>

RUN apt-get update && apt-get install -y curl
RUN curl https://packagecloud.io/install/repositories/basho/riak/script.deb | bash
RUN apt-get install riak=2.0.0-1
