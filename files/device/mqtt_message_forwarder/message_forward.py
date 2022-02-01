import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST = "cli-mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC ="face_finder" 

remote_mqttclient = mqtt.Client()
remote_mqttclient.connect("3.90.8.234", 30001)
REMOTE_MQTT_TOPIC = "face_finder"

print(f'{LOCAL_MQTT_HOST} {LOCAL_MQTT_PORT}')
print(type(LOCAL_MQTT_HOST), type(LOCAL_MQTT_PORT))

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_publish(client,userdata,result): #create function for callback
    print("data published \n")
    pass

def on_message(client,userdata, msg):
  try:
    #print("message received: ",str(msg.payload.decode("utf-8")))
    print("message received: ")   

    # Forward Message
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg.payload, qos=0, retain=False)
    print('message sent')

  except:
    print("Unexpected error:", sys.exc_info()[0])

print('Connecting to local host...')
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, port=1883, keepalive=60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
