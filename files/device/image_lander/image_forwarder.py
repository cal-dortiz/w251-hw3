import os
import boto3
import paho.mqtt.client as mqtt
import cv2
from datetime import datetime
import numpy as np

# LOCAL_MQTT_HOST = "serv-mosquitto-service"
LOCAL_MQTT_HOST ='10.43.155.173'
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC ="face_finder" 

#K8s Cred from Secret
ACCESS_KEY_ID = os.environ['USERNAME']
SECRET_ACCESS_KEY = os.environ['PASSWORD']

BUCKET = 'w251-hw3-2022-ortiz'

#S3 Connection
s3 = boto3.client('s3', 
                  aws_access_key_id=ACCESS_KEY_ID,
                  aws_secret_access_key=SECRET_ACCESS_KEY)

print(f'{LOCAL_MQTT_HOST} {LOCAL_MQTT_PORT}')
print(type(LOCAL_MQTT_HOST), type(LOCAL_MQTT_PORT))

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client,userdata, msg):
    try:
        # get payload
        img = msg.payload

        # Generate File Name
        date_time = datetime.now().strftime('%m-%d-%Y-%H-%M-%S')
        file_name = str(date_time) + '_image.png'

        # Save Image
        nparr = np.frombuffer(img, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imwrite(file_name, img)

        # Upload Image 
        s3.upload_file(file_name, BUCKET, str(file_name))
        print('wrote file name: ', file_name)

    except:
        print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, port=1883, keepalive=60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
