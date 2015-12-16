# Readability container
#
# VERSION		0.1

FROM ubuntu:trusty
MAINTAINER Matt Selph <matt.selph@gmail.com>

LABEL Description="This container calculates a readability score" Version="0.1"

RUN apt-get update
RUN apt-get install -y python3-pip wget
RUN pip3 install py-readability
RUN python3 -m nltk.downloader cmudict

WORKDIR /root
RUN wget -O readability.py https://gist.githubusercontent.com/mattselph/0eb8d1fa3595b69cab6a/raw/8982a156c5b86b200d9a4ed5ef1c5b8bf3aacf64/readability.py

ENTRYPOINT ["python3", "/root/readability.py"]
