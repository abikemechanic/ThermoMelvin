# import paho
# from paho.mqtt import client as mqtt
import paho.mqtt.client as mqtt


class MQTTHandler:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.mqtt_client = mqtt.Client()
        self.connected = False
        self.last_message = None

        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.on_message = self.on_message

        self.connect()
        self.topic_subscribe()

    def connect(self):
        self.mqtt_client.connect(self.host, self.port)

    def on_connect(self, cli, userdata, flags, rc):
        self.connected = True

    def on_disconnect(self, cli, userdata, rc):
        self.connected = False

    def on_message(self, cli, userdata, message):
        print("Message: " + message.payload.decode())
        self.last_message = message

    def topic_subscribe(self):
        self.mqtt_client.subscribe('home/cat/mango/can_opened')
