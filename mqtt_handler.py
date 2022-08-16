import paho.mqtt.client as mqtt


class MQTTHandler:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.mqtt_client = mqtt
        self.connected = False
        self.last_message = None

        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.on_message = self.on_message

        self.connect()

    def connect(self):
        self.mqtt_client.connect(self.host, self.port)

    def on_connect(self, cli, userdata, flags, rc):
        self.connected = True

    def on_disconnect(self, cli, userdata, rc):
        self.connected = False

    def on_message(self, cli, userdata, message):
        print("Message: " + message.payload)
        self.last_message = message
