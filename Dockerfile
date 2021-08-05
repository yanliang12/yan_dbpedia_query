##################Dockerfile##################
FROM openjdk:8

RUN apt-get update
RUN apt-get install -y bzip2 
RUN apt-get install -y wget
RUN apt-get install -y gcc 
RUN apt-get install -y git 
RUN apt-get install -y curl

RUN apt-get update
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip

RUN pip3 install gdown==3.12.2
RUN pip3 install requests==2.24.0
RUN pip3 install pandas==1.1.3
RUN pip3 install elasticsearch==7.11.0
RUN pip3 install pyspark==3.1.1
RUN pip3 install esdk-obs-python==3.20.11 --trusted-host pypi.org
RUN pip3 install Pillow==8.2.0
RUN pip3 install xlrd==1.1.0
RUN pip3 install xlsxwriter==1.4.3

RUN apt-get install -y zip 

RUN mkdir /yan/
RUN chmod 777 /yan/ 

RUN useradd -u 8877 yan
USER yan

RUN echo "sd1g6s1g52d0g5"

WORKDIR /yan/
COPY elasticsearch_dbpedia.tar.gz /yan/

WORKDIR /yan/
RUN tar -xzvf /yan/elasticsearch_dbpedia.tar.gz

RUN echo "sd4g5s1g6sg5"

WORKDIR /yan/
RUN git clone https://github.com/gaoyuanliang/jessica_kibana_docker.git
RUN mv jessica_kibana_docker/* ./
RUN rm -r jessica_kibana_docker

WORKDIR /yan/
RUN git clone https://github.com/yanliang12/yan_dbpedia_query.git
RUN mv yan_dbpedia_query/* ./
RUN rm -r yan_dbpedia_query
##################Dockerfile##################