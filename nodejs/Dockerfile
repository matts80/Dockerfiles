# VERSION 0.02
#
# node.js, express, and mysql on debian:wheezy

FROM debian:wheezy

MAINTAINER Matt Selph <matt.selph@gmail.com> | github.com/mattselph

# install node.js
RUN apt-get update && apt-get install -y curl git
RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs

# install express and the mysql module
RUN npm install express mysql --save

