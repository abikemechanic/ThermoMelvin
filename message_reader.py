import datetime


class MessageReader:
    def __init__(self):
        self._last_fish = ''
        self._last_chicken = ''

    @property
    def last_fish(self):
        return self._last_fish

    @last_fish.setter
    def last_fish(self, value):
        self._last_fish = datetime.datetime.now()

    @property
    def last_chicken(self):
        return self._last_chicken

    @last_chicken.setter
    def last_chicken(self, value):
        self._last_chicken = datetime.datetime.now()
