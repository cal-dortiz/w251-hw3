HW3 - Containers and Virtualization
===========================
<img align="right" width="130" src="./images/berkeley.png"/>

#### Authors : [Daniel Ortiz](https://github.com/cal-dortiz/)


U.C. Berkeley, Master of Information & Data Science Program - [datascience@berkeley](https://datascience.berkeley.edu/) 

Spring 2022, W251 - Deep Learning at the Cloud and on the Edge <br>
Wednesday, 4:00pm PDT

----

# Required Technology
---
 - Ubuntu 18.04 or compatible linuix OS
 - Docker
 - Kuberneties running Docker container (k3s)
 - Jetson Nano
 - AWS Account

 # File Structure
 ----
 |path|Description|
 |----|-----------|
 |/device/face_finder| Application to detect a face in webcam feed |
 |/device/image_lander| Device level transfer to S3 bucket|
 |/device/mqtt_broker| Device level MQTT Broker |
 |/device_mqtt_message_forwarder| Device - AWS MQTT bridge |
 |/device/mqtt_message_logger| Listen for logs on device broker |
 |/server/image_lander| Server level image transfer to s3 |
 |/server/server_broker| Server side MQTT Broker |
 |/server/server_logger_tbls| Listener for server MQTT Broker|
 |question_response| Response to 2 questions in homework|

 # s3 Image Repository Examples
 ___
https://w251-hw3-2022-ortiz.s3.amazonaws.com/02-01-2022-05-17-04_image.png
https://w251-hw3-2022-ortiz.s3.amazonaws.com/02-01-2022-05-17-16_image.png
https://w251-hw3-2022-ortiz.s3.amazonaws.com/02-01-2022-05-17-34_image.png

## Core s3 Link
https://w251-hw3-2022-ortiz.s3.amazonaws.com/

# Reconstructing Docker Images
---

The current k8 yaml files will pull from my dockerhub (djortiz32) with arm images for the device and x86 images for the server. If you need to build new images to run on different architectures or operating systems use the following commands. (If the images is updated, you will need to update the yaml file to point to the new docker image)

## Reconstruct the image

docker build --no-cache -t <dockerUserId>/<imageName> .

## Push to your own docker repo

docker push <dockerUserId>/<imageName> 

## Test run the container

ducker run --rm -it <dockerUserId>/<imageName> 


# Client Set Up (K8s)
---

## Initiate MQTT Broker Deployment

kubectl apply -f files/device/mqtt_broker/deployment.yaml

## Initiate MQTT Broker Service

kubectl apply -f files/device/mqtt_broker/service.yaml

## Initiate MQTT Logger

kubectl apply -f files/device/mqtt_message_logger/logger_deployment.yaml

## Initiate MQTT Message Forwarder

**Requires file edit for IP and Port of server**

kubectl apply -f files/device/mqtt_message_logger/forward_deployment.yaml


## Initiate face_finder application

kubectl apply -f  files/device/face_finder/face_finder.yaml


# Server Set Up (K8s)
---

## Initiate MQTT Broker Deployment

kubectl apply -f files/server/server_broker/deployment.yaml

## Initiate MQTT Broker Service

kubectl apply -f files/server/server_broker/service.yaml

## Initiate file transfer

kubectl apply-f files/server/image_lander/image_lander.yaml


# Test Connections (k8s)

Review the logs on both the server and device side to check if the messeges are reaching the server

## Device Side

kubectl get pods -l app=cli-serv-bridge
kubectl logs <podName>

## Server Side
kubectl get pods -l app=serv-listener
kubectl lovs <podName>
---



