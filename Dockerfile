FROM docker.io/centos/python-38-centos7


# 기본 환경 설치 명령어
#RUN yum update -y
#RUN yum install -y python
#RUN yum -y install epel-release && yum clean all
#RUN yum -y install python-pip && yum clean all

# 개발 소스 폴더 copy 
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt

# 실행 명령어
CMD [ "python", "discordbot.py" ]