# VERSION 0.01
#
# mysql on Debian wheezy

FROM debian:wheezy
MAINTAINER Matt Selph <matt.selph@gmail.com> | github.com/mattselph

# install mysql 
RUN apt-get update && apt-get install -y mysql-server

# listen on all addresses 
RUN sed -i -e"s/^bind-address\s*= 127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf

# add admin user for outside connections
RUN /usr/sbin/mysqld & \
    sleep 10s && \
    echo "GRANT ALL ON *.* TO admin@'%' IDENTIFIED BY 'changeme' WITH GRANT OPTION; FLUSH PRIVILEGES" | mysql


EXPOSE 3306

CMD ["mysqld_safe"]
