FROM centos:6.6
MAINTAINER Victor root@100pp.com
RUN yum clean all -y
USER root
RUN yum update -y && yum upgrade -y
#USER root
RUN yum install postfix -y
ADD ./main.cf /tmp
ADD ./ss.sh /tmp
WORKDIR /tmp
RUN mv main.cf /etc/postfix/
RUN chmod 775 ss.sh
EXPOSE 25
#ENTRYPOINT service postfix start && /bin/bash
ENTRYPOINT ./ss.sh && service postfix start && /bin/bash
