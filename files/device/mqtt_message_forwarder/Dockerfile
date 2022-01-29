FROM alpine:latest
# this is needed to make sure we can see the log output
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apk update 
RUN apk add python3 
RUN apk add py3-pip
RUN apk add mosquitto
RUN pip3 install paho-mqtt
COPY message_forward.py message_forward.py
CMD python3 message_forward.py

