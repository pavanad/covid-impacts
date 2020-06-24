
FROM python:3.6-stretch

WORKDIR /opt

COPY . /opt/bot
COPY requirements.txt /etc

RUN pip install pip --upgrade
RUN pip install -r /etc/requirements.txt

CMD python bot