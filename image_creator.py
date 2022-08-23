import datetime

from PIL import Image, ImageDraw, ImageFont
from mqtt_handler import MQTTHandler as MQTT
from paho.mqtt import client


class ImageCreator:
    small_font = ImageFont.truetype(r'fonts/Courier Prime Bold.ttf', 12)
    large_font = ImageFont.truetype(r'fonts/Courier Prime Bold.ttf', 20)

    def __init__(self, pixel_width=250, pixel_height=122):
        self.pixel_width = pixel_width
        self.pixel_height = pixel_height

        self._last_message: client.MQTTMessage = client.MQTTMessage()
        self._last_fish = datetime.datetime.strptime('1/1/1990', '%m/%d/%Y')
        self._last_chicken = datetime.datetime.strptime('1/1/1990', '%m/%d/%Y')

        self.image = Image.new('1', (self.pixel_height, self.pixel_width), 255)
        self.draw = ImageDraw.Draw(self.image)
        self.mqtt = MQTT('192.168.1.13', 1883)
        self.mqtt.mqtt_client.on_message = self.mqtt_message_recv

    @property
    def last_message(self):
        return self._last_message

    @last_message.setter
    def last_message(self, value):
        self._last_message = value
        print(value.payload.decode())
        if 'fish' in self._last_message.payload.decode().lower():
            self._last_fish = datetime.datetime.now()
        elif 'chicken' in self._last_message.payload.decode().lower():
            self._last_chicken = datetime.datetime.now()

    def add_text(self, text: str, font=large_font, line=0):
        # how to keep track of lines
        self.draw.text((0, line * 15), text, font=font, fill=0)

    def clear_image(self):
        self.image = Image.new('1', (self.pixel_height, self.pixel_width), 255)
        self.draw = ImageDraw.Draw(self.image)

    def mqtt_message_recv(self, cli, userdata, message):
        print(f'Message from ImageCreator: {message.payload.decode()}')
        self.last_message = message

