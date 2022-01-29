import paho.mqtt.client as mqtt
  

LOCAL_MQTT_HOST = "10.43.53.158"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC ="face_finder" 

print(f'{LOCAL_MQTT_HOST} {LOCAL_MQTT_PORT}')
print(type(LOCAL_MQTT_HOST), type(LOCAL_MQTT_PORT))

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, port=1883, keepalive=60)

#publish the message
local_mqttclient.publish(LOCAL_MQTT_TOPIC,"Hello MQTT...")
