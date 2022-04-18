import pytest
from classes import *

class Test:
    tv1 = Television()

    def test_init(self):
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tv1.power()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

        self.tv1.power()
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

    def test_channel_up(self):
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'

        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'

        self.tv1.channel_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'

        self.tv1.channel_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_volume_up(self):
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'

        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
