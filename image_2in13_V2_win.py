from image_creator import ImageCreator

from PIL import Image, ImageDraw, ImageFont


class WindowsImage(ImageCreator):
    def __init__(self):
        self.pixel_width = 122
        self.pixel_height = 250

        self._last_message: str = ""

        print('created windows image display')

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
        self.image.show('test')

    def clear(self):
        self.clear_image()
        print('nothing to clear on Windows')
