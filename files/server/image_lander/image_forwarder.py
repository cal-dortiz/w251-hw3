import boto3
import paho.mqtt.client as mqtt
import datetime
import numpy as np

LOCAL_MQTT_HOST = "serv-mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC ="face_finder" 

print(f'{LOCAL_MQTT_HOST} {LOCAL_MQTT_PORT}')
print(type(LOCAL_MQTT_HOST), type(LOCAL_MQTT_PORT))

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client,userdata, msg):
  try:
    print("message received: ",str(msg.payload.decode("utf-8")))
    session = boto3.Session(
        aws_access_key_id='',
        aws_secret_access_key=''
        )

    #Creating S3 Resource From the Session.
    s3 = session.resource('s3')

    # Convery binary to image
    img_str = msg.payload
    nparr = np.fromstring(img_str, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1

    # Generate File Name
    #  ts = datetime.datetime.now()
    date_time = now.strftime('%m-%d-%Y-%H-%M-%S')
    file_name = date_time + '_image.png'

    cv2.imwrite(file_name, img_np)

    # Define object
    object = s3.Object('w251-hw3-2022-ortiz', img))

    # Place image in s3 
    result = object.put(Body=txt_data)

  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, port=1883, keepalive=60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
