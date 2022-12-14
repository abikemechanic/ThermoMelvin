from image_creator import ImageCreator
import datetime

from waveshare_epd import epd2in13_V2


class EPDImage(ImageCreator):
    def __init__(self):
        self.epd = epd2in13_V2.EPD()
        self.pixel_width = self.epd.width
        self.pixel_height = self.epd.height

        self._last_message: str = ''
        self._last_fish = datetime.datetime.now()
        self._last_chicken = datetime.datetime.now()

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

        print(value.payload.decode())
        if 'fish' in self._last_message.payload.decode().lower():
            self._last_fish = datetime.datetime.now()
        elif 'chicken' in self._last_message.payload.decode().lower():
            self._last_chicken = datetime.datetime.now()

        self.clear()
        self.create_image()
        self.show_image()

    @property
    def last_fish(self):
        return self._last_fish

    @last_fish.setter
    def last_fish(self, value):
        self._last_fish = datetime.datetime.now()
        print(f'Last Fish at: {value.strftime("%H:%M")}')

    @property
    def last_chicken(self):
        return self._last_chicken

    @last_chicken.setter
    def last_chicken(self, value):
        self._last_chicken = datetime.datetime.now()
        print(f'Last Chicken at: {value.strftime("%H:%M")}')

    def show_image(self):
        self.epd.display(self.epd.getbuffer(self.image))

    def clear(self):
        self.clear_image()
        self.epd.Clear(0xFF)

    def create_image(self):
        self.add_text(f'Last Chicken:', line=0)
        self.add_text(f'    {self.last_chicken.strftime("%H:%M, %m/%d")}', line=1)

        self.add_text(f'Last Fish:', line=3)
        self.add_text(f'    {self.last_fish.strftime("%H:%M, %m/%d")}', line=4)
