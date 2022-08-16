from image_creator import ImageCreator

from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont


class EPDImage(ImageCreator):
    def __init__(self):
        self.epd = epd2in13_V2.EPD()
        self.pixel_width = self.epd.width
        self.pixel_height = self.epd.height

        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.Clear(0xFF)

        print('crated RPi image display')

        super().__init__(self.pixel_width, self.pixel_height)

    def show_image(self):
        self.epd.display(self.epd.getbuffer(self.image))

    def clear(self):
        self.clear_image()
        self.epd.Clear(0xFF)
