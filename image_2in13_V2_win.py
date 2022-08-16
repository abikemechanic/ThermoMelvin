from image_creator import ImageCreator

from PIL import Image, ImageDraw, ImageFont


class WindowsImage(ImageCreator):
    def __init__(self):
        self.pixel_width = 122
        self.pixel_height = 250

        print('created windows image display')

        super().__init__(self.pixel_width, self.pixel_height)

    def show_image(self):
        self.image.show('test')

    def clear(self):
        self.clear_image()
        print('nothing to clear on Windows')
