from image_creator import ImageCreator

from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont


class EPDImage(ImageCreator):
    def __init__(self):
        self.epd = epd2in13_V2.EPD()
        self.pixel_width = self.epd.width
        self.pixel_height = self.epd.height
        self.image = Image.new('1', (self.pixel_height, self.pixel_width), 255)
        self.draw = ImageDraw.Draw(self.image)

        self.small_font = ImageFont.truetype(r'fonts/Courier Prime Bold.ttf', 12)
        self.large_font = ImageFont.truetype(r'fonts/Courier Prime Bold.ttf', 20)

        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.Clear(0xFF)

        print('crated RPi image display')

        super().__init__(self.pixel_width, self.pixel_height)

    def add_text(self, text):
        self.draw.text((0, 0), text, font=self.large_font, fill=0)
        self.draw.text((0, 18), text, font=self.small_font, fill=0)

    def show_image(self):
        print(type(self.image))
        self.epd.display(self.image)
