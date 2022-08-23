from image_creator import ImageCreator
from mqtt_handler import MQTTHandler

from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont


class EPDImage(ImageCreator):
    def __init__(self):
        self.epd = epd2in13_V2.EPD()
        self.pixel_width = self.epd.width
        self.pixel_height = self.epd.height

        self._last_message: str = ''

        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.Clear(0xFF)

        print('created RPi image display')

        super().__init__(self.pixel_width, self.pixel_height)

    @property
    def last_message(self):
        return self._last_message

    @last_message.setter
    def last_message(self, value):
        self._last_message = value
        self.clear()
        self.add_text(value)
        self.show_image()

    def show_image(self):
        self.epd.display(self.epd.getbuffer(self.image))

    def clear(self):
        self.clear_image()
        self.epd.Clear(0xFF)
