FROM alpine:3.10

# setup user
RUN adduser -D sick

# install prereqs

RUN apk add --update python \
    && cd /tmp \
    && wget https://pypi.python.org/packages/source/C/Cheetah/Cheetah-2.4.4.tar.gz \
    && tar -zxvf Cheetah-2.4.4.tar.gz \
    && cd Cheetah-2.4.4 \
    && python setup.py install \
    && mkdir /app \
    && chown sick:users /app

# install sickbeard

USER sick

RUN cd /app \
    && wget --no-check-certificate https://github.com/midgetspy/Sick-Beard/tarball/master \
    && tar -xzvf master \
    && mv midgetspy*/ my-sickbeard-install 

VOLUME ["/config", "/sickdata", "/sickmedia"]

EXPOSE 8081

# run sickbeard
CMD cd /app/my-sickbeard-install && python SickBeard.py --datadir /config
