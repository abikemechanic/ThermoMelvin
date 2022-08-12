from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont


class EPDImage:
    def __init__(self):
        self.epd = epd2in13_V2.EPD()
        self.pixel_width = self.epd.width
        self.pixel_height = self.epd.height
        self.image = Image.new('1', (self.pixel_height, self.pixel_width), 255)
        self.draw = ImageDraw.Draw(self.image)

        self.small_font = ImageFont.truetype(r'fonts\Courier Prime.ttf', 12)
        self.large_font = ImageFont.truetype(r'fonts\Courier Prime.ttf', 20)

        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.Clear(0xFF)



