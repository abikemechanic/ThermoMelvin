from PIL import Image, ImageDraw, ImageFont


class WindowsImage:
    def __init__(self):
        self.pixel_width = 122
        self.pixel_height = 250
        self.image = Image.new('1', (self.pixel_height, self.pixel_width), 255)
        self.draw = ImageDraw.Draw(self.image)

        self.small_font = ImageFont.truetype(r'fonts\Courier Prime Bold.ttf', 12)
        self.large_font = ImageFont.truetype(r'fonts\Courier Prime Bold.ttf', 20)

    def add_text(self, text):
        self.draw.text((0, 0), text, font=self.large_font, fill=0)
        self.draw.text((0, 18), text, font=self.small_font, fill=0)

    def show_image(self):
        self.image.show('test')
