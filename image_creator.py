from PIL import Image, ImageDraw, ImageFont
from mqtt_handler import MQTTHandler as mqtt


class ImageCreator:
    small_font = ImageFont.truetype(r'fonts/Courier Prime Bold.ttf', 12)
    large_font = ImageFont.truetype(r'fonts/Courier Prime Bold.ttf', 20)

    def __init__(self, pixel_width=250, pixel_height=122):
        self.pixel_width = pixel_width
        self.pixel_height = pixel_height

        self.image = Image.new('1', (self.pixel_height, self.pixel_width), 255)
        self.draw = ImageDraw.Draw(self.image)
        self.mqtt = mqtt('192.168.1.13', 1883)

    def add_text(self, text: str):
        self.draw.text((0, 0), text, font=self.large_font, fill=0)

    def clear_image(self):
        self.image = Image.new('1', (self.pixel_height, self.pixel_width), 255)
        self.draw = ImageDraw.Draw(self.image)
