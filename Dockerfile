FROM python:3.8-alpine

RUN apk --update upgrade

COPY requirements.txt /opt/portfolio/requirements.txt

EXPOSE 9181

RUN python3 -m pip install --upgrade pip \
    pip install -r /opt/portfolio/requirements.txt

ADD . /opt/porfolio

WORKDIR /opt/porfolio

CMD ["python3", "-u", "app.py"]

