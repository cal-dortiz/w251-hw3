# w251-hw3
w251-hw3


# Required Technology
---
 - Ubuntu 18.04 or compatible linuix OS
 - Docker
 - Kuberneties running Docker container (k3s)
 - Jetson Nano
 - AWS Account


# AWS Provisions
---

## Provision VPC

## Setup EC2 Security Group

## Provision EC2 instance

## Provision s3 bucket

## Setup s3 Permissions


# Client Set Up
---

## Initiate MQTT Broker Deployment

kubectl apply -f files/device/mqtt_broker/deployment.yaml

## Initiate MQTT Broker Service

kubectl apply -f files/device/mqtt_broker/service.yaml

## Initiate MQTT Logger

kubectl apply -f files/device/mqtt_message_logger/logger_deployment.yaml

## Initiate MQTT Message Forwarder

**Requires file edit post server setup**

kubectl apply -f files/device/mqtt_message_logger/forward_deployment.yaml


## Initiate face_finder application




# Server Set Up
---

## Initiate MQTT Broker Deployment

kubectl apply -f files/server/server_broker/deployment.yaml

## Initiate MQTT Broker Service

kubectl apply -f files/server/server_broker/service.yaml

## Initiate file transfer


