# VERSION 0.01
#
# node.js and express on debian:wheezy

FROM debian:wheezy

MAINTAINER Matt Selph <matt.selph@gmail.com> | github.com/mattselph

# install node.js
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs
RUN npm install express --save
