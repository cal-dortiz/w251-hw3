import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST = "cli-mosquitto-service"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC ="face_finder" 

REMOTE_MQTT_HOST = "10.43.53.158"
REMOTE_MQTT_PORT = 1883
REMOTE_MQTT_TOPIC = "face_finder"

print(f'{LOCAL_MQTT_HOST} {LOCAL_MQTT_PORT}')
print(type(LOCAL_MQTT_HOST), type(LOCAL_MQTT_PORT))

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_connect_remote(client, userdata, flags, rc):
        print("connected to remote broker with rc: " + str(rc))
	
def on_message(client,userdata, msg):
  try:
    print("message received: ",str(msg.payload.decode("utf-8")))
    
    # Establish Remote connection
    print('Connecting to remote...')

    print(f'{REMOTE_MQTT_HOST} {REMOTE_MQTT_PORT}')
    print(type(REMOTE_MQTT_HOST), type(REMOTE_MQTT_PORT))

    remote_mqttclient = mqtt.Client()
    remote_mqttclient.on_connect = on_connect_remote
    remote_mqttclient.connect(REMOTE_MQTT_HOST, port=1883, keepalive=60)

    # Forward Message
    msg = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

print('Connecting to local host...')
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, port=1883, keepalive=60)


#print('Connecting to remote...')
#remote_mqttclient = mqtt.Client()
#remote_mqttclient.on_connect = on_connect_remote
#remote_mqttclient.connect(REMOTE_MQTT_HOST, port=1880, keepalive=60)

local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
